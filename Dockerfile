# Build and run docker with your example
#  docker build -t instabot2 .
#  docker run --name instabot2 -p 80:80 -i -t instabot2 python examples/welcome_message.py

# Build and run docker with your example
# Build and run docker with your example
FROM ubuntu:latest

# Env varible
ENV CODE_REPO https://github.com/moreno19/instabot2

# Environment setup
RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y install \
    	python-pip \
    	python-dev \
    	build-essential \
    	git \
    	wget \
    	vim

# TODO: Need to update. Currently this breaks.
# RUN pip install --upgrade pip \
# 	&& pip install --upgrade virtualenv 

RUN mkdir host_env \
	&& cd host_env \
	&& git clone ${CODE_REPO} 

WORKDIR /host_env

RUN pip install -e git+http://github.com/moreno19/instabot2.git#egg=instabot2
