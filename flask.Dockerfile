FROM python:3.10.12-slim-bullseye

COPY flask /workspace

WORKDIR /workspace

RUN apt update

RUN apt install -y build-essential python3-dev  \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

STOPSIGNAL 2

CMD ["uwsgi", "--http", "0.0.0.0:8000", "--master", "-p", "2", "-w", "hello:app"]
