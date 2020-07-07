import time

import pytest

from tests.pages.basket_page import BasketPage
from tests.pages.login_page import LoginPage
from tests.pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestGuestAddToBasketFromProductPage:
    @pytest.mark.skip
    def test_guest_cant_see_success_message(browser):
        page = ProductPage(browser, link)
        page.open()
        time.sleep(1)
        page.should_not_be_success_message()

    @pytest.mark.skip
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.click_on_add_in_the_basket_button()
        page.solve_quiz_and_get_code()
        page.message_about_adding_in_basket_exist()
        page.sum_in_basket_is_true()


@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_in_the_basket_button()
    time.sleep(1)
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_in_the_basket_button()
    time.sleep(1)
    page.should_disappeared_success_message()


@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_not_items_in_basket()
    basket_page.should_be_message_about_0_items_in_basket()


class TestUserAddToBasketFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        time.sleep(1)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        time.sleep(1)
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self,browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.click_on_add_in_the_basket_button()
        time.sleep(1)
        product_page.message_about_adding_in_basket_exist()
        product_page.sum_in_basket_is_true()
