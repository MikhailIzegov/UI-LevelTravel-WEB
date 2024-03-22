# from tests.pages.registration_page import RegistrationPage
from pages.hotels_page import HotelsPage
from pages.main_page import MainPage


class Application:
    def __init__(self):
        self.main_page = MainPage()
        self.hotels_page = HotelsPage()


app = Application()
