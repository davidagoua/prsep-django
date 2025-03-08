
FROM python:3.12-bullseye

WORKDIR /app

ENV DJANGO_SETTINGS_MODULE="prsep.settings.dev"
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate
#RUN python3 manage.py loaddata data.json


EXPOSE 8000


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "prsep.wsgi:application"]