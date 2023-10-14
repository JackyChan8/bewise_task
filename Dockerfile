FROM python:3.11-slim-buster

WORKDIR /quiz

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# Copy Project
COPY . /quiz/

RUN pip install -r requirements.txt

EXPOSE 8000