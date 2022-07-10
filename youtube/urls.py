from django.urls import path

from youtube.views import fetch_video_records

urlpatterns = [
    path('fetch-video-records', fetch_video_records, name='fetch_video_records')]