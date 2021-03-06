import pytest

from tests.pages.basket_page import BasketPage
from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.openBasket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_not_items_in_basket()
    basket_page.should_be_message_about_0_items_in_basket()
