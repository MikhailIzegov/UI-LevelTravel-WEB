from pages.application import app
from selene import browser


def test_smoke_hotel():
    app.main_page.open_page()
    app.main_page.log_in()
    app.main_page.choose_hotels()  # потом объединить с более высокоуровневым шагом теста
    app.main_page.set_number_of_tourists()

