FROM ubuntu:20.04
USER root
ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update && apt-get install -y  \
        python3 python3-pip \
        git \
        zip \ 
        vim nano 
RUN python3 -m pip install --upgrade pip

RUN mkdir /usr/src/app/ && cd /usr/src/app/
COPY . ./
WORKDIR /usr/src/app/
