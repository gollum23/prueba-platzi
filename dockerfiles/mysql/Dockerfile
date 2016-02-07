FROM ubuntu:14.04

MAINTAINER Diego Forero <gollum23[at]gmail.com>

# Update system and clean cache apt
RUN apt-get update -y --fix-missing && \
apt-get upgrade -y && \
apt-get clean

# Install mysql server and clean cache apt
RUN apt-get install -y mysql-server && \
apt-get install pwgen && \
apt-get clean

# Install supervisor
RUN apt-get install -y supervisor && \
apt-get clean

# Add mysql config for supervisor
ADD mysql.conf /etc/supervisor/conf.d/mysql.conf

# Create Volumen data
VOLUME ["/etc/mysql", "/var/lib/mysql"]

# Include in system path mysql
# CMD ["export" "PATH=$PATH:/usr/local/mysql/bin/"]

# Add file to docker
# ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh
# ADD create_db.sh /create_db.sh
ADD init_mysql.sh /init_mysql.sh
ADD config_mysql.sh /config_mysql.sh
ADD init.sh /init.sh

# Add mysql config file
ADD my.cnf /etc/mysql/conf.d/my.cnf

# Change permissions
RUN chmod +x /*.sh

# Run setup mysql script
RUN /init_mysql.sh

# Setting port to expose
EXPOSE 3306

# Run mysql
CMD ["/bin/bash", "/init.sh"]
