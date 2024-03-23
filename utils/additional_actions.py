from selene import browser, command


class Additional_Actions:
    def scroll_to(self, locator):
        browser.element(locator).perform(command.js.scroll_into_view)


do = Additional_Actions()
