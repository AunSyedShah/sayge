# Development

## Quickstart

This is a quickstart guide in case you have most of the requirements already installed.

### Environment
```shell
export PYTHONPATH=$PWD/server:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=sayge_ai.settings
export DATABASE_URL=postgres:///sayge_ai
export SECRET_KEY='SECRET_KEY'
export SENTRY_DSN=''

export ALLOWED_HOSTS='localhost'
export DEBUG=true
export CONTACT_EMAILS=hello@sayge.ai.example.com
export EMAIL_HOST=localhost
export EMAIL_HOST_USER=
export EMAIL_HOST_PASSWORD=
export EMAIL_PORT=1025
export EMAIL_USE_TLS=false

export REACT_APP_API_URL=http://localhost:8000/api
```
For a more detailed guide see [Environment](environment.md)

### Server side
```shell
$ poetry install
$ poetry run django-admin migrate
$ poetry run django-admin runserver
$ poetry run django-admin createsuperuser
```
For a more detailed guide see [Python](python.md)

### Client side
```shell
$ yarn install
$ yarn run start
```
For a more detailed guide see [JavaScript](javascript.md)
