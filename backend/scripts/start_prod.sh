#!/usr/bin/env bash

pypy3 manage.py collectstatic --no-input
pypy3 manage.py makemigrations
pypy3 manage.py migrate --no-input
pypy3 manage.py createsuperuser --no-input
gunicorn backend.wsgi -b 0.0.0.0:8000
