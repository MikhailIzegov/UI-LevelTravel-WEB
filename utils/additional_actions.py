import re

from selene import browser, command, query, be
from selenium.webdriver.common.by import By


class AdditionalActions:

    def __init__(self):
        self.shared_data = {}  # Словарь для хранения общих данных между страницами

    def set_data(self, key, value):
        self.shared_data[key] = value

    def get_data(self, key):
        return self.shared_data.get(key)

    def scroll_to(self, locator, timeout=20):
        browser.element(locator).with_(timeout=timeout).perform(command.js.scroll_into_view)

    def leave_only_digits(self, text_value):
        return int(''.join(re.findall(r'\d', text_value)))

    def extract_number_of_hotels(self, text):
        first_space_index = text.find(' ')
        number = text[:first_space_index]
        return number

    def extract_text(self, locator):
        return locator.get(query.text)

    def remove_cookies_banner(self):
        if browser.element('[data-testid=cookies-banner]').wait_until(be.visible):
            browser.element('[data-testid=cookies-banner]').perform(command.js.remove)

    def close_modal_window(self, locator):
        if browser.element(locator).wait_until(be.visible):
            browser.driver.switch_to.frame(browser.driver.find_element(By.CSS_SELECTOR, locator))  # либо через
            # селеновский locate()
            browser.element('[class=pc] .close[type=button]').click()
            browser.switch_to.default_content()
        else:
            pass


do = AdditionalActions()
