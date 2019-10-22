from selenium.webdriver.common.by import By
from behave import *
import time


@given('I navigate to the login page')
def navigate_to_page(context):
    context.login_page.navigate('login')


@when('I login with an "{cred_type}" credential combination')
def step_impl(context, cred_type):
    context.login_page.fill_login_credentials(cred_type, context)


@when('I login with a "{cred_type}" credential combination')
def step_impl(context, cred_type):
    context.login_page.fill_login_credentials(cred_type, context)


@then('I should see the invalid credentials login error message')
def step_impl(context):
    assert context.login_page.creds_error_message() == context.text


@then('I should see the Free Agent Login page')
def verify_login_page_title(context):
    assert context.login_page.get_page_title() == 'FreeAgent : Login', "page title doesn't match"


@then('I should see the Free Agent Overview page')
def verify_overview_page_title(context):
    assert context.overview_page.get_page_title() == 'FreeAgent : Overview', "page title doesn't match"

