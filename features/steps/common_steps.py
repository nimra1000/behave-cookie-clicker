import time
from behave import *

@step("I am on the Landing page")
def step_impl(context):
    expected_title = "Cookie Clicker!"
    expected_url = context.base_url
    assert context.driver.current_url == expected_url, f"URL received '{context.driver.current_url}' does not match expected URL of '{expected_url}' "
    assert context.driver.title == expected_title, f"Title received '{context.driver.title}' does not match expected title of '{expected_title}' "

@step("I wait for {delay} seconds")
def step_impl(context, delay):
    time.sleep(int(delay))

@step("I type '{text}' into the '{locator}' input field")
def step_impl(context, text, locator):
    if locator == 'name':
        context.name = text
    context.base.type(locator, text)

@step("I click on the '{locator}' button")
def step_impl(context, locator):
    context.base.click_button(locator)

@step("I should see the relevant info")
def step_impl(context):
    for r in context.table:
        locator = r["category"]
        context.landing.confirm_key_value_pair_visible(locator)

@step("I should see the relevant buttons")
def step_impl(context):
    for r in context.table:
        locator = r["category"]
        context.base.confirm_button_exists(locator)

@step("I should see the relevant input fields")
def step_impl(context):
    for r in context.table:
        locator = r["category"]
        context.base.confirm_input_fields_exists(locator)

@step("I login as '{name}'")
def step_impl(context, name):
    context.execute_steps(
        f"""
        Given I am on the Landing page
        When I type '{name}' into the 'name' input field
        And I click on the 'Start!' button
        Then I should be redirected to the Game page
        """
    )
