import asyncio

from utilities.models import YoutubeDevKey
from utilities.services.youtube_api_service import YoutubeService
from youtube.models import YoutubeFeed, QueryData


class YoutubeRecords:

    @classmethod
    def fetch_youtube_feeds(cls, query, page, limit):
        if len(query) > 100:
            return {'success': False, 'message': 'Query must be under 100 char', 'data': None}
        query_data = QueryData.fetch_query_id(query=query.lower())
        if not query_data:
            feed_resp = YoutubeRecords.populate_feed(query=query, page=0)
            if not feed_resp['success']:
                return feed_resp
            query_data = QueryData.fetch_query_id(query=query.lower())
        query_data_len = len(query_data)
        query_page = int(page/5)
        if query_page <= query_data_len:
            youtube_records = YoutubeFeed.fetch_records(query_id=query_data[query_page].id, page=page % 5, limit=limit)
        else:
            # not done gaming handling
            feed_resp = YoutubeRecords.populate_feed(query=query, page=query_page+1)
            if not feed_resp['success']:
                return feed_resp
            youtube_records = YoutubeFeed.fetch_records(query_id=query_data[query_page].id, page=page % 5, limit=limit)
        return {'success': True, 'message': 'Query fetch success',
                'data': YoutubeRecords.jsonify_feeds(youtube_records)}

    @classmethod
    def jsonify_feeds(cls, feed_records):
        feed_record = []
        for records in feed_records:
            feed_record.append({
                'video_id': records.video_id,
                'video_title': records.video_title,
                'publish_date': records.publish_date,
                'video_desc': records.video_desc,
                'thumbnail': records.thumbnail
            })
        return feed_record

    @classmethod
    def populate_feed(cls, query, page):
        active_keys = YoutubeDevKey.fetch_active_keys()
        if not active_keys:
            return {'success': False, 'message': 'No active key available', 'data': None}
        for key in active_keys:
            youtube_resp = YoutubeService.fetch_search_data(query=query, key=key.api_key)
            if youtube_resp and youtube_resp['success']:
                if not youtube_resp['data']:
                    key.is_active = False
                    key.save()
                    continue
                else:
                    # todo improvize on response time by splitting response
                    #  traverse for records and executing remaining on delay
                    update_resp = YoutubeRecords.update_new_query(query, page, youtube_resp['data'])
                    if not update_resp['success']:
                        return update_resp
            else:
                return {'success': False, 'message': 'Something went wrong when accessing googledata apis',
                        'data': None}
        return {'success': True, 'message': 'Success fetching data', 'data': None}

    @classmethod
    def update_new_query(cls, query, page, payload):
        data = payload['items']
        if not data:
            return {'success': False, 'message': 'No data fetched', 'data': None}
        QueryData(query=query.lower(), page=page, etag=payload['etag'],
                  next_page_key=payload['nextPageToken']).put_data()
        query = QueryData.fetch_query_id(query=query.lower())
        bulk_payload = []
        for fetched_feed in data:
            bulk_payload.append(
                YoutubeFeed(video_id=fetched_feed['id']['videoId'],
                            video_title=fetched_feed['snippet']['title'],
                            publish_date=fetched_feed['snippet']['publishedAt'],
                            video_desc=fetched_feed['snippet']['description'],
                            thumbnail=fetched_feed['snippet']['thumbnails']['default']['url'],
                            query_id=query[0].id)
            )
        YoutubeFeed.objects.bulk_create(bulk_payload)
        return {'success': True, 'message': 'Data updated', 'data': None}
