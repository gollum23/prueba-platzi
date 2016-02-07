#!/bin/bash

__mysql_start() {
    echo "Starting mysql"
    mysqladmin -u root password platzi2016
    mysql -uroot -pplatzi2016 -e "CREATE USER 'platzi'@'localhost' IDENTIFIED BY 'platzi2016';"
    mysql -uroot -pplatzi2016 -e "GRANT ALL PRIVILEGES ON *.* TO 'platzi'@'localhost' WITH GRANT OPTION;"
    mysql -uroot -pplatzi2016 -e "CREATE USER 'platzi'@'%' IDENTIFIED BY 'platzi2016';"
    mysql -uroot -pplatzi2016 -e "GRANT ALL PRIVILEGES ON *.* TO 'platzi'@'%' WITH GRANT OPTION;"
    mysql -uroot -pplatzi2016 -e "FLUSH PRIVILEGES;"
    mysql -uplatzi -pplatzi2016 -e "CREATE DATABASE prueba_platzi;"
    #mysql -uplatzi -pplatzi2016 -e "GRANT ALL PRIVILEGES ON prueba_platzi.* TO 'platzi'@'localhost' IDENTIFIED BY 'platzi2016' WITH GRANT OPTION; FLUSH PRIVILEGES;"
    #mysql -uroot -pplatzi2016 -e "GRANT ALL PRIVILEGES ON *.* TO 'platzi'@'localhost' WITH GRANT OPTION; FLUSH PRIVILEGES;"
    mysql -uroot -pplatzi2016 -e "select user, host FROM mysql.user;"
    killall mysqld
    sleep 10
}

__mysql_start
