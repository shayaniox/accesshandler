FROM python:3.6

WORKDIR /usr/local/accesshandler
COPY . .

RUN pip3 install gunicorn
RUN pip3 install -e .

RUN mkdir /etc/accesshandler
RUN echo "db:\n  url: postgresql://postgres:password@pg:5432/accesshandler\n\
  administrative_url: postgresql://postgres:password@pg:5432/postgres \nredis_:\n\
  host: redis\n  port: 6379\n  password: ~\n  db: 1\
  \ndebug: true" > /etc/accesshandler/config.yml

RUN echo "from accesshandler import accesshandler\n\naccesshandler.configure\
  (filename='/etc/accesshandler/config.yml')\naccesshandler.initialize_orm()\
  \n\napp = accesshandler" > /etc/accesshandler/wsgi.py

EXPOSE 8080

CMD accesshandler -c /etc/accesshandler/config.yml db create --drop --mockup \
    && gunicorn --chdir /etc/accesshandler wsgi:app --bind :8080 
