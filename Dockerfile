FROM python:3

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y postgresql-client

#ENV PYTHONUNBUFFERED=1

COPY . .

COPY .env .