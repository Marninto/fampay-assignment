from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import (api_view)


@api_view(['GET'])
def health_check_api(request):
    return HttpResponse('<html><h1>Hello from the local service!<h1></html>', status=status.HTTP_200_OK)
