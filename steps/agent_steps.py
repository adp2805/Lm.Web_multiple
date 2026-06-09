from time import *
from behave import *
from pages.base_page import *
from pages.selectors.agent_selectors import *
from test_data import *


@when('I click on Search by Id')
def step_impl(context):
    context.base_page.click_button(SEARCHBYID)
    sleep(2)

@when('I insert the Agent Id')
def step_impl(context):
    context.base_page.insert_input(agent_id,INSERT_AGENT_ID) #modify in test_data file what agent id you want to test.
    sleep(2)

@when('i click on agent search button')
def step_impl(context):
    context.base_page.click_button(SEARCH_BUTTON)
    sleep(2)

@when('I click on the specify agent')
def step_impl(context):
    context.base_page.click_button(SELECT_AGENT)
    sleep(2)

@when('I click on modify agent')
def step_impl(context):
    context.base_page.click_button(MODIFY_AGENT)
    sleep(2)

@when('I manage terminals allocation')
def step_impl(context):
    is_allocated = context.base_page.find_elements(ALLOCATED_TERMINALS)
    if is_allocated:
        context.base_page.click_button(TERMINAL_FOR_TEST)
        context.base_page.click_button(DEALOCATE_TERMINAL_BTN)
    else:
        context.base_page.click_button(TERMINAL_FOR_TEST)
        context.base_page.click_button(ALOCATE_TERMINAL_BTN)
    sleep(2)

@when('I clear the phone number')
def step_impl(context):
    context.base_page.delete_input(PHONE_TEXTBOX)
    sleep(2)
@when('I insert the new phone number as "{phone_number}"')
def step_impl(context,phone_number):
    context.base_page.insert_input(phone_number,PHONE_TEXTBOX)
    sleep(2)
@when('I click on add phone number')
def step_impl(context):
    context.base_page.click_button(ADDPHONE_BUTTON)
    sleep(2)

@When('I clear agent_nb textbox')
def step_impl(context):
    context.base_page.delete_input(EXTERNAL_REFERENCE)
    sleep(2)

@when('I insert an existing External Reference as "{agent_nb}"')
def step_impl(context,agent_nb):
    context.base_page.insert_input(agent_nb,EXTERNAL_REFERENCE)
    sleep(2)

@Then('I should see error message "{expected_err}"')
def step_impl(context,expected_err):
    context.base_page.verify_err_msg_outline(expected_err,EXTERNAL_REFERENCE_ERR)
    sleep(2)