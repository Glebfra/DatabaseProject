FROM nginx

ADD . /etc/nginx

RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/django.conf /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/react.conf /etc/nginx/sites-enabled/

RUN cd /etc/nginx

EXPOSE 80
EXPOSE 443
CMD ["nginx"]
