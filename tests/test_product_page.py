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

    @pytest.mark.need_review
    @pytest.mark.parametrize('url',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
    def test_guest_can_add_product_to_basket(self,browser, url):
        page = ProductPage(browser, url)
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
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_not_items_in_basket()
    basket_page.should_be_message_about_0_items_in_basket()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        time.sleep(1)
        page.should_be_authorized_user()

    @pytest.mark.skip
    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        time.sleep(1)
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.click_on_add_in_the_basket_button()
        time.sleep(1)
        product_page.message_about_adding_in_basket_exist()
        product_page.sum_in_basket_is_true()
