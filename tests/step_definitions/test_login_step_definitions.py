from playwright.sync_api import expect
from pytest_bdd import step, parsers, scenarios

from tests.utils.data_utils import DataUtils
from ..conftest import Context

scenarios('../features/test_login.feature')


@step('the login page is launched')
def navigate_to_login_page(poms: Context):
    url = poms.env_data.load_config_data["test_login_page"]["pageURL"]
    poms.test_login_pom.navigate_to_login_page(url)


@step(parsers.parse('the user types "{username}" username into the username field'))
def user_types_in_username_explicitly(poms: Context, username):
    poms.test_login_pom.type_in_username(username)


@step('the user types in the correct username into the username field')
def user_enters_correct_username(poms: Context):
    username = poms.env_data.load_config_data["test_login_page"]["username"]
    poms.test_login_pom.type_in_username(username)


@step('the user types in the incorrect username into the username field')
def user_enters_incorrect_username(poms: Context):
    username = poms.env_data.load_config_data["test_login_page"]["incorrectUser"]
    poms.test_login_pom.type_in_username(username)


@step(parsers.parse('the user types "{password}" password into the password field'))
def user_types_in_password_explicitly(poms: Context, password):
    poms.test_login_pom.type_in_password(password)


@step('the user types in the correct password into the password field')
def user_enters_correct_password(poms: Context):
    password = poms.env_data.load_config_data["test_login_page"]["password"]
    poms.test_login_pom.type_in_password(DataUtils.decrypt_secret(password))


@step('the user types in the incorrect password into the password field')
def user_enters_incorrect_password(poms: Context):
    password = poms.env_data.load_config_data["test_login_page"]["incorrectPassword"]
    poms.test_login_pom.type_in_password(password)


@step('the user pushes submit button')
def user_pushes_submit_button(poms: Context):
    poms.test_login_pom.push_submit_button()


@step(parsers.parse('the new page url should contain "{text}" text'))
@step(parsers.parse('the page url should contain "{text}" text'))
def verify_page_url(poms: Context, text):
    assert text in poms.test_login_pom.page.url


@step(parsers.parse('the new page should contain "{text}" text'))
def check_if_page_contains_text(poms: Context, text):
    expect(poms.test_login_pom.get_congratulation_message()).to_contain_text(text)


@step(parsers.parse('the "{button_text}" button should be displayed on the new page'))
def check_if_page_contains_button(poms: Context, button_text):
    expect(poms.test_login_pom.get_log_out_button_element()).to_have_text(button_text)


@step('the error message should be displayed')
def check_error_message_is_displayed(poms: Context,):
    expect(poms.test_login_pom.get_error_message_element()).to_be_visible()


@step(parsers.parse('the error message text "{error_message}" should be displayed'))
def check_error_message_text(poms: Context, error_message):
    expect(poms.test_login_pom.get_error_message_element()).to_have_text(error_message)


@step(parsers.parse('the message "{message}" should be displayed'))
def check_message_displayed_on_page(poms: Context, message):
    if 'logged-in-successfully' in poms.test_login_pom.page.url:
        expect(poms.test_login_pom.get_congratulation_message()).to_contain_text(message)
    else:
        expect(poms.test_login_pom.get_error_message_element()).to_contain_text(message)
