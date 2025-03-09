
FROM python:3.12-bullseye

WORKDIR /app

ENV DJANGO_SETTINGS_MODULE="prsep.settings.dev"
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/




EXPOSE 8000

