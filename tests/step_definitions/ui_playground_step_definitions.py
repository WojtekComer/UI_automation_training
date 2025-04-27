from playwright.sync_api import expect
from pytest_bdd import scenarios, step, parsers

from ..page_objects.ui_playground.ui_playground_pom import UiPlaygroundPOM

scenarios('../features/ui_playground.feature')


class UiPlayground:
    alert_message = None


@step('the UI Playground page is launched')
def launch_ui_playground_page(page, load_config_data):
    pom = UiPlaygroundPOM(page)
    url = load_config_data['ui_playground']['pageURL']
    pom.navigate_to_ui_playground_page(url)
    expect(page).to_have_title('UI Test Automation Playground')
    expect(pom.get_main_page_title_element()).to_contain_text('UI Test Automation')


@step(parsers.parse('the user clicks "{link_text}" link to navigate to "{page_name}" page'))
def user_clicks_link_to_navigate_to_page(page, link_text, page_name):
    pom = UiPlaygroundPOM(page)
    pom.click_navigation_link(link_text)
    expect(page).to_have_title(page_name)
    expect(pom.get_test_page_header_element()).to_have_text(page_name)


@step(parsers.parse('the user clicks button with text "{button_text}"'))
def user_clicks_button_with_text(page, button_text):
    pom = UiPlaygroundPOM(page)
    pom.click_button_with_text(button_text, 4000)


@step('the user clicks the blue primary button')
def click_primary_class_button(page):
    pom = UiPlaygroundPOM(page)

    def dialog_handler(dialog):
        UiPlayground.alert_message = dialog.message
        assert dialog.message in 'Primary button pressed'
        dialog.accept()

    pom.page.on('dialog', dialog_handler)
    pom.click_class_based_primary_button()


@step(parsers.parse('the alert message should be "{alert_message}"'))
def check_alert_message(alert_message):
    assert alert_message in UiPlayground.alert_message


@step(parsers.parse('the user should be still on the "{page_name}" page'))
def user_still_on_the_page(page, page_name):
    expect(page).to_have_title(page_name)


@step(parsers.parse('the user waits for the button with ID "{button_id}" to be visible for "{time_seconds}" seconds'))
def wait_for_button_with_id_for_given_time(page, button_id, time_seconds):
    pom = UiPlaygroundPOM(page)
    pom.wait_for_state_of_element_with_id(button_id, int(time_seconds)*1000)


@step(parsers.parse('the button with ID "{button_id}" should not be visible'))
def button_with_id_not_visible(page, button_id):
    pom = UiPlaygroundPOM(page)
    expect(pom.get_element_with_id(button_id)).not_to_be_visible()
