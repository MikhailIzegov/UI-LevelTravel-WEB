from pages.application import app
from selene import browser


def test_smoke_hotel():
    app.main_page.open_page()
    app.main_page.log_in()
    app.main_page.find_available_hotels()  # добавить выбор дат


