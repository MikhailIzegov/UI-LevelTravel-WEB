import time

import pytest
from selene import browser, have, be, command, query
from test_data.data_for_tests import test_user
from utils.additional_actions import do
from selenium.webdriver.common.by import By


class CheckoutPage:

    def check_info(self):
        self.compare_hotel_name()
        self.compare_room_name()
        self.compare_room_price()
        self.compare_dates()
        self.compare_tourists_number()
        self.fill_card_fields()
        time.sleep(10)

    def compare_hotel_name(self):
        (browser.element('[class*=HotelCard__Title]')
         .element('a')
         .should(have.exact_text(do.get_data('hotel_name'))))

    def compare_room_name(self):
        browser.element('[class*=__RoomType-]').should(have.exact_text(do.get_data('room_name')))

    def compare_room_price(self):
        try:
            (browser.element('[class*=StyledCurrencyFormat]')
             .should(have.exact_text(do.get_data('room_price'))))
        except AssertionError as e:
            pytest.fail(f"Expected failure, but test continues. Reason: {str(e)}", pytrace=False)  # Флаг
            # pytrace=False убирает трассировку стека для данной ошибки, делая вывод более чистым

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
        (browser.element('[class*=StyledTouristData]')
         .should(have.exact_text(do.get_data('tourists_number'))))

    def fill_card_fields(self):
        do.scroll_to('.checkout-discount')

        browser.element('#pan').type('0' * 16)
        browser.element('#expDate').type('1233')
        browser.element('#cvv').type('0' * 3)

        browser.element('').should(have.attribute('data-at-package-submit-order-button', 'true'))
