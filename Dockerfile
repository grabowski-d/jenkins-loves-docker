FROM python:3.8.8-slim-buster

WORKDIR /app

COPY app/server.py ./

ARG SERVER_PORT=8000
EXPOSE ${SERVER_PORT}

CMD [ "python", "./server.py" ]
