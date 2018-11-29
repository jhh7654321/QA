import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .base_element import BaseElement

# WooCommerce Shopping Cart


class CartPage(BasePage):
    path = None

    def is_on_page(self):
        return "Cart - One Two Cosmetics" in self.driver.title

    @property
    def item_qty(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".quantity input")

    @property
    def item_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".product-name a")

    @property
    def item_short_desc(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'tr.woocommerce-cart-form__cart-item.cart_item td.product-name')))
        return self.driver.find_element(By.CSS_SELECTOR, "tr.woocommerce-cart-form__cart-item.cart_item td.product-name")

    @property
    def item_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, "td.product-subtotal").text.replace(" ", "")

    @property
    def item_total(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".product-subtotal span").text

    @property
    def item_remove_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a.remove")

    @property
    def recalculate_btn(self):
        return self.driver.find_element(By.NAME, "update_cart")

    @property
    def checkout_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR , " div a.checkout-button")

    @property
    def checkout_amazon_pay_btn(self):
        return self.driver.find_element(By.ID, "OffAmazonPaymentsWidgets0")

    @property
    def cart_empty_msg(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".cart-empty")

    def recalculate_cart(self):
        self.recalculate_btn.click()

    def increment_quanity(self):
        qty = self.item_qty.get_attribute('value')
        qty = int(qty) + 1
        self.item_qty.clear()
        self.item_qty.send_keys(str(qty))

    def remove_cart_first_item(self):
        self.item_remove_btn.click()
        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-empty'), "Your cart is currently empty."))

    def empty_cart(self):
        pass
