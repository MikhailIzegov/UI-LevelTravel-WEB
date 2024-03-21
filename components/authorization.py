from selene import browser, have, be


class Authorization:
    def via_email_option(self):
        browser.all("[type='button']").element_by(have.exact_text('Почта')).click()

    def fill_email(self, login):
        browser.element('#email').send_keys(login).press_enter()

    def fill_password(self, password):
        browser.element('#password').send_keys(password).press_enter()

    def is_logged_in(self):
        browser.element('[class*=CashBackContainer]').with_(timeout=10).should(be.visible)


auth = Authorization()
