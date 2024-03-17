FROM python:3.10.4-buster
RUN apt-get update && apt-get install -y --no-install-recommends --yes nano netcat