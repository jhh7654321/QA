import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .base_element import BaseElement
from .cart_1sc import *


class OrderPage(BasePage):
    path = "/"

    def is_on_page(self):
        return True

    @property
    def add_to_cart_btn(self):
        return self.driver.find_element(By.CLASS_NAME, "add-to-cart-btn")

    @property
    def quantity_btn_a(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.choose-bottles-container div:nth-child(3)")  # Need id="opt-a"

    @property
    def quantity_btn_b(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.choose-bottles-container div:nth-child(2)")  # Need id="opt-b"

    @property
    def quantity_btn_c(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.choose-bottles-container div:nth-child(1)")  # Need id="opt-c"

    @property
    def yes_check_box(self):
        return self.driver.find_element(By.CLASS_NAME, "checkbox")


    def select_yes_checkbox(self):
        self.yes_check_box.click()

    def select_quantity(self, quantity):
        if quantity == 1:
            self.quantity_btn_a.click()
        if quantity == 3:
            self.quantity_btn_b.click()
        if quantity == 6:
            self.quantity_btn_c.click()

    def add_to_cart(self):
        self.add_to_cart_btn.click()

    def get_product_links2(self):
        # NEED a check for MOBILE HERE

        link_list = []
        # click on button a
        self.quantity_btn_a.click()
        time.sleep(1)
        url = self.add_to_cart_btn.get_attribute("href")
        url = url + "&bn=2"
        link_list.append(url)
        # click on button b
        self.quantity_btn_b.click()
        time.sleep(1)
        url = self.add_to_cart_btn.get_attribute("href")
        url = url + "&bn=2"
        link_list.append(url)
        # click on button C
        self.quantity_btn_c.click()
        time.sleep(1)
        url = self.add_to_cart_btn.get_attribute("href")
        url = url + "&bn=2"
        link_list.append(url)
        return link_list