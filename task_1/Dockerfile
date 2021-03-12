# BASE IMAGE
FROM python:3.8.5-alpine
# CREATOR
MAINTAINER Vittcal Neestackich <neestackich@gmail.com>

# SETS CONSTANT ENVIRONMENT VARIABLES
# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

# EXECUTES COMMAND AND CREATES NEW LAYER
# apk - Alpine Linux package manager
RUN apk update && apk add gcc libc-dev linux-headers
# CREATE WORK DIRECTORY
RUN mkdir -p /usr/src/app/

# SET WORK DIRECTORY
WORKDIR /usr/src/app/
# COPIES LOCAL FILES TO CONTAINER
COPY . /usr/src/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# DESCRIBES COMMAND THAT WILL BE EXECUTED WHEN CONTAINER IS LAUNCHED
CMD ["python", "task.py"]
