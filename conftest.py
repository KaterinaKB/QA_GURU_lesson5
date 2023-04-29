import pytest
from selene import browser


@pytest.fixture
def init_browser(scope="function"):
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.close()