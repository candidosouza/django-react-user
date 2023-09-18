#!/bin/bash

cp .env.example .env

poetry config virtualenvs.in-project true
poetry install
poetry shell
.venv/bin/python manage.py migrate
.venv/bin/python manage.py seeds
.venv/bin/python manage.py manage.py runserver 0.0.0.0:8000
tail -f /dev/null