#!/usr/bash

__install_requirements() {
    cd /opt/django_app/
    pip install -r ./requirements/dev.txt
}

__create_django_app() {
    cd /opt/django_app/
    django-admin startproject app
}

__install_requirements
__create_django_app
