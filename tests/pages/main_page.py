from .base_page import BasePage
from .locators import BasePageLocators


class MainPage(BasePage):


    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
