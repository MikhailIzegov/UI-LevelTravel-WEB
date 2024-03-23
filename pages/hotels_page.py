import time

from selene import browser, have, be, command
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
        self.set_rating()
        self.set_distance_to_the_sea()
        self.set_budget()
        self.set_beach_type()
        self.hotel_type()
        self.set_facilities()

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
         with_(timeout=8).click())
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

    def set_rating(self):
        pass



    def open_hotel_card(self):
        browser.element('').click()