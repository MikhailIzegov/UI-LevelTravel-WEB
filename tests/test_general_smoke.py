import time

from pages.application import app
from selene import browser

from utils.additional_actions import do


def test_smoke_hotel():
    app.main_page.open_page()
    app.main_page.log_in()
    app.main_page.find_available_hotels()
    app.hcp.choose_hotel()
    app.hotel_page.choose_room()


