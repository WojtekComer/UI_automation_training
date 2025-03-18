from playwright.sync_api import expect
from pytest_bdd import step, parsers, scenarios

from tests.page_objects.test_login_page.test_login_pom import TestLoginPOM

scenarios('../features/test_login.feature')


@step('the login page is launched')
def navigate_to_login_page(page, load_config_data):
    pom = TestLoginPOM(page)
    url = load_config_data["test_login_page"]["pageURL"]
    pom.navigate_to_login_page(url)


@step('the user types in the correct username into the username field')
def user_enters_username(page, load_config_data):
    pom = TestLoginPOM(page)
    username = load_config_data["test_login_page"]["username"]
    pom.type_in_username(username)


@step('the user types in the incorrect username into the username field')
def user_enters_username(page, load_config_data):
    pom = TestLoginPOM(page)
    username = load_config_data["test_login_page"]["incorrectUser"]
    pom.type_in_username(username)


@step('the user types in the correct password into the password field')
def user_enters_password(page, load_config_data):
    pom = TestLoginPOM(page)
    password = load_config_data["test_login_page"]["password"]
    pom.type_in_password(password)


@step('the user types in the incorrect password into the password field')
def user_enters_password(page, load_config_data):
    pom = TestLoginPOM(page)
    password = load_config_data["test_login_page"]["incorrectPassword"]
    pom.type_in_password(password)


@step('the user pushes submit button')
def user_pushes_submit_button(page):
    pom = TestLoginPOM(page)
    pom.push_submit_button()


@step(parsers.parse('the new page url should contain "{text}" text'))
def verify_page_url(page, text):
    assert text in page.url


@step(parsers.parse('the new page should contain "{text}" text'))
def check_if_page_contains_text(page, text):
    pom = TestLoginPOM(page)
    expect(pom.get_congratulation_message()).to_contain_text(text)


@step(parsers.parse('the "{button_text}" button should be displayed on the new page'))
def check_if_page_contains_button(page, button_text):
    pom = TestLoginPOM(page)
    expect(pom.get_log_out_button_element()).to_have_text(button_text)


@step('the error message should be displayed')
def check_error_message_is_displayed(page):
    pom = TestLoginPOM(page)
    expect(pom.get_error_message_element()).to_be_visible()


@step(parsers.parse('the error message text "{error_message}" should be displayed'))
def check_error_message_text(page, error_message):
    pom = TestLoginPOM(page)
    expect(pom.get_error_message_element()).to_have_text(error_message)
