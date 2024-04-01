# from tests.pages.registration_page import RegistrationPage
from pages.hotel_cards_page import HotelCardsPage
from pages.hotel_page import HotelPage
from pages.main_page import MainPage


class Application:
    def __init__(self):
        self.shared_data = {}  # Словарь для хранения общих данных между страницами
        self.main_page = MainPage()
        self.hcp = HotelCardsPage()
        self.hotel_page = HotelPage()

    def set_data(self, key, value):
        self.shared_data[key] = value

    def get_data(self, key):
        return self.shared_data.get(key)


app = Application()
