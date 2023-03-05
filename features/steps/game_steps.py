from behave import *

@step("I should be greeted")
def step_impl(context):
    greeting_label = f"Hello {context.name}"
    context.landing.confirm_label_text_visible(greeting_label)

@step('I should be redirected to the Game page')
def step_impl(context):
    #TODO: extend below contatenation to allow names with spaces eg: Nimra Ajmal
    expected_url = f"{context.base_url}game/{context.name}"
    context.base.confirm_redirection(expected_url)

@step('I should have {expected_quantity} {locator}')
def step_impl(context, expected_quantity, locator):
    context.game.check_quantity(int(expected_quantity), locator)

@step('I have {desired_quantity} cookies')
def step_impl(context, desired_quantity):
    context.game.set_cookie_quantity(int(desired_quantity))
