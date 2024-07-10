from behave import given, when, then


@given('Open the game page')
def open_game_page(context):
    context.app.base_page.open('http://sdetchallenge.fetch.com/')


@when('Placing 3 bars on each bowl and perform first weighing')
def perform_first_weighing(context):
    context.app.game_page.perform_first_weighing()


@when('Click Reset')
def click_reset(context):
    context.app.game_page.click_reset()


@when('Perform second weighing and finding fake bar')
def perform_second_weighing(context):
    context.app.game_page.perform_second_weighing()


@when('Click the button to indicate the fake bar')
def click_fake_bar(context):
    context.app.game_page.click_fake_bar()


@when('Get the alert message')
def get_alert_message(context):
    context.app.game_page.get_alert_message()


@then('Verify Fake bar was found and {message} displayed')
def verify_fake_bar(context, message):
    context.app.game_page.verify_fake_bar(message)