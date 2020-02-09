#!/usr/bin/env bash

# Restart nginx and redis to strat successfully after editing their config
service redis-server restart
service nginx restart

# Clone accesshandler and install it
cd /usr/local/
git clone git@github.com:shayan-7/accesshandler.git
if [ $? != 0 ] ; then
  echo "Can not clone accesshandler. Check this problem"
  exit 1
fi
cd accesshandler
pip3.6 install -e .

# Create required directories and files:
echo "
db:
  url: postgresql://accesshandler:@/accesshandler

debug: false
" > /etc/accesshandler/config.yml

echo "
import os
from accesshandler import accesshandler


accesshandler.configure(files='/etc/accesshandler/config.yml')
accesshandler.initialize_orm()

app = accesshandler

" > /etc/accesshandler/wsgi.py

echo "
[Unit]
Description=Access Handler Back-end REST API
After=network.target

[Service]
PIDFile=/run/accesshandler/accesshandler.pid
User=accesshandler
Group=accesshandler
ExecStart=/usr/local/bin/gunicorn \
	--bind unix:/run/accesshandler/accesshandler.socket \
	--pid /run/accesshandler/accesshandler.pid \
	--chdir /etc/accesshandler \
	wsgi:app

ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID
PrivateTmp=true

[Install]
WantedBy=multi-user.target
" > /etc/systemd/system/accesshandler.service

echo "
upstream accesshandler_api {
    server unix:/run/accesshandler/accesshandler.socket fail_timeout=1;
}
server {
    listen 8080 default;
    root /var/www/html;
    index index.html;

    location /apiv1/ {
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_redirect off;
      proxy_pass http://accesshandler_api;
    }

    location / {
        try_files $uri $uri/ =404;
    }
}
" > /etc/nginx/sites-available/accesshandler.conf

ln -s /etc/nginx/sites-available/accesshandler.conf /etc/nginx/sites-enabled/accesshandler.conf
sudo -u accesshandler accesshandler --config-file /etc/accesshandler/config.yml db create --drop --mockup

# Restart services and starting accesshandler
service nginx restart
systemctl enable accesshandler.service
service accesshandler start

