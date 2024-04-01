import time

from selene import browser, have, be, command, query
from test_data.data_for_tests import test_user
from utils.additional_actions import do
from selenium.webdriver.common.by import By


class CheckoutPage:

    def compare_hotel_name(self):
        (browser.element('[class*=HotelCard__Title]')
         .element('a')
         .should(have.exact_text(do.get_data('hotel_name'))))

    def compare_room_name(self):
        pass
    def compare_room_price(self):
        (browser.element('[class*=StyledCurrencyFormat]')
         .should(have.exact_text(do.get_data('hotel_price'))))
    def compare_dates(self):
        parts_start_date = do.get_data('start_date').split()
        formatted_start_date = f"{parts_start_date[0]} {parts_start_date[1][:3]}"

        (browser.all('[class*=StyledDateText]')
         .first
         .should(have.text(formatted_start_date)))

        parts_end_date = do.get_data('end_date').split()
        formatted_end_date = f"{parts_end_date[0]} {parts_end_date[1][:3]}"

        (browser.all('[class*=StyledDateText]')
         .second
         .should(have.text(formatted_end_date)))
    def compare_tourists_number(self):
        pass

    def fill_card_fields(self):
        pass

