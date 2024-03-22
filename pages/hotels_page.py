import time

from selene import browser, have, be, command
from selenium.webdriver.common.by import By

from test_data.data_for_tests import test_user


class HotelsPage:
    def choose_hotel(self):
        self.set_filters()
        self.open_hotel_card()

    def set_filters(self):
        self.close_login_modal_window()
        self.set_stars(test_user.stars)
        self.set_rating()
        self.set_distance_to_the_sea()
        self.set_budget()
        self.set_beach_type()
        self.hotel_type()
        self.set_facilities()


    def close_login_modal_window(self):
        # browser.switch_to.frame(browser.element("#fl-716178"))
        # Используем find_elements и проверяем, что список найденных элементов не пуст
        if browser.driver.find_elements(By.CSS_SELECTOR, "#fl-716178"):
            browser.driver.switch_to.frame(browser.driver.find_element(By.CSS_SELECTOR, "#fl-716178"))
            browser.element('.close[type=button]').click()
            browser.switch_to.default_content()
        else:
            pass

    def set_stars(self, stars):
        browser.element(f'#\\3{stars}[type=checkbox]').perform(command.js.scroll_into_view)
        browser.element(f'#\\3{stars}[type=checkbox]').click()
        time.sleep(5)



    def open_hotel_card(self):
        browser.element('').click()