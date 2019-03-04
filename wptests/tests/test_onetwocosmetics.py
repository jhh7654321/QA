
import pytest
import random

from ..pages.cart_wc import *
from ..pages.onetwocosmetics import *
from ..products.onetwocosmetics_products import PRODUCTS
from pytest_testrail.plugin import pytestrail


@pytest.mark.ui
class TestOneTwoCosmetics:  # Must start with 'Test...'
    """ Tests for OneTwoCosmetics.com"""

    @pytestrail.case('')
    def test_existence(self, browser, app_config):
        """ Quick test to know the home mpage is accessable. """
        home_page = HomePage(driver=browser)
        home_page.go(app_config.base_url_onetwocosmetics)
        assert home_page.is_on_page()

    @pytestrail.case('')
    def test_header(self, browser, app_config):
        """
        Clicks on each link in the header, verifies the next page's title
        """
        header = Header(driver=browser)
        shop_page = ShopPage(driver=browser)
        how_to_apply = HowToApplyPage(driver=browser)
        difference_page = TheOTCDifferencePage(driver=browser)
        blog_page = BlogPage(driver=browser)
        press_page =PressPage(driver=browser)
        our_story_page = OurStoryPage(driver=browser)
        login_page = LoginPage(driver=browser)
        cart_page = CartPage(driver=browser)
        header.go(app_config.base_url_onetwocosmetics)
        # logo
        header.click_on_link(header.logo_link)
        assert header.is_on_page()
        # shop
        header.click_on_link(header.shop_link)
        #header.click_on_link(header.shop_classic_sub_link)
        assert shop_page.is_on_page()
        header.go(app_config.base_url_onetwocosmetics)
        # how to apply
        header.click_on_link(header.how_to_apply_link)
        assert how_to_apply.is_on_page()
        header.go(app_config.base_url_onetwocosmetics)
        # the OTC difference
        header.click_on_link(header.otc_difference_link)
        assert difference_page.is_on_page()
        header.go(app_config.base_url_onetwocosmetics)
        # blog
        header.click_on_link(header.blog_link)
        assert blog_page.is_on_page()
        header.go(app_config.base_url_onetwocosmetics)
        # press
        header.click_on_link(header.press_link)
        assert press_page.is_on_page()
        header.go(app_config.base_url_onetwocosmetics)
        # our story
        header.click_on_link(header.our_story_link)
        assert our_story_page.is_on_page()
        header.go(app_config.base_url_onetwocosmetics)
        # cart / Bug WD-4644 - Goes to Woo cart, not 1SC
        #header.click_on_link(header.cart_link)
        #assert cart_page.is_on_page()
        #header.go(app_config.base_url_onetwocosmetics)

    @pytestrail.case('')
    def test_blog_pagination(self):
        pass

    @pytestrail.case('')
    def test_submit_review(self, browser, app_config):
        pass

    @pytestrail.case('')
    def test_submit_contact_form(self, browser, app_config):
        contact_page = ContactPage(driver=browser)
        contact_page.go(app_config.base_url_onetwocosmetics)
        contact_page.form_submit()
        assert contact_page.form_success_msg == 'Your message was sent successfully. One of our Lash Experts will get back to you within 48 hours. Love and Lashes.'

    @pytest.mark.skip
    def test_get_products(self, browser, app_config):
        """ NOt an actual test. This is used to get a current list of products"""
        producst_page = SupplementsPage(driver=browser)
        producst_page.go(app_config.base_url_onetwocosmetics)
        print(producst_page.get_products())
        assert False

    @pytestrail.case('', '', '')
    #@pytest.mark.parametrize( "title, page, quantity", random.sample(PRODUCTS, 1))
    @pytest.mark.parametrize("title, page, quantity", PRODUCTS)
    #@pytest.mark.parametrize("title, page, quantity", [("FOUNDERS's LASH", '/shop/founders-lash/', '3 CASES')])
    def test_add_to_cart(self, browser, app_config, title, page, quantity):
        """
        Randomly selects a product, goes to detail page, selects a quantity, notes price, adds to cart,
        verifies that price and title match.
        """
        product_page = ProductDetailPage(driver=browser)
        cart_page = CartPage(driver=browser)
        url = app_config.base_url_onetwocosmetics + page
        product_page.go(url)
        product_page.select_quantity(quantity)
        pp_price = product_page.price
        time.sleep(1)
        product_page.click_addtocart()
        assert pp_price == cart_page.item_price
        assert title.lower() in cart_page.item_short_desc.text.lower()
        cart_page.remove_cart_first_item()
        #assert cart_page.cart_empty_msg.text == 'Your cart is currently empty.'
        assert cart_page.cart_empty_msg.text == 'Your shopping cart is empty.'  # Black Friday

    @pytestrail.case('')
    @pytest.mark.parametrize("title, page, quantity", random.sample(PRODUCTS, 1))
    def test_cart_increase_quantity(elf, browser, app_config, title, page, quantity):
        product_page = ProductDetailPage(driver=browser)
        cart_page = CartPage(driver=browser)
        url = app_config.base_url_onetwocosmetics + page
        product_page.go(url)
        product_page.select_quantity(quantity)
        pp_price = product_page.price
        product_page.click_addtocart()
        cart_page.increment_quanity()
        assert cart_page.item_qty.get_attribute('value') == "2"
        cart_page.recalculate_cart()
        assert float(cart_page.item_total.strip('$')) == 2 * float(cart_page.item_price.strip('$'))

    pytestrail.case('')
    def test_coupon_code(self):
        pass

    @pytestrail.case('')
    def test_checkout_with_credit_card(self):
        pass

    @pytestrail.case('')
    def test_checkout_with_paypal(self):
        pass
