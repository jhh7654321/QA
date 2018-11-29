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

# Define GundryMD.com base_url: (comes from comman line argument: --testenv=prod) Use (prod, dev, or stage)


class Header(BasePage):
    path = "/"

    def is_on_page(self):
        """Verifies that the hardcoded text "HOME - Gundry MD" appears in page title"""
        return "HOME - Gundry MD" in self.driver.title

    @property
    def logo_link(self):
        return self.driver.find_element(By.ID,"logo")

    @property
    def about_link(self):
        return self.driver.find_element(By.ID, "menu-item-83")

    @property
    def blog_link(self):
        return self.driver.find_element(By.ID, "menu-item-3077")

    @property
    def supplements_link(self):
        return self.driver.find_element(By.ID, "menu-item-244")

    @property
    def skincare_link(self):
        return self.driver.find_element(By.ID, "menu-item-245")

    @property
    def food_link(self):
        return self.driver.find_element(By.ID, "menu-item-128237")

    @property
    def books_link(self):
        return self.driver.find_element(By.ID, "menu-item-129686")

    @property
    def vip_link(self):
        return self.driver.find_element(By.ID, "menu-item-16613")

    @property
    def podcast_link(self):
        return self.driver.find_element(By.ID, "menu-item-147054")

    def click_on_link(self, link):
        link.click()


class HomePage(BasePage):
    path = '/'

    def is_on_page(self):
        """Verifies that the hardcoded text "HOME - Gundry MD" appears in page title"""
        return "HOME - Gundry MD" in self.driver.title

    @property
    def ftc_first_name_input(self):
        return self.driver.find_element(By.ID, "home-ftc-name")

    @property
    def ftc_email_input(self):
        return self.driver.find_element(By.ID, "home-ftc-email")

    @property
    def ftc_signup_btn(self):
        return self.driver.find_element(By.ID, "home-ftc-submit")

    def ftc_signup(self, name, email):
        self.ftc_first_name_input.clear()
        self.ftc_first_name_input.send_keys(name)
        self.ftc_email_input.clear()
        self.ftc_email_input.send_keys(email)
        self.ftc_signup_btn.click()

    def test_contact_page_form(self):
        self.ftc_first_name_input.send_keys("Tester")
        self.ftc_email_input.send_keys("tester@goldenhippo.com")
        self.ftc_signup_btn.click()


class AboutPage(BasePage):
    path = '/gundry-md/'

    def is_on_page(self):
        return "About Gundry MD Supplements and Skincare Products" in self.driver.title


class BlogPage(BasePage):
    path = '/blog/'

    def is_on_page(self):
        return "Blog - Gundry MD" in self.driver.title


class SupplementsPage(BasePage):
    path = '/supplements/'

    def is_on_page(self):
        return "Supplements Archive - Gundry MD" in self.driver.title

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
        return products

    def add_products_to_cart(self):
        for btn in self.product_detail_btns:
            product_detail_page = btn.click()
            time.sleep(1)
            product_detail_page.supplements_link.click()


class ProductDetailPage(BasePage):
    path = ''

    def is_on_page(self):
        return "About Gundry MD Supplements and Skincare Products" in self.driver.title

    @property
    def supplements_link(self):
        return self.driver.find_element(By.LINK_TEXT, "supplements")

    @property
    def price(self):
        price = "$" + (self.driver.find_element(By.CSS_SELECTOR, "p span.cPrice")).text
        return price

    @property
    def quantity_dropdown(self):
        return Select(self.driver.find_element(By.ID, "addtocart"))

    @property
    def quantity_dropdown_food(self):
        return Select(self.driver.find_element(By.ID, "quantity_picker"))

    def select_quantity(self, qty):
        try:
            self.quantity_dropdown.select_by_visible_text(qty)
        except NoSuchElementException:
            self.quantity_dropdown_food.select_by_visible_text(qty)

    @property
    def add_to_cart_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".single-add-to-cart")

    def click_addtocart(self):
        self.add_to_cart_btn.click()


class SkinCarePage(BasePage):
    path = '/skincare/'

    def is_on_page(self):
        return "Skincare Products by GundryMD.com" in self.driver.title

    @property
    def product_titles(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".entry-title")

    def get_products(self):
        products = []
        for title in self.product_titles:
            print(title.text)
            products.append({'title': title.text})
        return products


class FoodPage(BasePage):
    path = '/food2/'

    def is_on_page(self):
        return "Food - Gundry MD" in self.driver.title

    @property
    def product_titles(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "h2.woocommerce-loop-product__title")

    def get_products(self):
        products = []
        for title in self.product_titles:
            print(title.text)
            products.append({'title': title.text})
        return products


class BooksPage(BasePage):
    path = '/books2/'

    def is_on_page(self):
        return "books2 - Gundry MD" in self.driver.title


class VipPage(BasePage):
    path = '/books2/'

    def is_on_page(self):
        return "VIP" in self.driver.title


class FTCPage(BasePage):
    path = '/vitalreds/first_time_customers_offer.php'

    def is_on_page(self):
        """Verifies that the hardcoded text "HOME - Gundry MD" appears in page title"""
        return "Vital Reds - Order Page" in self.driver.title

    @property
    def yes_agree_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#inputy")

    def click_agree_to_vip(self):
        self.yes_agree_input.click()

class ContactPage(BasePage):
    path = '/contact'

    def is_on_page(self):
        """Verifies that the hardcoded text "HOME - Gundry MD" appears in page title"""
        return "Phone, Email, and Mail Contacts for Gundry MD" in self.driver.title

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
    def form_subject_dropdown(self):
        return Select(self.driver.find_element(By.NAME, "your-subject"))

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
