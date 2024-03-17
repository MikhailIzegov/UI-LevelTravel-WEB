import time

from selene import browser, have, be, command

from components.authorization import auth
from test_data.data_for_tests import DataForTests


class MainPage:
    def open_page(self):
        browser.open('https://level.travel')
        browser.driver.maximize_window()

    def log_in(self):
        data = DataForTests()

        self.open_auth_model_window()
        auth.via_email_option()
        auth.fill_email(data.login)
        auth.fill_password(data.password)
        auth.is_logged_in()

    def set_number_of_tourists(self):
        self.unfold_tourists()
        self.decrease_tourists_number()
        time.sleep(5)

    def open_auth_model_window(self):
        (browser.all('[class*=HeaderMenuCategory__CategoryName]').element_by
         (have.exact_text('Вход')).click())

    def choose_hotels(self):
        browser.element('[value=hotel]').element('[type=button]').click()

    def unfold_tourists(self):
        browser.element('[data-testid*=tourists-picker]').click()

    def decrease_tourists_number(self):
        browser.element('[class*=CounterPluralize] > [type=button]:first-of-type').click()

    def increase_tourists_number(self):
        browser.element('[class*=CounterPluralize] > [type=button]:nth-of-type(2)').click()


    def choose_destination(self, destination):
        browser.element('[class=lt-destination-picker__input]').type(destination)

    def click_find_btn(self):
        browser.element('[type="submit"]').click()





