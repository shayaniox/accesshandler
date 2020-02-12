FROM ubuntu:18.04
ENV TZ=Asia/Tehran DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8
RUN apt-get update -y \
  && ln -sf /usr/share/zoneinfo/$TZ /etc/localtime \
  && apt-get install -y apt-utils locales tzdata \
  && locale-gen en_US.UTF-8 \
  && update-locale LANG=$LANG LC_ALL=$LANG LANGUAGE=$LANG\
  && apt-get install --no-install-suggests --no-install-recommends -y \
  libass-dev libpq-dev postgresql build-essential tzdata redis-server \
  redis-tools python3-pip python3-dev \
  && apt-get autoremove -y && rm -rf /var/lib/apt/lists/* 
WORKDIR /usr/local/accesshandler
COPY . .
RUN mkdir -p /etc/accesshandler && pip3 install --no-cache-dir -U \ 
  pip setuptools wheel gunicorn \
  && pip install .
RUN sed -ir "/^\s*bind/ s/\s*bind/# &/p" /etc/redis/redis.conf \
  && echo "bind 127.0.0.1" >> /etc/redis/redis.conf \
  && groupadd -r accesshandler \
  && useradd -rg accesshandler accesshandler \
  && echo "d /run/accesshandler 0755 accesshandler accesshandler -" > \
  /usr/lib/tmpfiles.d/accesshandler.conf \
  && echo "listen_addresses = '*'"  >> /etc/postgresql/10/main/postgresql.conf\
  && echo "db:\n  url: postgresql://accesshandler:@/accesshandler\n\ndebug: \
  false" > /etc/accesshandler/config.yml \
  && echo "from accesshandler import accesshandler\n\naccesshandler.configure\
  (filename='/etc/accesshandler/config.yml')\naccesshandler.initialize_orm()\
  \n\napp = accesshandler" > /etc/accesshandler/wsgi.py
RUN service postgresql start && service redis-server start \
  && su postgres -c \
  "psql -U postgres -c \"ALTER USER postgres PASSWORD 'postgres';\
  CREATE USER accesshandler;\"" \
  && echo " CREATE DATABASE accesshandler OWNER accesshandler;" | su postgres -c psql \
  && su accesshandler -c \
  "accesshandler -c /etc/accesshandler/config.yml db create --drop --mockup"
EXPOSE 8080
CMD service postgresql start \
    && service redis-server start \
    && /usr/local/bin/gunicorn \
    --bind :8080 \
    --chdir /etc/accesshandler \
    wsgi:app
