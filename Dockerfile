FROM debian:stable

EXPOSE 8000
WORKDIR /app/bin
CMD ["./run-docker.sh"]

RUN apt-get update && apt-get install -y --no-install-recommends build-essential python-pip python-dev && apt-get clean -y

ADD requirements.txt /app/requirements.txt
RUN cd /app && pip install -r requirements.txt

ADD . /app/
