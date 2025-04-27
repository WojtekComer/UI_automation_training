from playwright.sync_api import Page

from .selectors import Selectors


class UiPlaygroundPOM:
    def __init__(self, page: Page):
        self.page = page
        self.selectors = Selectors

    def navigate_to_ui_playground_page(self, url):
        self.page.goto(url)

    def get_main_page_title_element(self):
        return self.page.locator(self.selectors.MAIN_PAGE_TITLE)

    def click_navigation_link(self, link_text):
        self.page.locator(self.selectors.TEST_PAGE_LINK.format(link_name=link_text)).click()

    def get_test_page_header_element(self):
        return self.page.locator(self.selectors.TEST_PAGE_HEADER_ELEMENT)

    def click_button_with_text(self, button_text, timeout=30000):
        self.page.locator(self.selectors.BUTTON_WITH_TEXT.format(button_text=button_text)).click(timeout=timeout)

    def wait_for_state_of_element_with_id(self, element_id, timeout, state='visible'):
        try:
            self.page.locator(self.selectors.ID_BASED_ELEMENT_SELECTOR.format(element_id=element_id)).wait_for(
                timeout=timeout, state=state)
            return True
        except:
            return False

    def get_element_with_id(self, element_id):
        return self.page.locator(self.selectors.ID_BASED_ELEMENT_SELECTOR.format(element_id=element_id))

    def click_class_based_primary_button(self):
        self.page.locator(self.selectors.CLASS_BASED_PRIMARY_BUTTON_SELECTOR).click()
