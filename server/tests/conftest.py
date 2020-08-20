import os
import pytest
from collections import namedtuple
from django.test.client import Client

ANONYMOUS, CLIENT, ADMIN = 'ANONYMOUS', 'CLIENT', 'ADMIN'


@pytest.fixture
def roles(django_user_model):
    roles = [(CLIENT, None), (ADMIN, 'is_superuser')]
    clients = {}
    for username, attr in roles:
        email = f'{username}@example.com'
        user = django_user_model.objects.create_user(
            username=username, email=email, password=username
        )
        if attr:
            setattr(user, attr, True)
            user.save()

        client = Client()
        client.user = user
        client.login(email=email, password=username)
        clients[username] = client

    Roles = namedtuple('Roles', ['anonymous', 'client', 'admin'])
    return Roles(
        anonymous=Client(),
        client=clients[CLIENT],
        admin=clients[ADMIN]
    )


def pytest_collection_modifyitems(items):
    snowflake_tests_enabled = os.getenv('SNOWFLAKE_PRODUCTION_TESTS_ENABLED', False) == 'true'
    for item in items:
        if not snowflake_tests_enabled and "snowflake_production" in item.nodeid:
            item.add_marker(pytest.mark.skip)
