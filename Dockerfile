FROM python:3.8-buster

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor

RUN pip3 install uwsgi
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

RUN useradd --no-create-home nginx

RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY supervisord.conf /etc/supervisor/
COPY webserver.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/
COPY uwsgi.ini /etc/uwsgi/

COPY /app /app

WORKDIR /app

EXPOSE 8080:8080

CMD ["/usr/bin/supervisord"]
