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
    && pip install mysql-connector \
    #setuptools dependencies
    && pip install docutils \
    && pip install pytest \
    && pip install pytest-runner \
    && pip install pytest-cov

WORKDIR /app-run
COPY . /app-run

ENTRYPOINT ash /app-run/init.sh
 