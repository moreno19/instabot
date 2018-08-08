# Build and run docker with your example
#  docker build -t instabot .
#  docker run --name instabot -p 80:80 -i -t instabot python examples/welcome_message.py

FROM python:3.6
WORKDIR /opt/app
COPY . /opt/app
COPY requirements.txt /tmp/

RUN pip install --requirement /tmp/requirements.txt
ADD examples/ usr/local/examples
