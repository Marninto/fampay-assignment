import requests


def my_cron_job():
    requests.get(url='http://127.0.0.1:8001/knockknock')
    print('working')