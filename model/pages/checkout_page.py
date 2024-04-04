import pytest
from selene import browser, have
from test_data.data_for_tests import test_user
from utils.additional_actions import do


class CheckoutPage:

    def check_info(self):
        self.compare_hotel_name()
        self.compare_room_name()
        self.compare_room_price()
        self.compare_dates()
        self.compare_tourists_number()
        self.compare_user_data(test_user)
        self.fill_card_fields()

    def compare_user_data(self, user):
        (browser.element('#client_data_component')
            .all('[class*=ClientDataItem]')
            .should(
                have.exact_texts(
                    f'{user.first_name_ru} {user.last_name_ru}',
                    user.phone_number,
                    user.email
                )
        ))

        (browser.element('[class*=TouristForm]')
            .all('input')
            .should(
                have.values(
                    user.last_name_en,
                    user.first_name_en
                )
        ))

    def compare_hotel_name(self):
        (browser.element('[class*=HotelCard__Title]').with_(timeout=12)
         .element('a')
         .should(have.exact_text(do.get_data('hotel_name'))))

    def compare_room_name(self):
        browser.element('[class*=__RoomType-]').should(have.exact_text(do.get_data('room_name')))

    @pytest.mark.xfail(reason='It might be a bug, see: *there should be a link to bug-report*')
    def compare_room_price(self):
        (browser.element('[class*=StyledCurrencyFormat]').with_(timeout=15)
         .should(have.exact_text(do.get_data('room_price'))))

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
         .should(have.text(do.get_data('tourists_number'))))

    def fill_card_fields(self):
        do.scroll_to('.checkout-discount')

        browser.element('#pan').type('0' * 16)
        browser.element('#expDate').type('1233')
        browser.element('#cvv').type('0' * 3)

        (browser.element('[class*=PaymentMethod__StyledBottom]')
         .element('button').with_(timeout=12)
         .should(have.attribute('data-at-package-submit-order-button').value('true')))
