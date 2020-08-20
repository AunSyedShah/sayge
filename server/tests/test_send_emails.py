from django.urls import reverse


def test_send_emails(client, mailoutbox):
    url = reverse('api-send-emails')

    response = client.get(url)
    assert response.status_code == 405, 'GET not allowed'

    response = client.put(url)
    assert response.status_code == 405, 'PUT not allowed'

    response = client.delete(url)
    assert response.status_code == 405, 'DELETE not allowed'

    response = client.post(url)
    assert response.status_code == 400, 'POST without data'
    data = response.json()
    expected_errors = [
        'first_name',
        'last_name',
        'work_email',
        'phone_number',
        'company_name',
        'employee_count_range',
    ]
    assert set(expected_errors) == set(data['errors'].keys()), 'Unexpected field error'

    assert len(mailoutbox) == 0, 'Mailbox should be empty'

    payload = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'work_email': 'work@example.com',
        'phone_number': '',
        'company_name': 'Company Name',
        'employee_count_range': '1_50',
    }
    response = client.post(url, data=payload)
    assert response.status_code == 201, 'Something is wrong with the data'
    data = response.json()

    assert len(mailoutbox) == 1, 'Only 1 email should be sent'

    payload['employee_count_range'] = 'unknown'
    response = client.post(url, data=payload)
    assert response.status_code == 400, 'Employee count range is wrong'
    errors = response.json()['errors']
    assert 'employee_count_range' in errors, 'employee_count_range should be in errors'
    assert errors['employee_count_range'][0] == '"unknown" is not a valid choice.'
