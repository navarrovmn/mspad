FROM python:3.6.5

RUN apt-get update
RUN apt-get update && apt-get install -f -y postgresql-client
WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

RUN chmod +x /app/runserver.sh
