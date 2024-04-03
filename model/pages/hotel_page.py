import time

from selene import browser, have, be, command, query
from test_data.data_for_tests import test_user
from utils.additional_actions import do
from selenium.webdriver.common.by import By


class HotelPage:

    def choose_room(self):
        self.close_big_modal_window()
        self.compare_hotel_name()
        self.compare_hotel_price_from()
        self.close_small_modal_window()
        self.compare_date_and_tourists_number()
        self.save_room_price()
        self.save_room_name()
        self.pick_room()
        browser.switch_to_next_tab()

    def close_big_modal_window(self):
        if browser.element("#fl-772983").wait_until(be.visible):
            browser.driver.switch_to.frame(browser.driver.find_element(By.CSS_SELECTOR, "#fl-772983"))  # либо через
            # селеновский locate()
            browser.element('[class=pc] .close[type=button]').click()
            browser.switch_to.default_content()
        else:
            pass

        do.remove_cookies_banner()

    def close_small_modal_window(self):
        if browser.element("#fl-707112").wait_until(be.visible):
            browser.driver.switch_to.frame(browser.driver.find_element(By.CSS_SELECTOR, "#fl-707112"))  # либо через
            # селеновский locate()
            browser.element('[class=pc] .close[type=button]').click()
            browser.switch_to.default_content()
        else:
            pass

        do.remove_cookies_banner()

    def compare_hotel_name(self):
        browser.element('[class*=TitleBold]').should(have.exact_text(do.get_data('hotel_name')))

    def compare_hotel_price_from(self):
        (browser.element('.hotel-price-badge').element('[type=button] span').should
         (have.exact_text(do.get_data('hotel_price'))))

    def compare_date_and_tourists_number(self):
        do.scroll_to('#lt-hotel-searcher')
        (browser.element('[data-testid*=tourists-picker]').element('span')
         .should(have.exact_text(do.get_data('tourists_number'))))

        (browser.element('#start').element('[class*=DurationTripField__Value]')
         .should(have.exact_text(do.get_data('start_date'))))

        (browser.element('#end').element('[class*=DurationTripField__Value]')
         .should(have.exact_text(do.get_data('end_date'))))

    def save_room_price(self):
        room_price = (browser.all('[class*=HotelRatesResults__StyledItemWrapper]').
                      second.
                      all('[class*=HotelOffers]').
                      first.element('[class*=HotelOfferPrice__StyledPrice]').get(query.text))
        do.set_data('room_price', room_price)

    def save_room_name(self):
        room_name = (browser.all('[class*=HotelRatesResults__StyledItemWrapper]')
                     .second
                     .element('[class*=HotelRoomName]').get(query.text))
        do.set_data('room_name', room_name)

    def pick_room(self):
        (browser.all('[class*=HotelRatesResults__StyledItemWrapper]')
         .second.all('[class*=HotelOffers]').first.element('[type=button]').click())
