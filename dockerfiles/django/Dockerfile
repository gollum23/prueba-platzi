FROM ubuntu:14.04

MAINTAINER Diego Forero <gollum23[at]gmail.com>

# Update system
RUN apt-get update -y --fix-missing && \
apt-get upgrade -y && \
apt-get clean

# Install dev libs and pip for python 3
RUN apt-get install -y build-essential && \
apt-get install -y python3-dev && \
apt-get install -y python3-setuptools && \
apt-get install -y python3-pip && \
apt-get clean

# Install mysql lib dev for compile mysql python package
RUN apt-get install -y libmysqlclient-dev && \
apt-get clean

# Update pip
RUN pip3 install -U pip

# Change dir and create folder for app
RUN cd /opt && \
mkdir django_app

# Define Work dir
WORKDIR /opt/django_app

# Add file to docker
ADD ./django_dev.sh /django_dev.sh
ADD ./django_run.sh /django_run.sh

# Change permission for execute
RUN chmod +x /*.sh

# Set environ vars
#ENV DJANGO_SETTINGS_MODULE app.settings.dev
ENV DB_USER 'platzi'
ENV DB_PASS 'platzi2016'
ENV SECRET_KEY 'ss(h^m+9*6-cs5$d*l8oa_zrg8!&hv^813pi4#6mv(9+e*-re4'
ENV DB 'prueba_platzi'
ENV HOST 'mysql'

# Setting port to expose
EXPOSE 8000
