FROM python:3.10.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /var/lib/django/app
WORKDIR /var/lib/django/app

RUN apk add gcc libc-dev linux-headers nodejs mysql mysql-client mysql-dev

RUN cd /var/lib/django
RUN pip install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:8000
