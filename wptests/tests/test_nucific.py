
import pytest
import random

from ..pages.cart_1sc import *
from ..pages.nucific import *
from ..products.nucific_products import PRODUCTS
from pytest_testrail.plugin import pytestrail


@pytest.mark.ui
class TestNucific:  # Must start with 'Test...'

    @pytestrail.case('')
    def test_chatbot(self, browser, app_config):
        """ Quick test to know the home mpage is accessable. """
        test_page = BotTestPage(driver=browser)
        test_page.go(app_config.base_url_nucific)
        assert test_page.is_on_page()
        #time.sleep(5)
        test_page.chatbot_open()
        time.sleep(3)
        test_page.chatbot_send_message("returns")
        time.sleep(5)

    @pytestrail.case('')
    def test_existence(self, browser, app_config):
        """ Quick test to know the home mpage is accessable. """
        home_page = HomePage(driver=browser)
        home_page.go(app_config.base_url_nucific)
        assert home_page.is_on_page()

    def test_purchase_renewal(self, browser, app_config):
        # https://brandx.goldenhippo.com/product/test-internal-subscription-vital-reds/
        product_detail_page = ProductDetailPage(driver=browser)

    @pytestrail.case('')
    def test_header(self, browser, app_config):
        """
        Clicks on each link in the header, verifies the next page's title
        """
        header = Header(driver=browser)
        about_page = AboutPage(driver=browser)
        product_page = ProductDetailPage(driver=browser)
        blog_page = BlogPage(driver=browser)
        contact_page = ContactPage(driver=browser)
        cart_page = CartPage(driver=browser)
        header.go(app_config.base_url_nucific)
        # logo
        header.click_on_link(header.logo_link)
        assert header.is_on_page()
        # about
        header.click_on_link(header.about_link)
        header.click_on_link(header.about_sub_link)
        assert about_page.is_on_page()
        header.go(app_config.base_url_nucific)
        # products
        header.click_on_link(header.products_link)
        header.click_on_link(header.products_sub_link)
        assert product_page.is_on_page()
        header.go(app_config.base_url_nucific)
        # blog
        header.click_on_link(header.blog_link)
        assert blog_page.is_on_page()
        header.go(app_config.base_url_nucific)
        # contact
        header.click_on_link(header.contact_link)
        assert contact_page.is_on_page()
        header.go(app_config.base_url_nucific)
        # cart
        header.click_on_link(header.cart_link)
        assert cart_page.is_on_page()
        header.go(app_config.base_url_nucific)

    @pytestrail.case('')
    def test_ftc_signup(self, browser, app_config):
        home_page = HomePage(driver=browser)
        ftc_page = FTCPage(driver=browser)
        home_page.go(app_config.base_url_nucific)
        home_page.ftc_signup()
        assert ftc_page.is_on_page()

    @pytestrail.case('C206')
    def test_ftc_continuity(self, browser, app_config):
        ftc_page = FTCPage(driver=browser)
        ftc_page.go(app_config.base_url_nucific)
        assert True

    @pytestrail.case('')
    def test_blog_pagination(self):
        pass

    @pytestrail.case('')
    def test_submit_review(self, browser, app_config):
        pass

    @pytestrail.case('')
    def test_submit_contact_form(self, browser, app_config):
        contact_page = ContactPage(driver=browser)
        contact_page.go(app_config.base_url_nucific)
        contact_page.form_submit()
        # This test currently fails because it has no success message.
        assert contact_page.form_success_msg == "Thank you for contacting us. We'll be in touch shortly."

    @pytest.mark.skip
    def test_get_products(self, browser, app_config):
        """ NOt an actual test. This is used to get a current list of products"""
        producst_page = SupplementsPage(driver=browser)
        producst_page.go(app_config.base_url_nucific)
        print(producst_page.get_products())
        assert False

    @pytestrail.case('', '', '')
    #@pytest.mark.parametrize("title, page, quantity", random.sample(PRODUCTS, 1))
    @pytest.mark.parametrize("title, page, quantity", PRODUCTS)
    def test_add_to_cart(self, browser, app_config, title, page, quantity):
        """
        Randomly selects a product, goes to detail page, selects a quantity, notes price, adds to cart,
        verifies that price and title match.
        """
        product_page = ProductDetailPage(driver=browser)
        cart_page = CartPage(driver=browser)
        url = app_config.base_url_nucific + page
        product_page.go(url)
        pp_price = product_page.select_quantity(quantity)
        #print("pp_price = ", pp_price)
        product_page.click_addtocart()
        assert pp_price == cart_page.item_price
        #assert title.lower() in cart_page.item_short_desc.text.lower()
        assert title.lower() in cart_page.item_title.text.lower()
        cart_page.remove_cart_first_item()
        assert cart_page.cart_empty_msg.text == 'Your shopping cart is empty.', "Cart isn't empty!"

    @pytestrail.case('')
    #@pytest.mark.parametrize("title, page, quantity", [('Bio-X4', 'bio-x4', '1'),])
    @pytest.mark.parametrize("title, page, quantity", random.sample(PRODUCTS, 1))
    def test_cart_increase_quantity(elf, browser, app_config, title, page, quantity):
        product_page = ProductDetailPage(driver=browser)
        cart_page = CartPage(driver=browser)
        url = app_config.base_url_nucific + page
        product_page.go(url)
        product_page.select_quantity(quantity)
        pp_price = product_page.get_price(quantity)
        product_page.click_addtocart()
        cart_page.increment_quanity()
        assert cart_page.item_qty.get_attribute('value') == "2"
        cart_page.recalculate_cart()
        assert float(cart_page.item_total.strip('$')) == 2 * float(cart_page.item_price.strip('$'))

    pytestrail.case('')
    def test_coupon_code(self):
        pass



    @pytestrail.case('')
    def test_checkout_with_paypal(self):
        pass

    @pytestrail.case('')
    def test_checkout_with_credit_card(self):
        pass


