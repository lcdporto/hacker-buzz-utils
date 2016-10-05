FROM ubuntu:14.04

RUN apt-get update && \
apt-get install -y python3-pip

COPY app /app

RUN pip3 install -r /app/requirements.txt

CMD tail -f /dev/null