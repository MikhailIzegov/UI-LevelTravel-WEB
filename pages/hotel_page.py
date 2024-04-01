import time

from selene import browser, have, be, command, query

from test_data.data_for_tests import test_user
from utils.additional_actions import do


class HotelPage:

    def get_hotel_name(self):
        pass

    def get_price_from(self):
        browser.element('[class*=TitleBold]').should(have.exact_text(''))


    # НЕ ЗАБЫТЬ ПЕРЕКЛЮЧИТЬСЯ НА ДРУГУЮ ВКЛАДКУ!