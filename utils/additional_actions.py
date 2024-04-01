import re

from selene import browser, command, query


class AdditionalActions:
    def scroll_to(self, locator):
        browser.element(locator).perform(command.js.scroll_into_view)

    def leave_only_digits(self, text_value):
        return int(''.join(re.findall(r'\d', text_value)))

    def extract_number_of_hotels(self, text):
        first_space_index = text.find(' ')
        number = text[:first_space_index]
        return number

    def extract_text(self, locator):
        return locator.get(query.text)


do = AdditionalActions()
