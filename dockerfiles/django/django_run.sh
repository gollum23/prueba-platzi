#!/usr/bash

__run_django() {
    cd /opt/django_app/app/
    python3 manage.py runserver 0.0.0.0:8000
}

__run_django
