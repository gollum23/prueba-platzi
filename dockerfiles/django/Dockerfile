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

# Install ssh server
RUN apt-get install -y openssh-server && \
apt-get clean
# Update pip
RUN pip3 install -U pip

# Change dir and create folder for app
RUN cd /opt && \
mkdir django_app

# Define Work dir
WORKDIR /opt/django_app

# Add file to docker
# ADD ./django_ssh.sh /django_ssh.sh
ADD ./django_dev.sh /django_dev.sh
ADD ./django_run.sh /django_run.sh

# Change permission for execute
RUN chmod +x /*.sh

# CMD ["/bin/bash", "/django_ssh.sh"]

# Set environ vars
#ENV DJANGO_SETTINGS_MODULE app.settings.dev
ENV DB_USER 'platzi'
ENV DB_PASS 'platzi2016'
ENV SECRET_KEY 'ss(h^m+9*6-cs5$d*l8oa_zrg8!&hv^813pi4#6mv(9+e*-re4'
ENV DB 'prueba_platzi'
ENV HOST 'mysql'

RUN mkdir /var/run/sshd
RUN echo 'root:platzi2016' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile


# Setting port to expose
EXPOSE 8000 22
CMD ["/usr/sbin/sshd", "-D"]
