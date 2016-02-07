# Test Platzi

App build in python 3.4.3 and django 1.9.2 using stripe api, docker and unit testing.

## Installing

### Build docker images and containers

Build mysql docker image

```bash
docker build --rm -t platzi/mysql ./dockerfiles/mysql/
```

Build django docker image

```bash
docker build --rm -t platzi/django ./dockerfiles/django/
```

### Create docker container for data
```
docker create --name=platzi-data -v /var/lib/mysql platzi/mysql true
```

### Run docker container mysql using docker container data
```
docker run -idt -p 3306:3306 --volumes-from platzi-data --name=platzi-mysql platzi/mysql
```
