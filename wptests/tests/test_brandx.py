
import pytest
import random

from ..pages.cart_wc import *
from ..pages.brandx import *
from ..products.brandx_products import PRODUCTS
from pytest_testrail.plugin import pytestrail


@pytest.mark.ui
class TestBrandX:  # Must start with 'Test...'
    """ Tests for BrandX"""

    @pytestrail.case('')
    def test_existence(self, browser, app_config):
        """ Quick test to know the home mpage is accessable. """
        home_page = HomePage(driver=browser)
        home_page.go(app_config.base_url_brandx)
        assert home_page.is_on_page()

    def test_purchase_renewal(self, browser, app_config):
        # https://brandx.goldenhippo.com/product/test-internal-subscription-vital-reds/
        product_detail_page = ProductDetailPage(driver=browser)

    @pytestrail.case('')
    def test_header(self, browser, app_config):
        """
        Clicks on each link in the header, verifies the next page's title
        TODO: Header - verify podcast links.
        """
        header = Header(driver=browser)
        blog_page = BlogPage(driver=browser)
        products_page = ProductsPage(driver=browser)
        contact_page = ContactPage(driver=browser)
        header.go(app_config.base_url_brandx)
        # logo
        header.click_on_link(header.logo_link)
        assert header.is_on_page()
        # blog
        header.click_on_link(header.blog_link)
        assert blog_page.is_on_page()
        header.go(app_config.base_url_brandx)
        # shop
        header.click_on_link(header.shop_link)
        assert products_page.is_on_page()
        header.go(app_config.base_url_brandx)

    @pytestrail.case('')
    def test_blog_pagination(self):
        pass

    @pytestrail.case('')
    def test_submit_review(self, browser, app_config):
        pass

    @pytestrail.case('')
    def test_submit_contact_form(self, browser, app_config):
        contact_page = ContactPage(driver=browser)
        contact_page.go(app_config.base_url_brandx)
        contact_page.form_submit()
        # This test currently fails because it has no success message.
        contact_page.form_success_msg
        assert contact_page.form_success_msg == 'Thanks for contacting us'

    @pytest.mark.skip
    def test_get_products(self, browser, app_config):
        """ NOt an actual test. This is used to get a current list of products"""
        producst_page = SupplementsPage(driver=browser)
        producst_page.go(app_config.base_url_brandx)
        print(producst_page.get_products())
        assert False

    @pytestrail.case('', '', '')
    @pytest.mark.parametrize("title, page, quantity", random.sample(PRODUCTS, 1))
    #@pytest.mark.parametrize("title, page, quantity", PRODUCTS)
    def test_add_to_cart(self, browser, app_config, title, page, quantity):
        """
        Randomly selects a product, goes to detail page, selects a quantity, notes price, adds to cart,
        verifies that price and title match.
        """
        product_page = ProductDetailPage(driver=browser)
        cart_page = CartPage(driver=browser)
        url = app_config.base_url_brandx + page
        product_page.go(url)
        product_page.set_quantity(quantity)
        pp_price = product_page.price
        product_page.click_addtocart()
        assert pp_price == cart_page.item_price
        assert title.lower() in cart_page.item_short_desc.text.lower()
        cart_page.remove_cart_first_item()
        assert cart_page.cart_empty_msg.text == 'Your cart is currently empty.', "Cart isn't empty!"

    @pytestrail.case('')
    @pytest.mark.parametrize("title, page, quantity", [('Vital Reds', 'vital-reds', '1'),])
    def test_cart_increase_quantity(elf, browser, app_config, title, page, quantity):
        product_page = ProductDetailPage(driver=browser)
        cart_page = CartPage(driver=browser)
        url = app_config.base_url_brandx + '/product/' + page
        product_page.go(url)
        product_page.set_quantity(2)
        pp_price = product_page.price
        product_page.click_addtocart()
        cart_page.increment_quanity()
        assert cart_page.item_qty.get_attribute('value') == "3"
        cart_page.recalculate_cart()
        assert str(float(cart_page.item_total.strip('$'))) == cart_page.item_price.strip('$')

    pytestrail.case('')
    def test_coupon_code(self):
        pass



    @pytestrail.case('')
    def test_checkout_with_paypal(self):
        pass

    @pytestrail.case('')
    def test_checkout_with_credit_card(self):
        pass

    @pytestrail.case('')
    def test_subscription_purchase_woocommerce(self, browser, app_config):
        """ Places order for a subscription product, then renews that product """
        # Login as a customer
        login_page = LoginPage(driver=browser)
        product_detail_page = ProductDetailPage(driver=browser)
        login_page.go(app_config.base_url_brandx)
        assert login_page.login('tester@goldenhippo.com', 'of0pE6I3mRkqPiawu$P%K%BE')
        # purchase product https://brandx.goldenhippo.com/product/test-internal-subscription-vital-reds/
        product_detail_page.go(app_config.base_url_brandx + "/product/test-internal-subscription-vital-reds/")
        product_detail_page.click_addtocart()
        # Get order ID
        # Login as Admin
        # Go to Orders, verify order created, verify status
        # Go to subscriptions, open subscription, renew
        # Go to orders, verify new order created, verify status
        time.sleep(5)

