from behave import *
from time import *
from pages.selectors.terminalspage_selectors import *
from test_data import *
from selenium.common.exceptions import *
@when ('I click on ID to search a terminal by ID')
def step_impl(context):
    context.base_page.click_button(SEARCHBYID)
    sleep(2)

@when('I fill-out the terminal id')
def step_impl(context):
    context.base_page.insert_input(terminal_id, TERMINALID)
    sleep(2)

@when ('I click on search button')
def step_implu(context):
    context.base_page.click_button(SEARCHTBUTTON)
    sleep(4)

@when ('I click on the selected terminal')
def step_impl(context):
    context.base_page.click_button(SELECT_TERMINAL)
    sleep(4)

@when('I click on modify terminal button')
def step_impl(context):
    context.base_page.click_button(MODIFY_BUTTON)
    sleep(2)
@when('I manage group allocation')
def step_impl(context):
    is_allocated = context.base_page.find_elements(SELECTED_GROUP_ALLOCATED)
    if is_allocated:
        context.base_page.click_button(SELECT_GROUP)
        context.base_page.click_button(REMOVE_GROUP)
    else:
        context.base_page.click_button(SELECT_GROUP)
        context.base_page.click_button(ALLOW_GROUP)
    sleep(2)



@when ("I click on save terminal")
def step_impl(context):
    context.base_page.click_button(SAVE_TERMINAL)
    sleep(2)

#@when('I should not see any err message: {err}')
# def step_impl(context,err):
#     context.base_page.verify_err_msg(err, SAVE_ERR)
#     sleep(2)

