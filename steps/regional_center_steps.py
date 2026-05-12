from pages.selectors.regional_center_selectors import *
from behave import *
from time import *
@when('I select the second regional center from the list')
def step_impl(context):
    context.base_page.click_button(SELECT_CENTER)
    sleep(2)
@when('I click on succursale drop_down list')
def step_impl(context):
    context.base_page.click_button(SUCCURSALE_DROPDOWN)
    sleep(2)

@when('I select the succursale from the list')
def step_impl(context):
    context.base_page.click_button(SELECTED_SUCCURSALE)
    sleep(2)
@when('I click on modify button')
def step_impl(context):
    context.base_page.click_button(MODIFY_CENTER)
    sleep(2)

@when('I clear the phone number text box')
def stept_impl(context):
    context.base_page.delete_input(PHONE_NUMBER)
    sleep(2)

@when('I complete with a new phone number')
def step_impl(context):
    context.base_page.insert_input("40766696235",PHONE_NUMBER)
    sleep(2)

@when('I click on save')
def step_impl(context):
    context.base_page.click_button(SAVE_CENTER)
    sleep(2)

