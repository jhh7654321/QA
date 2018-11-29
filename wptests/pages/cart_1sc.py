import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_page import BasePage
from .base_element import BaseElement

# 1SC Shopping Cart Pages


class CartPage(BasePage):
    path = ""

    def is_on_page(self):
        return self.driver.find_element(By.ID, "merchantHeader")

    @property
    def item_qty(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".input-quantity")

    @property
    def item_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".item-title")

    @property
    def item_short_desc(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".item-description")

    @property
    def item_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".cell-price span").text

    @property
    def item_total(self):
        return self.driver.find_element(By.CSS_SELECTOR, "td.cell-total").text

    @property
    def item_remove_btn(self):
        return self.driver.find_element(By.ID, "ctl00_ctl00_mainContent_scPageContent_cartContentsControl_cartItems_ctl01_removeButton")

    @property
    def recalculate_btn(self):
        return self.driver.find_element(By.ID, "ctl00_ctl00_mainContent_scPageContent_recalculateButton")

    @property
    def checkout_btn(self):
        return self.driver.find_element(By.ID, "ctl00_ctl00_mainContent_scPageContent_checkoutButton")

    @property
    def checkout_paypal_btn(self):
        return self.driver.find_element(By.ID, "ctl00_ctl00_mainContent_scPageContent_payPalEcInlineButton")

    @property
    def cart_empty_msg(self):
        return self.driver.find_element(By.ID, "ctl00_ctl00_mainContent_scPageContent_cartContentsControl_infoMessageWrapper")

    def recalculate_cart(self):
        self.recalculate_btn.click()


    def increment_quanity(self):
        qty = self.item_qty.get_attribute('value')
        qty = int(qty) + 1
        self.item_qty.clear()
        self.item_qty.send_keys(str(qty))

    def remove_cart_first_item(self):
        self.item_remove_btn.click()

    def empty_cart(self):
        pass

    @property
    def coupon_code_field(self):
        return self.driver.find_element(
            By.ID, "ctl00_ctl00_mainContent_scPageContent_cartContentsControl_couponEntryControl_couponCodeTextBox")

    @property
    def coupon_apply_btn(self):
        return self.driver.find_element(
            By.ID, "ctl00_ctl00_mainContent_scPageContent_cartContentsControl_couponEntryControl_applyCouponButton")

    @property
    def alert_messages(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#ctl00_ctl00_mainContent_alertList li").text

    def apply_coupon(self, coupon_code):
        self.coupon_code_field.clear()
        self.coupon_code_field.send_keys(coupon_code)
        self.coupon_apply_btn.click()