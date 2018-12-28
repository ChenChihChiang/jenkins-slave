FROM jenkins/slave:3.26-1-alpine
MAINTAINER Oleg Nenashev <o.v.nenashev@gmail.com>
LABEL Description="This is a base image, which allows connecting Jenkins agents via JNLP protocols" Vendor="Jenkins project" Version="3.23"
USER root

RUN apk upgrade
RUN apk add gawk
RUN apk add curl
RUN apk add docker
RUN apk add python
RUN apk add py-pip
RUN pip install awscli
RUN apk add php
RUN apk add php-curl
RUN apk add php-json

COPY jenkins-slave /usr/local/bin/jenkins-slave
COPY docker-java-home /usr/local/bin/docker-java-home

ENTRYPOINT ["jenkins-slave"]
