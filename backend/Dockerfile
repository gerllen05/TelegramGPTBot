FROM python:3.8-slim-bullseye

RUN apt-get update && apt-get upgrade -y
# RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential

RUN pip install pipenv


COPY ./Pipfile /opt
COPY ./Pipfile.lock /opt
WORKDIR /opt

RUN pip install -r --system --deploy

CMD ["python", "main.py"]



