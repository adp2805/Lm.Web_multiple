from time import *
from behave import *
from pages.selectors.retailer_selectors import *
from test_data import *
@when('I click on select retailer by id')
def step_impl(context):
    context.base_page.click_button(RETAILER_BY_ID)
    sleep(2)

@when('I insert retailer ID')
def step_impl(context):
    context.base_page.insert_input(retailer_id,INSER_RETAILER_ID)
    sleep(2)

@when('I click on search retailer')
def step_impl(context):
    context.base_page.click_button(SEARCH_RETAILER)
    sleep(2)

@when('I select the firs retailer')
def step_impl(context):
    context.base_page.click_button(SELECT_RETAILER)
    sleep(2)

@when('I click on modify retailer')
def step_impl(context):
    context.base_page.click_button(MODIFY_RETAILER)
    sleep(2)

@when('I clear the name')
def step_impl(context):
    context.base_page.delete_input(MODIFY_NAME)
    sleep(2)

@when('I insert the new name')
def step_impl(context):
    ret_name = "editec"
    context.base_page.insert_input(ret_name+"1",MODIFY_NAME)
    sleep(2)

@when('I clic on save retailer')
def step_impl(context):
    context.base_page.click_button(SAVE_RETAILER)
    sleep(2)
