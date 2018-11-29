
import pytest
import random

from ..pages.cart_wc import *
from ..pages.gundrywellness import *
from ..products.gundrywellness_products import PRODUCTS
from pytest_testrail.plugin import pytestrail


@pytest.mark.ui
class TestGundryWellness:  # Must start with 'Test...'
    """ Tests for GundryWellness.com"""

    @pytestrail.case('')
    def test_existence(self, browser, app_config):
        """ Quick test to know the home mpage is accessable. """
        home_page = HomePage(driver=browser)
        home_page.go(app_config.base_url_gundrywellness)
        assert home_page.is_on_page()

    @pytestrail.case('')
    def test_header(self, browser, app_config):
        """
        Clicks on each link in the header, verifies the next page's title
        TODO: Header - verify podcast links.
        """
        header = Header(driver=browser)
        ambassador_page = AmbassadorLoginPage(driver=browser)
        about_page = AboutPage(driver=browser)
        blog_page = BlogPage(driver=browser)
        products_page = ProductsPage(driver=browser)
        contact_page = ContactPage(driver=browser)
        header.go(app_config.base_url_gundrywellness)
        # logo
        header.click_on_link(header.logo_link)
        assert header.is_on_page()
        # ambassador login page
        header.click_on_link(header.ambassador_link)
        assert ambassador_page.is_on_page()
        # about
        header.click_on_link(header.about_link)
        assert about_page.is_on_page()
        header.go(app_config.base_url_gundrywellness)
        # products
        header.click_on_link(header.products_link)
        assert products_page.is_on_page()
        header.go(app_config.base_url_gundrywellness)

    @pytestrail.case('')
    def test_ftc_signup(self, browser, app_config):
        home_page = HomePage(driver=browser)
        ftc_page = FTCPage(driver=browser)
        home_page.go(app_config.base_url_gundrywellness)
        home_page.ftc_signup()
        assert ftc_page.is_on_page()

    @pytestrail.case('')
    def test_ftc_continuity(self, browser, app_config):
        ftc_page = FTCPage(driver=browser)
        ftc_page.go(app_config.base_url_gundrywellness)
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
        contact_page.go(app_config.base_url_gundrywellness)
        contact_page.form_submit()
        # This test currently fails because it has no success message.
        assert contact_page.form_success_msg == 'Thank you for your message. It has been sent.'

    @pytest.mark.skip
    def test_get_products(self, browser, app_config):
        """ NOt an actual test. This is used to get a current list of products"""
        producst_page = SupplementsPage(driver=browser)
        producst_page.go(app_config.base_url_gundrywellness)
        print(producst_page.get_products())
        assert False

    @pytestrail.case('')
    @pytest.mark.parametrize(
        "title, page, quantity", random.sample(PRODUCTS, 1))
    def test_add_to_cart(self, browser, app_config, title, page, quantity):
        """
        Randomly selects a product, goes to detail page, selects a quantity, notes price, adds to cart,
        verifies that price and title match.
        """
        product_page = ProductDetailPage(driver=browser)
        cart_page = CartPage(driver=browser)
        url = app_config.base_url_gundrywellness + page
        product_page.go(url)
        product_page.select_quantity(quantity)
        pp_price = product_page.price
        product_page.click_addtocart()
        assert pp_price == cart_page.item_price
        #print("title from file: " + title.lower())
        #print("title in cart: " + cart_page.item_short_desc.text.lower)
        time.sleep(5)
        assert title.lower() in cart_page.item_short_desc.text.lower()
        #cart_page.remove_cart_first_item()
        #assert cart_page.cart_empty_msg.text == 'Your shopping cart is empty.', "Cart isn't empty!"

    @pytestrail.case('')
    @pytest.mark.parametrize(
        "title, page, quantity", [
            ('Total Restore', 'total-restore', '1'),
        ]
    )
    def test_cart_increase_quantity(elf, browser, app_config, title, page, quantity):
        product_page = ProductDetailPage(driver=browser)
        cart_page = CartPage(driver=browser)
        url = app_config.base_url_gundrywellness + '/supplements/' + page
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
