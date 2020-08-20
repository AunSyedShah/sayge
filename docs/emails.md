# Emails

## Send an email

`POST /api/emails`

The API endpoint allows any user (anonymous or authenticated) to send an email.

## Request

Endpoint expects these fields/params to exist in a request:
- `first_name` min. length 1, max. length 200
- `last_name` min. length 1, max. length 200
- `work_email` valid email
- `phone_number` optional but required in request (blank/emtpy value)
- `company_name` min. length 1, max. length 200
- `employee_count_range` available choices:
  - `1_50`: 1-50 employees
  - `51_200`: 51-200 employees
  - `201_500`: 201-500 employees
  - `501+`: 501+ employees

## Response

`HTTP 201`
The request was successfully processed.

`HTTP 400`
The request data is not valid (example: `employee_count_range` value is not one of the available choices).

Response example:
```yaml
{
"errors": {
    "employee_count_range": ["\\"unknown\\" is not a valid choice."]
  }
}
```

## Unsupported HTTP methods

`GET, PUT, DELETE, ...` etc. are not allowed.

## Development, debugging and testing

See [Python docs](python.md) for instructions on howto setup local development/debugging.
See [Email tests](../server/tests/test_send_emails.py) to get a better idea how the API is implemented.
