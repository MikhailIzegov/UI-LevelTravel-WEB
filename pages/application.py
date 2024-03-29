# from tests.pages.registration_page import RegistrationPage
from pages.hotel_cards_page import HotelCardsPage
from pages.hotel_page import HotelPage
from pages.main_page import MainPage


class Application:
    def __init__(self):
        self.main_page = MainPage()
        self.hotel_cards_page = HotelCardsPage()
        self.hotel_page = HotelPage()


app = Application()
