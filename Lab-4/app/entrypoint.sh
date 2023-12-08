#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL 

#gunicorn django_project.wsgi:application --bind 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000