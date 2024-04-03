from model.pages.checkout_page import CheckoutPage
from model.pages.hotel_cards_page import HotelCardsPage
from model.pages.hotel_page import HotelPage
from model.pages.main_page import MainPage


class Application:
    def __init__(self):
        self.main_page = MainPage()
        self.hcp = HotelCardsPage()
        self.hotel_page = HotelPage()
        self.checkout_page = CheckoutPage()


app = Application()
