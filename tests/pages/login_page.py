from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "word \"login\" not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME) and \
                self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login form don't exist"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL) and \
               self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_1) and \
               self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_2), "Register Form don't exist"
