FROM python:3.8

RUN apt update
RUN apt-get install cron -y
RUN alias py=python

ENV PYTHONUNBUFFERED 1

# WORKDIR /usr/src/app
#
# COPY ./app .
# COPY ./requirements.txt /usr/src/app

WORKDIR /code/
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN pip install -r requirements.txt

# django-crontab logfile
# RUN mkdir /cron
# RUN touch /cron/django_cron.log

# EXPOSE 8000
#
# CMD service cron start && python manage.py runserver 0.0.0.0:8000