#!/bin/sh

set -e

if [ -n "$DM_NAME" ]; then
    sed -i "s#http://0.0.0.0:8000#$DM_NAME#g" templates/index.html
fi

cp -r -f templates/base_site.html /usr/local/lib/python3.6/site-packages/django/contrib/admin/templates/admin/
cp -r -f docker/nginx.conf /etc/nginx/

exec "$@"