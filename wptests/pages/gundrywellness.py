import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .base_element import BaseElement
from .cart_wc import *


class Header(BasePage):
    path = "/"

    def is_on_page(self):
        return "Home" in self.driver.title

    @property
    def logo_link(self):
        return self.driver.find_element(By.ID,"logo")

    @property
    def ambassador_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu .menu-item-132347")

    @property
    def about_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu .menu-item-131506")

    @property
    def products_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu .menu-item-131505")

    @property
    def contact_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu .menu-item-131504")

    @property
    def cart_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu .menu-item-131523")

    def click_on_link(self, link):
        link.click()


class HomePage(BasePage):
    path = '/'

    def is_on_page(self):
        return "Home" in self.driver.title

    def test_contact_page_form(self):
        self.ftc_first_name_input.send_keys("Tester")
        self.ftc_email_input.send_keys("tester@goldenhippo.com")
        self.ftc_signup_btn.click()


class AboutPage(BasePage):
    path = '/gundry-md/'

    def is_on_page(self):
        return "About - Gundry Wellness" in self.driver.title


class AmbassadorLoginPage(BasePage):
    path = '/ambassador-area/'

    def is_on_page(self):
        return "Ambassador Portal - Gundry Wellness" in self.driver.title


class BlogPage(BasePage):
    path = '/blog/'

    def is_on_page(self):
        return "Blog - Gundry MD" in self.driver.title


class ProductsPage(BasePage):
    path = '/products/'

    def is_on_page(self):
        return "Products" in self.driver.title

    @property
    def product_titles(self):
        return self.driver.find_elements(By.CSS_SELECTOR,".entry-title")

    @property
    def product_detail_btns(self):
        return self.driver.find_elements(By.XPATH, "//article/div/a")

    #@property
    #def learn_more_button(self):
    #    locator = (By.XPATH, '//article')
    #    return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    def get_products(self):
        products = []
        for title in self.product_titles:
            print(title.text)
            products.append({'title': title.text})
            #for btn in self.product_detail_btns:
            #    print(str(btn))
            #    #products.append({'btm': btn})
        return products

    def add_products_to_cart(self):
        for btn in self.product_detail_btns:
            product_detail_page = btn.click()
            time.sleep(1)
            product_detail_page.supplements_link.click()


class ProductDetailPage(BasePage):
    path = ''

    def is_on_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.entry-summary")

    @property
    def price(self):
        price = self.driver.find_element(By.CSS_SELECTOR, "span.tabbed-radio-st-variant-details span.tabbed-radio-st-price").text
        return price


    def select_quantity(self, qty):
        choice = "//span[contains(text(), qty)]/parent::label"
        self.driver.find_element(By.XPATH, choice).click()

    @property
    def add_to_cart_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".et_pb_button.tabbed-radio-st-addtocart")

    def click_addtocart(self):
        self.add_to_cart_btn.click()


class ContactPage(BasePage):
    path = '/contact'

    def is_on_page(self):
        """Verifies that the hardcoded text "HOME - Gundry MD" appears in page title"""
        return "Contact - Gundry Wellness" in self.driver.title

    # Contact Form

    @property
    def form_first_name_input(self):
        return self.driver.find_element(By.ID, "et_pb_contact_name_1")

    @property
    def form_email_input(self):
        return self.driver.find_element(By.ID, "et_pb_contact_email_1")

    @property
    def form_message_textarea(self):
        return self.driver.find_element(By.ID, "et_pb_contact_message_1")

    @property
    def form_submit_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button.et_pb_contact_submit")

    @property
    def form_success_msg(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.et-pb-contact-message p").text

    def form_submit(self):
        self.form_first_name_input.send_keys("Test")
        self.form_email_input.send_keys("tester@goldenhippo.com")
        self.form_message_textarea.send_keys("TESTING... Please ignore.")
        self.form_submit_btn.click()
        # The form takes a few seconds to send so I've added a wait here until I see the message.
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.et-pb-contact-message p'), "Thanks for contacting us"))
