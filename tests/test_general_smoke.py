import allure
from allure_commons.types import Severity

from model.application import app


@allure.label('owner', 'ms_izegov')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.feature('Отели. Смоук-тест')
@allure.story('Обычный юзер может забронировать номер в отеле')
@allure.link('https://example.com', name='see the task here')
def test_smoke_hotel():

    with allure.step('Открытие главное страницы'):
        app.main_page.open_page()

    with allure.step('Авторизация'):
        app.main_page.log_in()

    with allure.step('Выбор направления, кол-ва человек, дат'):
        app.main_page.find_available_hotels()

    with allure.step('Установка фильтров, выбор отеля'):
        app.hcp.choose_hotel()

    with allure.step('Выбор номера в отеле'):
        app.hotel_page.choose_room()

    with allure.step('Проверка данных на чекауте'):
        app.checkout_page.check_info()
