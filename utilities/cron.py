import requests

from utilities.models import Test


def my_cron_job():
    resp = requests.get(url='http://127.0.0.1:8001/knockknock')
    return resp
