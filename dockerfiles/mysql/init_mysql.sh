#!/bin/bash

__mysql_init() {
    echo "Running setup mysql function"
    rm -rf /var/lib/mysql/
    mysql_install_db
    chown -R mysql:mysql /var/lib/mysql
    /usr/bin/mysqld_safe &
    sleep 10
}

__mysql_init
