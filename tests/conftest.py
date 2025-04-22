import json
import os

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture()
def load_config_data():
    path = os.path.dirname(__file__)
    with open(f'{path}/page_objects/config/config_data.json', "rb") as data:
        data_dictionary = json.loads(data.read())
    return data_dictionary



