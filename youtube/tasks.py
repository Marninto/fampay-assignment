from utilities.models import YoutubeDevKey
from utilities.services.youtube_api_service import YoutubeService
from youtube.models import QueryData


# ideal scheduling by celery_beat/airflow
from youtube.services.youtube_records import YoutubeRecords


def sync_existing_data():
    query_keys = QueryData.fetch_all_base_query()
    active_keys = YoutubeDevKey.fetch_active_keys()
    if not active_keys:
        return {'success': False, 'message': 'No active key available', 'data': None}
    update_success = False
    for query_key in query_keys:
        for key in active_keys:
            if update_success:
                continue
            youtube_resp = YoutubeService.fetch_search_data(query=query_key.query, key=key.api_key)
            if youtube_resp and youtube_resp['success']:
                if not youtube_resp['data']:
                    key.is_active = False
                    key.save()
                    active_keys = YoutubeDevKey.fetch_active_keys()
                    update_success = False
                    continue
                else:
                    update_success = True
                    if query_key.etag == youtube_resp['data']['etag']:
                        continue
                    else:
                        QueryData.disable_old_fetches(query_key.query)
                        YoutubeRecords.update_new_query(query_key.query, 0, youtube_resp['data'])
            else:
                break
