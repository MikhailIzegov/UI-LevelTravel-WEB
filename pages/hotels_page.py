import time

from selene import browser, have, be, command
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from test_data.data_for_tests import test_user
from utils.additional_actions import do


class HotelsPage:
    def choose_hotel(self):
        self.set_filters()
        self.open_hotel_card()

    def set_filters(self):
        self.close_login_modal_window()
        self.set_confirmability()
        self.set_stars(test_user.stars)
        self.set_rating(test_user.rating)
        self.set_regions(test_user.regions)
        self.set_budget()
        self.set_wifi_type()
        self.open_hotel_card()

    def close_login_modal_window(self):
        # browser.switch_to.frame(browser.element("#fl-716178"))
        # Используем find_elements и проверяем, что список найденных элементов не пуст
        # if browser.driver.find_element(By.CSS_SELECTOR, "#fl-716178"):

        if browser.element("#fl-716178").should(be.visible):
            browser.driver.switch_to.frame(browser.driver.find_element(By.CSS_SELECTOR, "#fl-716178"))
            browser.element('.close[type=button]').click()
            browser.switch_to.default_content()
        else:
            pass


        # if browser.element("#fl-716178").with_(timeout=10):
        #     browser.driver.switch_to.frame(browser.driver.find_element(By.CSS_SELECTOR, "#fl-716178"))
        #     browser.element('.close[type=button]').click()
        #     browser.switch_to.default_content()
        # else:
        #     pass


    def set_confirmability(self):
        (browser.element('#filter-confirmability').element(f'#\\31[class*=MultiToggleSwitch]').
         with_(timeout=12).click())
        all_given_hotels = browser.all('[class*=HotelCard__StyledHotelOfferCardContent]')
        hotels_with_instant_confirmation = (
            all_given_hotels.all('[class*=HotelCard__StyledHotelOfferCardContent] [class*=InstantConfirmIcon]'))
        all_given_hotels.should(have.size(len(hotels_with_instant_confirmation)))


    def set_stars(self, stars):
        # browser.element(f'#\\3{stars}[type=checkbox]').perform(command.js.scroll_into_view)
        do.scroll_to('[class*=FilterCancellationPolicy__StyledLabelIcon]')
        browser.element(f'#\\3{stars}[type=checkbox]').click()

        # Находим все карточки отелей
        all_given_hotels = browser.all('[class*=HotelCard__StyledHotelOfferCardContent] [itemprop=ratingValue]')

        # Проверяем, что у всех найденных отелей есть искомое кол-во звезд,
        # чтобы впоследствии получить кол-во таких отелей
        options_with_attribute = all_given_hotels.filtered_by(have.attribute('content', stars))

        # Сравниваем
        all_given_hotels.should(have.size(len(options_with_attribute)))

    def set_rating(self, rating):
        do.scroll_to('.filter-meals')
        browser.all('[class*=SwitcherItem]').element_by(have.exact_text(rating + '+')).click()
        all_given_hotels = browser.all('[class*=HotelCard__StyledHotelOfferCardContent]')
        all_given_ratings = browser.all('[class*=HotelRating]').should(have.texts('Дубай' or 'Турция'))
        print(all_given_ratings)
        all_given_hotels.should(have.size(len(all_given_ratings)))

        # Проверка, что рейтинг каждого отеля >= указанного рейтинга
        for hotel_rating in all_given_ratings:
            # Получаем value у элемента и преобразуем в float, чтобы проверить
            value = float(hotel_rating.get_attribute('value'))
            print(value)
            assert value >= float(rating), f'Рейтинг отеля {value} меньше указанного: {rating}'

    def set_regions(self, regions):
        do.scroll_to('[class*=FilterLine__FilterDiv]')
        browser.element('[type=checkbox]#\\31 09028').click()
        browser.element('[type=checkbox]#\\31 09030').click()
        # all_given_regions = (browser.all('[class*=HotelCard__StyledHotelOfferCardContent]').
        #                      all('[itemprop=addressRegion]'))
        all_given_regions = '[class*=HotelCard__StyledHotelOfferCardContent] [itemprop=addressRegion]'

        self.check_element_with_text_from_list(all_given_regions, regions)

    def check_element_with_text_from_list(self, locator: str, texts: list):
        for text in texts:
            try:
                browser.all(locator).should(have.text(text))
                print(f"Элемент с текстом '{text}' найден и виден.")
                return  # Если элемент найден, завершаем функцию
            except TimeoutException:
                continue  # Если элемент не найден, пробуем следующий текст
        # Если ни один элемент не найден, выбрасываем исключение
        raise AssertionError(f"Ни один из элементов с текстами {texts} не найден.")





        # for region in all_given_regions:
        #     text_value_of_region = region.text
        #     if not any(valid_location in text_value_of_region for valid_location in regions):
        #         raise AssertionError(f"Найденный текст '{text_value_of_region}' не соответствует выбранному фильтру")



    def open_hotel_card(self):
        browser.element('').click()


