FROM python:latest

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install -r requirements.txt

COPY requirements.txt .
COPY . .

WORKDIR /app





CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
