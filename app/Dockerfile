FROM python:3.10.6-alpine

COPY . /var/lib/django
WORKDIR /var/lib/django

RUN apk add --virtual build-deps gcc python3-dev musl-dev

RUN cd /var/lib/django
RUN pip install -r requirements.txt

CMD python3 ./app/manage.py runserver
