from behave import *
from time import *
from pages.selectors.login_selectors import *
from pages.selectors.succursales_selectors import *
from pages.selectors.homepage_selectors import *
# @when ('I click on home button')
# def step_impl(context):
#     context.base_page.click_button(HOMEBUTTON)
#     sleep(2)

@when ("I select one succursale from the list")
def step_impl(context):
    context.base_page.click_button(TRDSUCCURSALE)
    sleep(2)

@when ("I click on modify succursale")
def step_impl(context):
    context.base_page.click_button(MODIFYSUC)
    sleep(2)
@when ("I delete the current name")
def step_impl(context):
    context.base_page.delete_input(DELETEINPUT)
    sleep(2)
@when ('I modify the name or the limit with "{succursale_name}"')
def step_impl(context,succursale_name):
    context.base_page.insert_input(succursale_name,MODIFY_SUC_NAME)
    sleep(2)

@when('I delete the current online payment limit')
def step_impl(context):
    context.base_page.delete_input(ONLINE_PAYMENT_LIMIT)
    sleep(2)

@when('I insert the new value "{payment_value}"')
def step_impl(context,payment_value):
    context.base_page.insert_input(payment_value,ONLINE_PAYMENT_LIMIT)
    sleep(2)

@when ("I click on save succursale")
def step_impl(context):
    context.base_page.click_button(SAVEBUTTON)
    sleep(2)
@when('I should see an succursale error message "{expected_err}"')
def step_impl(context,expected_err):
    context.base_page.verify_err_msg_outline(expected_err, EXPECTED_ERR)
    sleep(2)
@when ('I should get back to the homepage')
def step_impl(context):
    context.home_page.verify_login_successful()
    sleep(5)

