import traceback

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from youtube.services.youtube_records import YoutubeRecords


@api_view(['GET'])
def fetch_video_records(request, version):
    limit = 10
    page = int(request.GET.get('page', 0))
    query = request.GET.get('query', None)
    try:
        data = YoutubeRecords.fetch_youtube_feeds(query=query, page=page, limit=limit)
        return Response(data, status=status.HTTP_200_OK)
    except Exception:
        tb = traceback.format_exc()
        return Response({'success': False, 'message': f'Something went wrong', 'data': None,
                         'exception': f'{tb}'}, status=status.HTTP_400_BAD_REQUEST)
