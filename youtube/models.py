from django.core.paginator import Paginator
from django.db import models

# Create your models here.


class QueryData(models.Model):
    query = models.CharField(max_length=100, unique=True)
    page = models.IntegerField(default=0)
    etag = models.CharField(max_length=50)
    next_page_key = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'query_data'

    def put_data(self, *args, **kwargs):
        super(QueryData, self).save(*args, **kwargs)

    @classmethod
    def fetch_query_id(cls, query):
        return cls.objects.filter(query=query, is_active=True).order_by('-page')

    @classmethod
    def fetch_all_base_query(cls):
        return cls.objects.filter(page=0, is_active=True).order_by('-id')

    @classmethod
    def disable_old_fetches(cls, query):
        cls.objects.filter(query=query).update(is_active=False)


class YoutubeFeed(models.Model):
    video_id = models.CharField(max_length=100)
    video_title = models.CharField(max_length=500)
    publish_date = models.DateTimeField()
    video_desc = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=100)
    video_etag = models.CharField(max_length=50)
    query = models.ForeignKey(QueryData, null=True, on_delete=models.SET_NULL)
    # to use mapping if we want to avoid duplicacy but db calls will increase

    class Meta:
        db_table = 'youtube_feed'

    def put_data(self, *args, **kwargs):
        super(YoutubeFeed, self).save(*args, **kwargs)

    @classmethod
    def fetch_records(cls, query_id, page, limit=10):
        data = cls.objects.filter(query_id=query_id).order_by('-publish_date')
        if page:
            txn_paginator = Paginator(data, limit)
            last_page = txn_paginator.num_pages
            if last_page < page:
                return []
            txn_paginator = txn_paginator.get_page(page)
            data = txn_paginator.object_list
        return data


class QueryFeedMapper(models.Model):
    query = models.ForeignKey(QueryData, null=True, on_delete=models.SET_NULL)
    feed = models.ForeignKey(YoutubeFeed, null=True, on_delete=models.SET_NULL)
    publish_date = models.DateTimeField()

    class Meta:
        db_table = 'query_feed_mapper'

    def put_data(self, *args, **kwargs):
        super(QueryFeedMapper, self).save(*args, **kwargs)
