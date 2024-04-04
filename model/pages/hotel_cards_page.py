import allure
from selene import browser, have, be, query

from test_data.data_for_tests import test_user
from utils.additional_actions import do


class HotelCardsPage:

    def __init__(self):
        self.all_hotel_cards = browser.all('[class*=HotelCard__StyledHotelOfferCardContent]')

    def choose_hotel(self):
        self.set_filters()
        self.save_hotel_name_and_price()
        self.open_hotel_card()

        browser.switch_to_next_tab()

    def set_filters(self):
        do.close_modal_window('#fl-716178')
        do.remove_cookies_banner()

        with allure.step('Мгновенное подтверждение'):
            self.set_confirmability()

        with allure.step('Кол-во звезд'):
            self.set_stars(test_user.stars)

        with allure.step('Рейтинг отеля'):
            self.set_rating(test_user.rating)

        with allure.step('Бюджет'):
            self.set_budget_from(test_user.budget_from)

        with allure.step('Регионы'):
            self.set_regions(test_user.regions)

    def set_confirmability(self):
        if browser.element('#filter-confirmability').wait_until(be.visible):
            (browser.element('#filter-confirmability')
             .element(f'#\\31[class*=MultiToggleSwitch]')
             .with_(timeout=12).click())

            hotels_with_instant_confirmation = (
                self.all_hotel_cards.all('[class*=InstantConfirmIcon]'))
            self.all_hotel_cards.should(have.size(len(hotels_with_instant_confirmation)))
        else:
            pass

    def set_stars(self, stars):
        browser.element(f'#\\3{stars}[type=checkbox]').click()

        # Находим все карточки отелей
        all_given_stars_per_hotel = self.all_hotel_cards.all('[itemprop=ratingValue]')

        # Проверяем, что у всех найденных отелей есть искомое кол-во звезд,
        # чтобы впоследствии получить кол-во таких отелей
        filtered_ratings = all_given_stars_per_hotel.by(have.attribute('content', stars))

        # Сравниваем
        all_given_stars_per_hotel.should(have.size(len(filtered_ratings)))

    def set_rating(self, rating):
        do.scroll_to('.filter-meals')

        (browser.all('[class*=SwitcherItem]')
         .element_by(have.exact_text(rating + '+')).click())

        all_given_ratings = self.all_hotel_cards.all('[class*=HotelRating]')

        self.all_hotel_cards.should(have.size(len(all_given_ratings)))

        # Проверка, что рейтинг каждого отеля >= указанного рейтинга
        for i in range(len(all_given_ratings)):
            # Получаем value у элемента и преобразуем в float, чтобы проверить
            value = float(all_given_ratings[i].get(query.value))
            assert value >= float(rating), f'Рейтинг отеля {value} меньше указанного: {rating}'

    def set_budget_from(self, budget_from):
        (browser.all('input[class*=PriceFilterInput]')
         .first
         .type(budget_from).press_enter())
        all_given_prices = browser.all('[itemprop=priceRange]')

        for i in range(len(all_given_prices)):
            text_value = all_given_prices[i].get(query.text)
            value = do.leave_only_digits(text_value)
            assert value >= int(budget_from), f'Бюджет отеля {value} меньше указанного: {budget_from}'

    def set_regions(self, regions):
        do.scroll_to('[class*=FilterLine__FilterDiv]')

        browser.element('[type=checkbox]#\\31 09028').click()
        browser.element('[type=checkbox]#\\31 09030').click()

        # Считаем число отелей, которое найдется согласно фильтрам
        region_1 = (browser.element('.filter-regions')
                    .element('[class*=dSjECn]')
                    .element('[class*=StyledItemInfo]'))

        region_2 = (browser.all('[class*=StyledItemName]').element_by(have.text(regions[1])).element
                    ('./following-sibling::div'))

        number_1 = int(do.extract_number_of_hotels(do.extract_text(region_1)))
        number_2 = int(do.extract_number_of_hotels(do.extract_text(region_2)))
        summ = number_1 + number_2

        browser.element('[class*=HotelCounter]').should(have.text(str(summ)))

        '''
        Либо можно прописать "неждущий" в отличие от селеновского .should ассёрт:
        assert summ == self.get_total_hotels_according_to_filters(), ('Кол-во результатов согласно фильтру не совпадает'
                                                                      ' с кол-вом найденных отелей')
        '''

        all_given_regions = self.all_hotel_cards.all('[itemprop=addressRegion]')
        all_given_regions[:summ-1].should(have.text(regions[0]).or_(have.text(regions[1])).each)

    def get_total_hotels_according_to_filters(self):
        total_loc = browser.element('[class*=HotelCounter]')
        total_number = int(do.leave_only_digits(do.extract_text(total_loc)))
        return total_number

    def open_hotel_card(self):
        do.scroll_to('[class*=HotelCounter]')

        self.all_hotel_cards.all('[class*=HotelCardExploreButton]').first.click()

    def save_hotel_name_and_price(self):
        self.get_name_of_first_hotel_card()
        self.get_price_of_first_hotel_card()

    def get_name_of_first_hotel_card(self):
        hotel_name = self.all_hotel_cards.all('[itemprop=name]').first.get(query.text)
        do.set_data('hotel_name', hotel_name)

    def get_price_of_first_hotel_card(self):
        hotel_price = self.all_hotel_cards.all('[itemprop=priceRange]').first.get(query.text)
        do.set_data('hotel_price', hotel_price)

