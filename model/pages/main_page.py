from selene import browser, have, query

from model.components.authorization import auth
from test_data.data_for_tests import test_user
from utils.additional_actions import do


class MainPage:
    def open_page(self):
        browser.open('https://level.travel')
        browser.driver.maximize_window()
        do.remove_cookies_banner()

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

    def save_date_and_tourists_number(self):
        self.get_tourists_number()
        self.get_start_date()
        self.get_end_date()

    def find_available_hotels(self):
        self.set_number_of_tourists()
        self.choose_hotels_section()
        self.choose_destination(test_user.destination)
        self.set_start_date(test_user.start_date)
        self.set_end_date(test_user.end_date)
        self.save_date_and_tourists_number()
        self.click_find_btn()

    def choose_hotels_section(self):
        browser.element('[value=hotel]').element('[type=button]').click()

    def unfold_tourists(self):
        browser.element('[data-testid*=tourists-picker]').click()

    def decrease_tourists_number(self):
        browser.element('[class*=CounterPluralize]').all('button').first.click()

    def increase_tourists_number(self):
        browser.element('[class*=CounterPluralize]').all('button').second.click()

    def choose_destination(self, destination):
        browser.element('[class=lt-destination-picker__input]').click()

        (browser.element('.lt-destination-picker__option[id*=option-3-0]').
         element('[class*=styles__LabelText]').should(have.text(destination)).click())

    def set_start_date(self, start_date):
        browser.element('#start').click()
        browser.element(f'[class*=datepicker__day--{start_date}][aria-disabled=false]').click()

        browser.element('#start').element('[class*=DurationTrip]').should(have.text(start_date.replace('0', '')))

    def set_end_date(self, end_date):
        browser.element('#end').click()
        browser.element(f'[class*=datepicker__day--{end_date}][aria-disabled=false]').click()

        browser.element('#end').element('[class*=DurationTrip]').should(have.text(end_date.replace('0', '')))

    def get_tourists_number(self):
        tourists_number = browser.element('[class*=TouristsPickerdesktop__StyledLabel]').get(query.text)
        do.set_data('tourists_number', tourists_number)

    def get_start_date(self):
        start_date = browser.element('#start').element('[class*=DurationTripField__Value]').get(query.text)
        do.set_data('start_date', start_date)

    def get_end_date(self):
        end_date = browser.element('#end').element('[class*=DurationTripField__Value]').get(query.text)
        do.set_data('end_date', end_date)

    def click_find_btn(self):
        browser.element('[type="submit"]').click()
