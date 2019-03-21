#!/bin/sh
cd /code

/venv/bin/python manage.py collectstatic --noinput
/venv/bin/python manage.py makemigrations peytalaneApp
/venv/bin/python manage.py migrate
touch db.sqlite
/bin/chmod 666 db.sqlite


exec "$@"
