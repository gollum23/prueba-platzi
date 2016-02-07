#!/bin/bash

__start_supervisor() {
    echo "Starting supervisor"
    supervisord -n
}

__start_supervisor
