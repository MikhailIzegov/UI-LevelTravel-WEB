import time

from selene import browser, have, be, command, query
from test_data.data_for_tests import test_user
from utils.additional_actions import do


class HotelPage:

    def choose_room(self):
        self.compare_hotel_name()
        self.compare_hotel_price()

    def compare_hotel_name(self):
        browser.element('[class*=TitleBold]').should(have.exact_text(do.get_data('hotel_name')))

    def compare_hotel_price(self):
        (browser.all('.hotel-price-badge').element('[type=button] span').should
         (have.exact_text(do.get_data('hotel_price'))))
