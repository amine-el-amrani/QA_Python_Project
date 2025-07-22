from behave import given, when, then
import requests

@given('I am an API client')
def step_impl(context):
    context.base_url = 'http://127.0.0.1:5000'

@when('I send a POST request to /users with name "{name}"')
def step_impl(context, name):
    context.response = requests.post(f'{context.base_url}/users', json={"name": name}, timeout=60)

@then('I should receive a {status_code} status code')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)

@then('the user "{name}" should be created')
def step_impl(context, name):
    response_json = context.response.json()
    assert response_json['name'] == name
