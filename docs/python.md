# Python

## Poetry

This project uses Poetry to manage Python development and production environment.
Installation: https://python-poetry.org/docs/#installation 

If you'd like to have installed packages/scripts in your PATH check `poetry env info` output for virtualenv path and add this to your environment:
```shell
export PATH=$HOME/.cache/pypoetry/virtualenvs/<INSERT sayge-ai venv>/bin:$PATH
```
Note: replace the `<INSERT ...>` path with a valid path.

## Project setup

In project root run:
```shell
$ poetry install
$ poetry run django-admin migrate
$ poetry run django-admin runserver
```

If you need anything else just use `poetry run django-admin` like you'd use `python manage.py`.

## Debug email

This command will output any email sent and should be used for local development and debugging only.
```shell
$ poetry run django-admin mail_debug
```

## Create a superuser
```shell
$ poetry run django-admin createsuperuser
```
