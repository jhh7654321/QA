import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .base_element import BaseElement
from .cart_1sc import *


class BotTestPage(BasePage):
    path = "/3harmfulfoods/orderbiox4chatbot.php"

    def is_on_page(self):
        return "3 Harmful Foods" in self.driver.title

    @property
    def chatbot_container(self):
        return self.driver.find_element(By.ID, "mck-sidebox")

    @property
    def chatbot_message_input(self):
        return self.driver.find_element(By.ID, "mck-autosuggest-search-input")

    @property
    def chatbot_start_icon(self):
        return self.driver.find_element(By.ID, "mck-sidebox-launcher")

    def chatbot_open(self):
        #WebDriverWait(self.driver, 15).until((EC.presence_of_element_located(By.ID, 'mck-sidebox-launcher')))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "mck-sidebox-launcher"))
        )
        self.chatbot_start_icon.click()

    def chatbot_send_message(self, message):
        self.chatbot_message_input.send_keys(message)


class Header(BasePage):
    path = "/"

    def is_on_page(self):
        return "Nucific | Nucific Bio X4" in self.driver.title

    @property
    def logo_link(self):
        return self.driver.find_element(By.ID,"logo")

    @property
    def about_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu .menu-item-2682")

    @property
    def about_sub_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu li.menu-item-2759")

    @property
    def blog_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu li.menu-item-3246")

    @property
    def products_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu li.menu-item-2687 a")

    @property
    def products_sub_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu li.menu-item-2689")

    @property
    def contact_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu li.menu-item-2685")

    @property
    def cart_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu .menu-item-2721")

    def click_on_link(self, link):
        link.click()


class HomePage(BasePage):
    path = '/'

    def is_on_page(self):
        """Verifies that the hardcoded text "HOME - Gundry MD" appears in page title"""
        return "Nucific | Nucific Bio X4" in self.driver.title

    @property
    def ftc_first_name_input(self):
        return self.driver.find_element(By.ID, "home-ftc-name")

    @property
    def ftc_email_input(self):
        return self.driver.find_element(By.ID, "home-ftc-email")

    @property
    def ftc_signup_btn(self):
        return self.driver.find_element(By.ID, "home-ftc-submit")

    def ftc_signup(self):
        self.ftc_first_name_input.send_keys("Tester")
        self.ftc_email_input.send_keys("tester@goldenhippo.com")
        self.ftc_signup_btn.click()

    def test_contact_page_form(self):
        self.ftc_first_name_input.send_keys("Tester")
        self.ftc_email_input.send_keys("tester@goldenhippo.com")
        self.ftc_signup_btn.click()


class AboutPage(BasePage):
    path = '/about/'

    def is_on_page(self):
        return "Nucific About Us | About Nucific | Nucific About Dr. Amy Lee" in self.driver.title


class BlogPage(BasePage):
    path = '/blog/'

    def is_on_page(self):
        return "Blog for Nucific.com" in self.driver.title


class ProductsPage(BasePage):
    path = '/products/'

    def is_on_page(self):
        return "Products - Nucific | Nucific Products | Nucific Supplements" in self.driver.title

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
        return self.driver.find_element(By.CSS_SELECTOR, "div.product-section div.product")

    #@property
    #def price(self):
    #    price = "$" + (self.driver.find_element(By.CSS_SELECTOR, "p span.cPrice")).text
    #    return price

    def select_quantity(self, qty):
        radio_btn = self.driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='" + qty + "']")
        price = self.driver.find_element(By.XPATH, "//input[@type='radio'][@value='" + qty + "']/parent::label").text
        price = ''.join(re.findall('(?:[\$\€]{1}[,\d]+.?\d*)',price))
        radio_btn.click()
        return price

    @property
    def add_to_cart_btn(self):
        return self.driver.find_element(By.ID, "ctaButton")

    def click_addtocart(self):
        self.add_to_cart_btn.click()


class SkinCarePage(BasePage):
    path = '/skincare/'

    def is_on_page(self):
        return "" in self.driver.title


class FoodPage(BasePage):
    path = '/food/'

    def is_on_page(self):
        return "" in self.driver.title


class BooksPage(BasePage):
    path = '/books2/'

    def is_on_page(self):
        return "" in self.driver.title


class FTCPage(BasePage):
    path = '/vitalreds/first_time_customers_offer.php'

    def is_on_page(self):
        return "Vital Reds - Order Page" in self.driver.title

    @property
    def yes_agree_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#inputy")

    def click_agree_to_vip(self):
        self.yes_agree_input.click()

class ContactPage(BasePage):
    path = '/contact/'

    def is_on_page(self):
        return "Contact - Nucific | Nucific Customer Service | support@nucific.com" in self.driver.title

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
