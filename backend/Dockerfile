FROM python:3.8-slim-bullseye

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential

COPY ./requirements.txt /opt
WORKDIR /opt

RUN pip install -r requirements.txt

CMD ["python", "main.py"]