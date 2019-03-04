
import pytest
import random

from ..pages.cart_wc import *
from ..pages.gundrymd import *
from ..products.gundrymd_products import PRODUCTS
from pytest_testrail.plugin import pytestrail


@pytest.mark.ui
class TestGundryMD:  # Must start with 'Test...'

    @pytest.mark.critical
    @pytestrail.case('C131')
    def test_existence(self, browser, app_config):
        """ Quick test to know the home mpage is accessable. """
        home_page = HomePage(driver=browser)
        home_page.go(app_config.base_url_gundrymd)
        assert home_page.is_on_page()

    @pytestrail.case('C201')
    def test_header(self, browser, app_config):
        """
        Clicks on each link in the header, verifies the next page's title
        TODO: Header - verify podcast links.
        """
        header = Header(driver=browser)
        about_page = AboutPage(driver=browser)
        blog_page = BlogPage(driver=browser)
        supplements_page = SupplementsPage(driver=browser)
        skincare_page = SkinCarePage(driver=browser)
        food_page = FoodPage(driver=browser)
        books_page = BooksPage(driver=browser)
        vip_page = VipPage(driver=browser)
        header.go(app_config.base_url_gundrymd)
        # logo
        header.click_on_link(header.logo_link)
        assert header.is_on_page()
        # about
        header.click_on_link(header.about_link)
        assert about_page.is_on_page()
        header.go(app_config.base_url_gundrymd)
        # blog
        header.click_on_link(header.blog_link)
        assert blog_page.is_on_page()
        header.go(app_config.base_url_gundrymd)
        # supplements
        header.click_on_link(header.supplements_link)
        assert supplements_page.is_on_page()
        header.go(app_config.base_url_gundrymd)
        # skincare
        header.click_on_link(header.skincare_link)
        assert skincare_page.is_on_page()
        header.go(app_config.base_url_gundrymd)
        # food
        header.click_on_link(header.food_link)
        assert food_page.is_on_page()
        header.go(app_config.base_url_gundrymd)
        # books
        header.click_on_link(header.books_link)
        assert books_page.is_on_page()
        header.go(app_config.base_url_gundrymd)
        # Vip
        header.click_on_link(header.vip_link)
        assert vip_page.is_on_page()

    @pytestrail.case('C164')
    def test_ftc_signup(self, browser, app_config):
        """
        First tests that the required fields are populated, then with valid inputs, checks if user is taken
        to the ftc page.
        """
        home_page = HomePage(driver=browser)
        ftc_page = FTCPage(driver=browser)
        home_page.go(app_config.base_url_gundrymd)
        home_page.ftc_signup('', 'tester@goldenhippo.com')
        assert not ftc_page.is_on_page()
        home_page.ftc_signup('Tester', '')
        assert not ftc_page.is_on_page()
        home_page.ftc_signup('Tester', 'tester@goldenhippo.com')
        assert ftc_page.is_on_page()

    @pytestrail.case('C164')
    def test_ftc_products_page(self, browser, app_config):
        """
        First tests that the required fields are populated, then with valid inputs, checks if user is taken
        to the ftc page.
        """
        ftc_page = FTCPage(driver=browser)
        ftc_page.go(app_config.base_url_gundrymd)
        print(ftc_page.page_titles)
        assert 'Here are our first time customer specials on Gundry MD' in ftc_page.page_titles
        assert 'SUPPLEMENTS' in ftc_page.page_titles
        assert 'Vital Reds' in ftc_page.page_titles
        assert 'PrebioThrive' in ftc_page.page_titles
        assert 'Total Restore' in ftc_page.page_titles
        assert 'Lectin Shield' in ftc_page.page_titles
        assert 'Proplant' in ftc_page.page_titles
        assert 'Primal Plants' in ftc_page.page_titles
        assert 'Heart Defense' in ftc_page.page_titles
        assert 'E-Balance' in ftc_page.page_titles
        assert 'Enhanced Circulation Formula' in ftc_page.page_titles
        assert 'TriTrim Multipack' in ftc_page.page_titles
        assert 'SKINCARE' in ftc_page.page_titles
        assert 'Polyphenol Dark Spot Diminisher' in ftc_page.page_titles



    pytestrail.case('C164')
    def test_ftc_products(self, browser, app_config):
        """
        Tests each product in this list
        """
        ftc_page = FTCPage(driver=browser)
        ftc_page.go(app_config.base_url_gundrymd)
        assert True

    @pytest.mark.skip
    @pytestrail.case('C206')
    def test_ftc_continuity(self, browser, app_config):
        ftc_page = FTCPage(driver=browser)
        ftc_page.go(app_config.base_url_gundrymd)
        assert True

    @pytestrail.case('C27')
    def test_blog_pagination(self):
        pass

    @pytestrail.case('C123')
    def test_submit_review(self, browser, app_config):
        pass

    @pytest.mark.critical
    @pytestrail.case('116')
    def test_submit_contact_form(self, browser, app_config):
        contact_page = ContactPage(driver=browser)
        contact_page.go(app_config.base_url_gundrymd)
        contact_page.form_submit()
        # This test currently fails because it has no success message.
        assert contact_page.form_success_msg == 'Thank you for your message. It has been sent.'

    @pytest.mark.skip
    def test_get_products(self, browser, app_config):
        """ NOt an actual test. This is used to get a current list of products"""
        products_page = SupplementsPage(driver=browser)
        products_page.go(app_config.base_url_gundrymd)
        print(products_page.get_products())
        assert False

    @pytestrail.case('')
    @pytest.mark.parametrize("page, expected_result", [
        ('supplements', 30),
        ('skincare', 5),
        ('food', 3)])
    def test_count_products(self, browser, app_config, page, expected_result):
        """
        This test simply counts the number of products.  If the count is different than the expected count, then it
        will fail.  This will help us know if a product gets added without our knowledge, so we can test it.
        """
        if page == 'supplements':
            products_page = SupplementsPage(driver=browser)
        elif page == 'skincare':
            products_page = SkinCarePage(driver=browser)
        else:
            products_page = FoodPage(driver=browser)
        products_page.go(app_config.base_url_gundrymd)
        actual_result = len(products_page.get_products())
        assert actual_result == expected_result

    @pytestrail.case('C133', 'C135', 'C138')
    #@pytest.mark.parametrize("title, page, quantity", random.sample(PRODUCTS, 1))
    @pytest.mark.parametrize("title, page, quantity", PRODUCTS)
    def test_add_to_cart(self, browser, app_config, title, page, quantity):
        """
        Randomly selects a product, goes to detail page, selects a quantity, notes price, adds to cart,
        verifies that price and title match.
        """
        product_page = ProductDetailPage(driver=browser)
        cart_page = CartPage(driver=browser)
        url = app_config.base_url_gundrymd + page
        product_page.go(url)
        product_page.select_quantity(quantity)
        pp_price = product_page.price
        product_page.click_addtocart()
        assert pp_price == cart_page.item_price
        assert title.lower() in cart_page.item_short_desc.text.lower()
        cart_page.remove_cart_first_item()
        assert cart_page.cart_empty_msg.text == 'Your shopping cart is empty.', "Cart isn't empty!"

    @pytestrail.case('C139')
    @pytest.mark.parametrize(
        "title, page, quantity", [
            ('Total Restore', 'total-restore', '1'),
        ]
    )
    def test_cart_increase_quantity(elf, browser, app_config, title, page, quantity):
        """ Increases the quantity, recalculates, and checks for new total"""
        product_page = ProductDetailPage(driver=browser)
        cart_page = CartPage(driver=browser)
        url = app_config.base_url_gundrymd + '/supplements/' + page
        product_page.go(url)
        product_page.select_quantity(quantity)
        pp_price = product_page.price
        product_page.click_addtocart()
        cart_page.increment_quanity()
        assert cart_page.item_qty.get_attribute('value') == "2"
        cart_page.recalculate_cart()
        assert float(cart_page.item_total.strip('$')) == 2 * float(cart_page.item_price.strip('$'))

    pytestrail.case('C142')
    def test_coupon_code(self, browser, app_config):
        """
        Enters an invalid code, checks the alert message.  Currently not coupon codes for site.
        TODO: add a valid coupon code when it becomes available.
        (May be flaky since they have expiry dates
        """
        cart_page = CartPage(driver=browser)
        url = app_config.base_url_gundrymd + '/cmd.php?pid=f7d1003f4829438e80ffa60c416df476'
        cart_page.go(url)
        cart_page.apply_coupon('coupon10')  # Invalid code.
        assert 'Sorry, the coupon code you have entered is invalid. Please check the code and try again.' in cart_page.alert_messages
        # Valid coupon code
        # Site currently has no vaild coupon codes.


    @pytestrail.case('C159')
    def test_checkout_with_credit_card(self):
        """
        Currently test are using live cart transactions, so this will need to wait until TouchCR has a test environment.
        :return:
        """
        pass

    @pytestrail.case('C155')
    def test_checkout_with_paypal(self):
        pass
