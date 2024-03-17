import time

from selene import browser, have, be, command

from components.authorization import auth
from test_data.data_for_tests import test_user


class MainPage:
    def open_page(self):
        browser.open('https://level.travel')
        browser.driver.maximize_window()

    def open_auth_model_window(self):
        (browser.all('[class*=HeaderMenuCategory__CategoryName]').element_by
         (have.exact_text('Вход')).click())

    def log_in(self):
        self.open_auth_model_window()
        auth.via_email_option()
        auth.fill_email(test_user.email)
        auth.fill_password(test_user.password)
        auth.is_logged_in()

    def set_number_of_tourists(self):
        self.unfold_tourists()
        self.decrease_tourists_number()

    def find_hotels(self):
        self.choose_hotels_section()
        self.set_number_of_tourists()
        self.choose_destination(test_user.destination)
        self.click_find_btn()


    def choose_hotels_section(self):
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





