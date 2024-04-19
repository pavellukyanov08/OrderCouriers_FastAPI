FROM python:latest

WORKDIR /fastapi_app

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /fastapi_app/requirements.txt
COPY ./app /fastapi_app/app

RUN pip install --no-cache-dir --upgrade -r /fastapi_app/requirements.txt
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
