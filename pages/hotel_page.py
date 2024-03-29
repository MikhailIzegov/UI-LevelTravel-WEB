import time

from selene import browser, have, be, command, query

from pages import hotel_cards_page as hcp
from test_data.data_for_tests import test_user
from utils.additional_actions import do


class HotelPage:
    def get_price_from(self):
        # browser.element('[class*=TitleBold]').should(have.exact_text(hcp.get_name_of_first_hotel_card))

    def get_hotel_name(self):
        pass


    # НЕ ЗАБЫТЬ ПЕРЕКЛЮЧИТЬСЯ НА ДРУГУЮ ВКЛАДКУ!