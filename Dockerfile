FROM reg.cctv.cn/library/python:3.6-alpine-utc8
COPY . /src
WORKDIR /src
COPY docker/docker-entrypoint.sh /src
COPY docker/get-pip.py /src
RUN pip install -r requirements.txt \
    && mkdir -p /run/nginx \
    && apk add nginx \
    && apk add python \
    && /usr/bin/python2 /src/get-pip.py \
    && pip2 install supervisor \
    && mkdir -p /data/log/supervisor \
    && mkdir -p /src/log/supervisor/

COPY docker/supervisord.conf /etc/
COPY docker/nginx.ini /etc/supervisor.d/
COPY docker/home_index.ini /etc/supervisor.d/
ENTRYPOINT ["/src/docker-entrypoint.sh"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
#CMD ["gunicorn", "--bind=0.0.0.0:80", "home_index.wsgi:application"]
CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]