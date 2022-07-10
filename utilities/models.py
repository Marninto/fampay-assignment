from django.db import models

# Create your models here.


class YoutubeDevKey(models.Model):
    gmail = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    # should be expandable if it helps with checking key quota available

    class Meta:
        db_table = 'youtube_dev_key'

    def put_data(self, *args, **kwargs):
        super(YoutubeDevKey, self).save(*args, **kwargs)

    @classmethod
    def fetch_active_keys(cls):
        return cls.objects.filter(is_active=True)

    @classmethod
    def fetch_first_active_key(cls):
        return cls.objects.filter(is_active=True).first()

    @classmethod
    def mark_key_inactive(cls, key_id):
        # ideally a cron will update inactive keys back to active in midnight PDT
        obj = cls.objects.filter(id=key_id)
        if obj:
            obj.is_active = False
            obj.save()
        return None
