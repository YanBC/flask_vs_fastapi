FROM python:3.10.12-slim-bullseye

COPY fastapi /workspace

WORKDIR /workspace

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

STOPSIGNAL 2

CMD ["uvicorn", "hello:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
