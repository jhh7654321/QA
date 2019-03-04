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
        return "Maggie Q and Dr. de Mello present ActivatedYou" in self.driver.title

    @property
    def logo_link(self):
        return self.driver.find_element(By.CSS_SELECTOR,".logo_container a")

    @property
    def home_link(self):
        return self.driver.find_element(By.ID, "menu-item-133096")

    @property
    def about_link(self):
        return self.driver.find_element(By.ID, "menu-item-716")

    @property
    def shop_link(self):
        return self.driver.find_element(By.ID, "menu-item-552")

    @property
    def blog_link(self):
        return self.driver.find_element(By.ID, "menu-item-848")

    @property
    def contact_link(self):
        return self.driver.find_element(By.ID, "menu-item-132913")

    @property
    def cart_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#menu-item-132915 a")

    def click_on_link(self, link):
        link.click()


class HomePage(BasePage):
    path = '/'

    def is_on_page(self):
        """Verifies that the hardcoded text "HOME - Gundry MD" appears in page title"""
        return "Maggie Q and Dr. de Mello present ActivatedYou" in self.driver.title

    def test_contact_page_form(self):
        self.ftc_first_name_input.send_keys("Tester")
        self.ftc_email_input.send_keys("tester@goldenhippo.com")
        self.ftc_signup_btn.click()


class AboutPage(BasePage):
    path = '/about/'

    def is_on_page(self):
        return "About - ActivatedYou" in self.driver.title


class BlogPage(BasePage):
    path = '/blog/'

    def is_on_page(self):
        return "Blog - ActivatedYou" in self.driver.title


class ShopPage(BasePage):
    path = '/product/'

    def is_on_page(self):
        return "ActivatedYou | Products" in self.driver.title

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


class FTCPage(BasePage):
    path = '/first-time-customer-vip/'

    def is_on_page(self):
        """Verifies that the hardcoded text "HOME - Gundry MD" appears in page title"""
        return "First Time Customer VIP - Gundry MD" in self.driver.title

    @property
    def page_titles(self):
        titles_list =  self.driver.find_elements(By.CSS_SELECTOR, "div.et_pb_text_inner h1")
        title_string = []
        for title in titles_list:
            title_string.append(title.text)
        return title_string

    @property
    def yes_agree_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#inputy")

    def click_agree_to_vip(self):
        self.yes_agree_input.click()

class ContactPage(BasePage):
    path = '/contact'

    def is_on_page(self):
        return "Contact - ActivatedYou" in self.driver.title

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


class PrelanderPage(BasePage):
    path = ''

    def is_on_page(self):
        """Verifies that the hardcoded text "HOME - Gundry MD" appears in page title"""
        return "Gundry MD" in self.driver.title
