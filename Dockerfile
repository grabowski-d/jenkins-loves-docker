FROM python:3.8.8-slim-buster

WORKDIR /app

COPY app/server.py ./

ENV SERVER_PORT=8000
EXPOSE 8000

CMD [ "python", "./server.py" ]
