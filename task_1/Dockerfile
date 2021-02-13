FROM python:3.8.5-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add gcc libc-dev linux-headers

COPY ./requirements.txt .
 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .