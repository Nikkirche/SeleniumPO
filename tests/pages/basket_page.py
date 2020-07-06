from tests.pages.base_page import BasePage
from tests.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_OF_ITEMS_IN_BASKET), " Basket items are presented"
    def should_be_message_about_0_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_0_ELEMENTS_IN_BASKET),"Message about  items don't show"