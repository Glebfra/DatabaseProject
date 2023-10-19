FROM python:3.10.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN apk add gcc libc-dev linux-headers nodejs mysql mysql-client mysql-dev

RUN mkdir /var/lib/django && mkdir /var/lib/django/app
COPY requirements.txt /var/lib/django/app/requirements.txt
RUN pip install -r /var/lib/django/app/requirements.txt

COPY . /var/lib/django/app
WORKDIR /var/lib/django/app

RUN cd /var/lib/django

RUN mkdir static

CMD uwsgi --http :8000 --wsgi-file /var/lib/django/app/app/wsgi.py --chmod-socket=666 --enable-threads
