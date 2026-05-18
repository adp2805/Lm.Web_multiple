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

