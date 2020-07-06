import time

from tests.pages.base_page import BasePage
from tests.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_add_in_the_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add Button don't exist"
        self.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def message_about_adding_in_basket_exist(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE)
        assert self.is_element_present(*ProductPageLocators.NAME)
        template = "{} has been added to your basket."
        message = self.find_element(*ProductPageLocators.MESSAGE).text
        book_name = self.find_element(*ProductPageLocators.NAME).text
        assert template.format(message) == template.format(book_name), 'нет названия книги {message}'.format(
            message=message)

    def sum_in_basket_is_true(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Price don't show"
        assert self.is_element_present(*ProductPageLocators.SUM_CART), "Sum in basket, don't show"
        price = str(self.find_element(*ProductPageLocators.PRICE).text)
        basket_text = str(self.find_element(*ProductPageLocators.SUM_CART).text)

        assert price == basket_text, "Sum in basket is wrong"
