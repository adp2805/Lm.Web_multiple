from time import sleep

from behave import *


from pages.selectors.login_selectors import *
from pages.selectors.homepage_selectors import *


# primul lucru in login, importam libraria behave


@given("I access the Lm.web homepage") # Ce este intre ghilimele trebuie sa fie identic cu ce avem in 01_login.feature
                                        # fara spatiu fara punct, identic!!!!
def step_impl(context):
    context.login_page.go_to_login_page()

@when('I insert username')
def step_impl(context):
    context.base_page.insert_input("editec", USERNAME)
    sleep(2)

@when('I insert username "{username_value}"')
def step_impl(context,username_value):
    context.base_page.insert_input(username_value,USERNAME)

@when('I insert password "{password}"')
def step_impl(context,password):
    context.base_page.insert_input(password,PASSWORD)


@when('I insert password')
def step_impl(context):
    context.base_page.insert_input("editec",PASSWORD)
    sleep(2)

@when('I click login button')
def step_impl(context):
    # context.login_page.click_login_button()
    context.base_page.click_button(LOGIN_BUTTON)
    sleep(2)

@Then('I should receive an unsuccessful login message: "{expected_err_message}"')
def step_impl(context,expected_err_message):
    context.base_page.verify_err_msg_outline(expected_err_message,WRONG_PASSWORD_MSG)

@when('I click logout button')
def step_impl(context):
    context.login_page.click_logout_button(LOGOUT_BUTTON)
    sleep(5)
# @then('I should be on the loggin page')
# def step_impl(context):


# @when('I insert a wrong password')
# def step_impl(context):
#     context.login_page.insert_password()


# @then('I should see an error message "invalid credentials"')
# def step_impl(context):
#     context.login_page.click_login_button()
