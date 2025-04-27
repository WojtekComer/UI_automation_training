import json
import os

import pytest
from playwright.sync_api import Page

from .page_objects.test_login_page.test_login_pom import TestLoginPOM
from .page_objects.ui_playground.ui_playground_pom import UiPlaygroundPOM


class Context:
    def __init__(self, page: Page, env_data):
        self.env_data = env_data
        self.test_login_pom = TestLoginPOM(page)
        self.ui_playground_pom = UiPlaygroundPOM(page)


class EnvironmentData:
    def __init__(self):
        self.alert_dialog = self.AlertDialog()

    class AlertDialog:
        def __init__(self):
            self.alert_message = None

    @property
    def load_config_data(self):
        path = os.path.dirname(__file__)
        with open(f'{path}/page_objects/config/config_data.json', "rb") as data:
            data_dictionary = json.loads(data.read())
        return data_dictionary


@pytest.fixture()
def poms(page):
    env_data = EnvironmentData()
    context = Context(page, env_data)
    yield context


@pytest.fixture()
def browser_context_args(browser_context_args, tmpdir_factory: pytest.TempdirFactory):
    return {
        **browser_context_args,
        "record_video_dir": tmpdir_factory.mktemp('videos'),
        "ignore_https_errors": True
    }
