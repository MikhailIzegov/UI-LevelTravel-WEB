import pytest
from selene import browser

from utils import attach


@pytest.fixture(scope="function", autouse=True)
def teardown():

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
