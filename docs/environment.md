
## Environment

This project uses environment variables to configure behaviour and credentials.
Use a shell script or something like https://direnv.net/ to automate the setup:

The environment should have these available:
```shell
export PATH=$HOME/.cache/pypoetry/virtualenvs/sayge-ai-khQhfck1-py3.8/bin:$PATH
export PATH=$PWD/client/node_modules/.bin:$PATH
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
export SNOWFLAKE_PRODUCTION_TESTS_ENABLED=true
export SNOWFLAKE_USER=
export SNOWFLAKE_PASSWORD=
export SNOWFLAKE_ACCOUNT=
export REACT_APP_API_URL=http://localhost:8000/api
```
