FROM tiangolo/uwsgi-nginx:python3.6-alpine3.7
LABEL name=code6 Version=0.0.1

EXPOSE 8000
ENV LISTEN_PORT=8000
ENV UWSGI_INI uwsgi.ini



WORKDIR /app
ADD . /app
RUN chmod g+w /app
RUN chmod g+w /app/db.sqlite3

RUN python3 -m pip install -r requirements.txt