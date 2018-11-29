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
        if self.driver.title == "Test Cases - BrandX" or "BrandX | Test Site":
            return True
        else:
            return False

    @property
    def logo_link(self):
        return self.driver.find_element(By.ID,"logo")

    @property
    def blog_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu .menu-item-60 a")

    @property
    def shop_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu .menu-item-68 a")

    @property
    def contact_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu .menu-item-47 a")

    def click_on_link(self, link):
        link.click()


class HomePage(BasePage):
    path = '/'

    def is_on_page(self):
        if self.driver.title == "Test Cases - BrandX" or "BrandX | Test Site":
            return True
        else:
            return False


class BlogPage(BasePage):
    path = '/blog/'

    def is_on_page(self):
        return "Blog | BrandX" in self.driver.title


class ProductsPage(BasePage):
    path = '/shop/'

    def is_on_page(self):
        return "Shop – BrandX" in self.driver.title

    @property
    def product_titles(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".woocommerce-loop-product__title")

    def get_products(self):
        products = []
        for title in self.product_titles:
            print(title.text)
            products.append({'title': title.text})
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
        price = self.driver.find_element(By.CSS_SELECTOR, "p.price span.woocommerce-Price-amount.amount").text
        return price

    @property
    def quantity_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.quantity input.input-text")


    def set_quantity(self, qty):
        self.quantity_input.clear()
        self.quantity_input.send_keys(qty)

    @property
    def add_to_cart_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".single_add_to_cart_button")

    def click_addtocart(self):
        #time.sleep(5)
        self.add_to_cart_btn.click()


class ContactPage(BasePage):
    path = '/contact'

    def is_on_page(self):
        return "" in self.driver.title

    # Contact Form

    @property
    def form_first_name_input(self):
        return self.driver.find_element(By.NAME, "first-name")

    @property
    def form_last_name_input(self):
        return self.driver.find_element(By.NAME, "last-name")

    @property
    def form_email_input(self):
        return self.driver.find_element(By.NAME, "your-email")

    @property
    def form_message_textarea(self):
        return self.driver.find_element(By.NAME, "your-message")

    @property
    def form_submit_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".et_pb_contact_form_container input")

    @property
    def form_success_msg(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.wpcf7-response-output").text

    def form_submit(self):
        self.form_first_name_input.send_keys("Test")
        self.form_last_name_input.send_keys("Tester")
        self.form_email_input.send_keys("tester@goldenhippo.com")
        self.form_subject_dropdown.select_by_visible_text("6. Other")
        self.form_message_textarea.send_keys("TESTING... Please ignore.")
        self.form_submit_btn.click()
        # The form takes a few seconds to send so I've added a wait here until I see the message.
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.wpcf7-response-output'), "Thank you for your message. It has been sent."))

class LoginPage(BasePage):
    path = '/wp-login.php'

    def is_on_page(self):
        return "Log In" in self.driver.title

#    @property
#    def form_username_input(self):
#        return self.driver.find_element(By.ID, "user_login")
#
#    @property
#    def form_password_input(self):
#        return self.driver.find_element(By.ID, "user_pass")
#
#    @property
#    def form_login_btn(self):
#        return self.driver.find_element(By.ID, "wp-submit")
#
#    def login(self, un, pw):
#        WebDriverWait(self.driver, 10).until(
#            EC.presence_of_element_located((By.ID, "loginform"))
#        )
#        self.form_username_input.send_keys(un)
#        self.form_password_input.send_keys(pw)
#        self.form_login_btn.click()
#        WebDriverWait(self.driver, 10).until(
#            EC.presence_of_element_located((By.CSS_SELECTOR, ".woocommerce-MyAccount-content"))
#        )


class MyAccountPage(BasePage):
    path = '/my-account/'

    @property
    def login_success_msg(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".woocommerce-MyAccount-content").text

    def is_on_page(self):
        if "Hello tester" in self.login_success_msg:
            return True
        else:
            return False

