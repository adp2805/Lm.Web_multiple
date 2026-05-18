from behave import *
from time import *
from pages.selectors.login_selectors import *
from pages.selectors.homepage_selectors import *
@when('I should be logged in and I should see the LM.web homepage')
def step_impl(context):
    context.home_page.verify_login_successful()
    sleep(5)

@when ('I click Succursales button')
def step_impl(context):
    context.base_page.click_button(SUCCURSALES)
    sleep(5)

@when ('I click on Terminal section')
def step_impl(context):
    context.base_page.click_button(TERMINALBUTTON)
    sleep(2)

@when('I click on regional center button')
def stept_impl(context):
    context.base_page.click_button(REGIONAL_CENTER)
    sleep(2)
@when('I click on retailers section')
def step_impl(context):
    context.base_page.click_button(RETAILER)
    sleep(2)
@when('I click on Agent button')
def step_impl(context):
    context.base_page.click_button(AGENT_BUTTON)
    sleep(2)

@then('I click on Logout button')
def step_impl(context):
    context.base_page.click_button(LOGOUT_BUTTON)
