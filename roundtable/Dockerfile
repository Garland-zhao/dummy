FROM ubuntu:20.04
LABEL maintainer="zhaofan<garland_zhao@foxmail.com>"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3.8 python3.8-dev python3-pip
RUN apt-get install build-essential  \
    libldap2-dev libsasl2-dev slapd ldap-utils tox \
    lcov valgrind cron curl vim -y

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3.8 get-pip.py

WORKDIR /roundtable
ENV DEBUG=xxxx
ENV DB_NAME=xxxx
ENV DB_USER=xxxx
ENV DATABASE_HOST='x.x.x.x'
ENV DATABASE_PORT='xxxx'

ADD . /roundtable
RUN pip3.8 install -r requirement.txt

RUN python3.8 manage.py makemigrations && python3.8 manage.py migrate
CMD python3.8 manage.py runserver 0.0.0.0:xxxx
