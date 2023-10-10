#!/bin/sh

while ! nc -z $DJANGO_DATABASE_HOST $DJANGO_DATABASE_PORT; do
  sleep 0.1
done

echo MYSQL запущен
python3 ./app/manage.py runserver