import re

from selene import browser, command, query


class Additional_Actions:
    def scroll_to(self, locator):
        browser.element(locator).perform(command.js.scroll_into_view)

    def leave_only_digits(self, text_value):
        return int(''.join(re.findall(r'\d', text_value)))

    def count_number_of_hotels_to_be_given(self, locator_1, locator_2):
        text_1 = locator_1.get(query.text)

        text_2 = locator_2.get(query.text)

    def extract_number_of_hotels(self, text):
        first_space_index = text.find(' ')
        number = text[:first_space_index]
        return number

    def extract_text(self, locator):
        return locator.get(query.text)


do = Additional_Actions()
