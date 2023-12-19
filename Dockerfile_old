FROM ubuntu:22.04

RUN apt update && apt install python3 python3-pip -y

RUN python3 -m pip install mysql-connector-python

RUN mkdir -p /workdir

COPY src /workdir

WORKDIR /workdir

ENTRYPOINT [ "python3", "main.py" ]


