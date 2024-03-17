# from tests.pages.registration_page import RegistrationPage
from pages.main_page import MainPage


class Application:
    def __init__(self):
        self.main_page = MainPage()


app = Application()
