# Test Platzi

App build in python 3.4.3 and django 1.9.2 using stripe api, docker and unit testing.

## Installing

### Build docker images and run containers

#### Build mysql docker image

```bash
docker build --rm -t platzi/mysql ./dockerfiles/mysql/
```

#### Build django docker image

```bash
docker build --rm -t platzi/django ./dockerfiles/django/
```

#### Create docker container for data
```
docker create --name=platzi-data -v /var/lib/mysql platzi/mysql true
```

#### Run docker container mysql using docker container data
```
docker run -idt -p 3306:3306 --volumes-from platzi-data --name=platzi-mysql platzi/mysql
```

#### Create docker container for django app
```
docker run -idt -p 8000:8000 --name=platzi-django -v <ruta folder descarga proyecto>:/opt/django_app/ --privileged=true --link platzi-mysql:mysql platzi/django
```

### Config mysql docker

Create user and database

```
docker exec -it platzi-mysql sh /config_mysql.sh
```

### Config django docker

Install requirements and start project app

```
docker exec -it platzi-django sh /django_dev.sh
```

Run migrations

```
docker exec -it platzi-django python3 ./app/manage.py migrate
```

Run server

```
docker exec -it platzi-django sh /django_run.sh
```
