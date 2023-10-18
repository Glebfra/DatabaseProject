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

CMD python3 manage.py runserver 0.0.0.0:8000
