#!/usr/bin/env bash


pypy3 manage.py collectstatic --no-input
pypy3 manage.py makemigrations
pypy3 manage.py migrate
pypy3 manage.py createsuperuser --no-input
pypy3 manage.py runserver 0.0.0.0:8000
