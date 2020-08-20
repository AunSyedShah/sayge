import json
from rest_framework.test import APIClient
import pytest
from django.contrib.auth.tokens import default_token_generator
from djoser import utils
from users.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_create_user():
    client = APIClient()
    url = reverse('user-list')  # '/auth/users/'
    response = client.get(url)
    assert response.status_code == 401 or response.status_code == 403
    assert response.json()['detail'] == 'Authentication credentials were not provided.'

    response = client.put(url)
    assert response.status_code == 401 or 401 or response.status_code == 403
    assert response.json()['detail'] == 'Authentication credentials were not provided.'

    response = client.delete(url)
    assert response.status_code == 401 or 401 or response.status_code == 403
    assert response.json()['detail'] == 'Authentication credentials were not provided.'

    response = client.post(url)
    assert response.status_code == 400, 'POST without data'
    data = response.json()

    expected_errors = [
        'email',
        'first_name',
        'last_name',
        'password',
    ]

    assert set(expected_errors) == set(data.keys()), 'This field is required.'
    payload = json.dumps({
        "email": "testuser@gmail.com",
        "first_name": "test",
        "last_name": "user",
        "password": "poilk123",
    })
    response = client.post(url, content_type='application/json', data=payload)
    assert response.status_code == 201, 'User Created'


@pytest.mark.django_db
def test_activate_user():
    client = APIClient()
    signup_url = reverse('user-list')  # '/auth/users/'
    # testing without data
    response = client.post(signup_url, content_type='application/json', data={})
    assert response.status_code == 400, 'uid and token required'

    payload = json.dumps({
        "email": "testuser+1@gmail.com",
        "first_name": "test",
        "last_name": "user",
        "password": "poilk123",
    })
    response = client.post(signup_url, content_type='application/json', data=payload)
    data = response.json()
    user = User.objects.get(email=data['email'])
    uid = utils.encode_uid(user.pk)
    token = default_token_generator.make_token(user)

    activate_url = reverse('user-activation')  # '/auth/users/activation/'
    payload = json.dumps({
        'uid': uid,
        'token': token
    })
    activate_response = client.post(activate_url, content_type='application/json', data=payload)

    assert activate_response.status_code == 204


@pytest.mark.django_db
def test_login_user():
    client = APIClient()
    signup_url = reverse('user-list')  # '/auth/users/'
    login_url = reverse('login')  # '/auth/token/login/'
    payload = json.dumps({
        "email": "testuser+2@gmail.com",
        "first_name": "test",
        "last_name": "user",
        "password": "poilk123",
    })
    response = client.post(signup_url, content_type='application/json', data=payload)
    data = response.json()
    user = User.objects.get(email=data['email'])
    uid = utils.encode_uid(user.pk)
    token = default_token_generator.make_token(user)

    # user not active
    login_payload = json.dumps({
        'email': 'testuser+2@gmail.com',
        'password': 'poilk123'
    })

    login_response = client.post(login_url, content_type='application/json', data=login_payload)
    assert login_response.status_code == 400, 'User Not activated'
    non_field_errors = login_response.json()['non_field_errors']
    assert non_field_errors[0] == 'Unable to log in with provided credentials.'

    # wrong credentials
    login_payload = json.dumps({
        'email': 'testuser+2@gmail.com',
        'password': 'poilk567'
    })
    login_response = client.post(login_url, content_type='application/json', data=login_payload)
    assert login_response.status_code == 400, 'User Not activated'
    non_field_errors = login_response.json()['non_field_errors']
    assert non_field_errors[0] == 'Unable to log in with provided credentials.'

    # activate user
    activate_url = reverse('user-activation')  # '/auth/users/activation/'
    payload = json.dumps({
        'uid': uid,
        'token': token
    })
    client.post(activate_url, content_type='application/json', data=payload)

    login_payload = json.dumps({
        'email': 'testuser+2@gmail.com',
        'password': 'poilk123'
    })
    login_response = client.post(login_url, content_type='application/json', data=login_payload)

    assert login_response.status_code == 200

    assert login_response.json()['auth_token']
