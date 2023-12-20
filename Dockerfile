FROM python:3.11.6-bullseye


RUN apt update && apt install python3-pip -y

RUN python3 -m pip install mysql-connector-python


WORKDIR /app

COPY connect_and_run.py .

#EXPOSE 80

ENTRYPOINT ["python3", "connect_and_run.py" ]


