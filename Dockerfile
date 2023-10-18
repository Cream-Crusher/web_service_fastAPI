FROM python:3.10

WORKDIR /web_service_fastAPI

COPY ./requirements.txt /web_service_fastAPI/requirements.txt
COPY ./application /web_service_fastAPI/application
COPY ./config.py /web_service_fastAPI/config.py
COPY ./.env /web_service_fastAPI/.env

RUN pip install -r requirements.txt

# Запуск приложения
CMD ["uvicorn", "application.main:app", "--host", "0.0.0.0", "--port", "8000"]
