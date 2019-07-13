FROM python:3.7-alpine3.9
RUN apk update \
    && apk add --update build-base \
    && apk add --no-cache python3 \ 
    && pip install gunicorn \
    #server dependendencies
    && pip install flask \
    && pip install flask-sqlalchemy \
    && pip install requests \
    && pip install pymysql \
    && pip install mysql-connector 

WORKDIR /app-run
COPY . /app-run

ENTRYPOINT gunicorn -w 4 --bind 0.0.0.0:5000 --chdir /app-run/src/ server:app --reload
 