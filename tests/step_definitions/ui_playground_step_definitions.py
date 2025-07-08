import time

from playwright.sync_api import expect
from pytest_bdd import scenarios, step, parsers

from ..conftest import Context

scenarios('../features/ui_playground.feature')


@step('the UI Playground page is launched')
def launch_ui_playground_page(poms: Context):
    url = poms.env_data.load_config_data['ui_playground']['pageURL']
    poms.ui_playground_pom.navigate_to_ui_playground_page(url)
    expect(poms.ui_playground_pom.page).to_have_title('UI Test Automation Playground')
    expect(poms.ui_playground_pom.get_main_page_title_element()).to_contain_text('UI Test Automation')


@step(parsers.parse('the user clicks "{link_text}" link to navigate to "{page_name}" page'))
def user_clicks_link_to_navigate_to_page(poms: Context, link_text, page_name):
    poms.ui_playground_pom.click_navigation_link(link_text)
    expect(poms.ui_playground_pom.page).to_have_title(page_name)
    expect(poms.ui_playground_pom.get_test_page_header_element()).to_have_text(page_name)


@step(parsers.parse('the user clicks button with text "{button_text}"'))
def user_clicks_button_with_text(poms: Context, button_text):
    def dialog_handler(dialog):
        dialog_message = str(dialog.message)
        if "\n" in dialog_message:
            dialog_message = dialog_message.replace('\n', " ")
        poms.env_data.alert_dialog.alert_message = dialog_message
        dialog.accept()

    poms.ui_playground_pom.page.on('dialog', dialog_handler)
    poms.ui_playground_pom.click_button_with_text(button_text, 4000)


@step(parsers.parse(
    'the user clicks button with text "{button_text}" and "{action}" the "{confirm_message}" confirm type dialog message'))
def accept_or_dismiss_confirm_dialog_message(poms: Context, button_text, action, confirm_message):
    def dialog_handler(dialog):
        confirm_dialog_message = str(dialog.message)
        if dialog.type in 'confirm':
            if "\n" in confirm_dialog_message:
                confirm_dialog_message = confirm_dialog_message.replace('\n', " ")
            assert confirm_dialog_message in confirm_message
            if action in 'accepts':
                dialog.accept()
            elif action in 'dismisses':
                dialog.dismiss()
            else:
                raise ValueError(f'"{action}" action is not defined. Use either "accepts" or "dismisses" action!')

        retry = poms.env_data.load_timeouts['MIN_RETRY_ATTEMPTS']
        while retry:
            if dialog.type in 'alert':
                break
            retry -= 1
            time.sleep(poms.env_data.load_timeouts['MIN_HARD_SLEEP'])
        assert retry > 0, f'"Alert" type dialog was not generated after accepting "Confirm" type dialog'

        if dialog.type in 'alert':
            poms.env_data.alert_dialog.alert_message = dialog.message
            dialog.accept()

    poms.ui_playground_pom.page.on('dialog', dialog_handler)
    poms.ui_playground_pom.click_button_with_text(button_text, 4000)


@step(parsers.parse(
    'the user clicks button with text "{button_text}" enters "{user_value}" value and "{action}" prompt type dialog message'))
def enter_value_and_accept_or_dismiss_prompt_dialog_message(poms: Context, button_text, user_value, action):
    def dialog_handler(dialog):
        if dialog.type in 'prompt':
            assert 'Enter your value:' in dialog.message
            if action in 'accepts':
                dialog.accept(user_value)
            elif action in 'dismisses':
                dialog.dismiss(user_value)
            else:
                raise ValueError(f'"{action}" action is not defined. Use either "accepts" or "dismisses" action!')

        retry = poms.env_data.load_timeouts['MIN_RETRY_ATTEMPTS']
        while retry:
            if dialog.type in 'alert':
                break
            retry -= 1
            time.sleep(poms.env_data.load_timeouts['MIN_HARD_SLEEP'])
        assert retry > 0, f'"Alert" type dialog was not generated after accepting "Prompt" type dialog'

        if dialog.type in 'alert':
            poms.env_data.alert_dialog.alert_message = dialog.message
            dialog.accept()

    poms.ui_playground_pom.page.on('dialog', dialog_handler)
    poms.ui_playground_pom.click_button_with_text(button_text, 4000)


@step('the user clicks the blue primary button')
def click_primary_class_button(poms: Context):
    def dialog_handler(dialog):
        poms.env_data.alert_dialog.alert_message = dialog.message
        dialog.accept()

    poms.ui_playground_pom.page.on('dialog', dialog_handler)
    poms.ui_playground_pom.click_class_based_primary_button()


@step(parsers.parse('the alert message should be "{alert_message}"'))
def check_alert_message(poms: Context, alert_message):
    assert alert_message in poms.env_data.alert_dialog.alert_message


@step(parsers.parse('the user should be still on the "{page_name}" page'))
def user_still_on_the_page(poms: Context, page_name):
    expect(poms.ui_playground_pom.page).to_have_title(page_name)


@step(parsers.parse('the user waits for the button with ID "{button_id}" to be visible for "{time_seconds}" seconds'))
def wait_for_button_with_id_for_given_time(poms: Context, button_id, time_seconds):
    poms.ui_playground_pom.wait_for_state_of_element_with_id(button_id, int(time_seconds) * 1000)


@step(parsers.parse('the button with ID "{button_id}" should not be visible'))
def button_with_id_not_visible(poms: Context, button_id):
    expect(poms.ui_playground_pom.get_element_with_id(button_id)).not_to_be_visible()
