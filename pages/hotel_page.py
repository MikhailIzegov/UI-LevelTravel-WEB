import time

from selene import browser, have, be, command, query
from test_data.data_for_tests import test_user
from utils.additional_actions import do
from selenium.webdriver.common.by import By


class HotelPage:

    def choose_room(self):
        self.close_modal_window()
        self.compare_hotel_name()
        self.compare_hotel_price()

    def close_modal_window(self):
        if browser.element("#fl-772983").wait_until(be.visible):
            browser.driver.switch_to.frame(browser.driver.find_element(By.CSS_SELECTOR, "#fl-772983"))  # либо через
            # селеновский locate()
            browser.element('[class=pc] .close[type=button]').click()
            browser.switch_to.default_content()
        else:
            pass

        if browser.element('[data-testid=cookies-banner]').wait_until(be.visible):
            browser.element('[data-testid=cookies-banner]').perform(command.js.remove)

    def compare_hotel_name(self):
        browser.element('[class*=TitleBold]').should(have.exact_text(do.get_data('hotel_name')))

    def compare_hotel_price(self):
        (browser.element('.hotel-price-badge').element('[type=button] span').should
         (have.exact_text(do.get_data('hotel_price'))))
