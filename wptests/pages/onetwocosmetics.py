import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from .base_page import BasePage
from .base_element import BaseElement
#from .cart_wc import *
from .cart_1sc import *

class Header(BasePage):
    path = "/"

    def is_on_page(self):
        return "Home - One Two Cosmetics" in self.driver.title

    @property
    def logo_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".logo_container a")

    @property
    def shop_link(self):
        return self.driver.find_element(By.ID, "menu-item-458339")

    @property
    def shop_classic_sub_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "ul.sub-menu li.menu-item-260966")

    @property
    def shop_advanced_sub_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "ul.sub-menu li.menu-item-260967")

    @property
    def how_to_apply_link(self):
        return self.driver.find_element(By.ID, "menu-item-461865")

    @property
    def howto_classic_sub_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "ul.sub-menu li.menu-item-264230")

    @property
    def howto_advanced_sub_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu ul.sub-menu li.menu-item-264228")

    @property
    def otc_difference_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu li.menu-item-143582")

    @property
    def blog_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu li.menu-item-423506")

    @property
    def press_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu li.menu-item-12436")

    @property
    def our_story_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu li.menu-item-12435")

    @property
    def login_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#top-menu li.menu-item-423066")

    @property
    def cart_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a.et-cart-info")

    def hover_over_link(self, link):
        hover = ActionChains(self.driver).move_to_element(link)
        hover.perform()

    def click_on_link(self, link):
        link.click()


class HomePage(BasePage):
    path = '/'

    def is_on_page(self):
        return "Home - One Two Cosmetics" in self.driver.title

    def test_contact_page_form(self):
        self.ftc_first_name_input.send_keys("Tester")
        self.ftc_email_input.send_keys("tester@goldenhippo.com")
        self.ftc_signup_btn.click()

class OurStoryPage(BasePage):
    path = '/our-story/'

    def is_on_page(self):
        return "Our Story - One Two Cosmetics" in self.driver.title


class BlogPage(BasePage):
    path = '/blog/'

    def is_on_page(self):
        return "Blog - One Two Cosmetics" in self.driver.title


class PressPage(BasePage):
    path = '/press/'

    def is_on_page(self):
        return "Press - One Two Cosmetics" in self.driver.title


class ShopPage(BasePage):
    path = '/shop/'

    def is_on_page(self):
        return "Shop | One Two Cosmetics" in self.driver.title

    @property
    def product_titles(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"h5")

    @property
    def product_detail_btns(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "a.button-dark")

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


class ShopAdvancedCollectionPage(BasePage):
    path = '/advanced-collection/'

    def is_on_page(self):
        return "Advanced Collection - One Two Cosmetics" in self.driver.title


class HowTwoClassicPage(BasePage):
    path = '/how-two/'

    def is_on_page(self):
        return "How Two - One Two Cosmetics" in self.driver.title


class HowToApplyPage(BasePage):
    path = '/howto/'

    def is_on_page(self):
        return "Choose your How To - One Two Cosmetics" in self.driver.title


class TheOTCDifferencePage(BasePage):
    path = '/the-otc-difference/'

    def is_on_page(self):
        return "The OTC Difference - One Two Cosmetics" in self.driver.title


class ProductDetailPage(BasePage):
    path = ''

    def is_on_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, "et_pb_text_inner")

    @property
    def supplements_link(self):
        return self.driver.find_element(By.LINK_TEXT, "supplements")

    @property
    def price(self):
        time.sleep(.5)
        #price = self.driver.find_element(By.CSS_SELECTOR, ".et_pb_text_inner .selected-set-price").text
        price = self.driver.find_element(By.CSS_SELECTOR, "span.selected-set-price1").text  # BLACK FRIDAY
        return price

    @property
    def quantity_dropdown_advanced(self):
        return Select(self.driver.find_element(By.ID, "product-selector"))

    @property
    def quantity_dropdown_black_friday(self):
        return Select(self.driver.find_element(By.ID, "product-set2"))

    @property
    def quantity_dropdown_classic(self):
        return Select(self.driver.find_element(By.ID, "product-set"))

    def select_quantity(self, qty):
        try:
            self.quantity_dropdown_black_friday.select_by_visible_text(qty)
            #self.quantity_dropdown_classic.select_by_visible_text(qty)
        except:
            self.quantity_dropdown_advanced.select_by_visible_text(qty)

    #@property
    #def add_to_cart_classic_btn(self):
    #    return self.driver.find_element(By.LINK_TEXT, "ADD TO CART")  # BLACK FRIDAY
    #    #return self.driver.find_element(By.CSS_SELECTOR, ".et_pb_text_inner input.button-dark")

    @property
    def add_to_cart_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a.productLink")

    def click_addtocart(self):
        #try:
        #    self.add_to_cart_classic_btn.click()
        #except:
        self.add_to_cart_btn.click()


class LoginPage(BasePage):
    path = '/my-account/'

    def is_on_page(self):
        return "My Account - One Two Cosmetics" in self.driver.title


class ContactPage(BasePage):
    path = '/contact'

    def is_on_page(self):
        return "" in self.driver.title

    # Contact Form

    @property
    def form_first_name_input(self):
        return self.driver.find_element(By.ID, "et_pb_contact_first_name_1")

    @property
    def form_last_name_input(self):
        return self.driver.find_element(By.ID, "et_pb_contact_last_name_1")

    @property
    def form_email_input(self):
        return self.driver.find_element(By.ID, "et_pb_contact_email_1")

    @property
    def form_subject_dropdown(self):
        return Select(self.driver.find_element(By.ID, "et_pb_contact_subject_1"))

    @property
    def form_message_textarea(self):
        return self.driver.find_element(By.ID, "et_pb_contact_message_1")

    @property
    def form_submit_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button.et_pb_contact_submit")

    @property
    def form_success_msg(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".et-pb-contact-message p").text

    def form_submit(self):
        self.form_first_name_input.send_keys("Test")
        self.form_last_name_input.send_keys("Tester")
        self.form_email_input.send_keys("tester1@goldenhippo.com")
        self.form_subject_dropdown.select_by_visible_text("7. Other")
        self.form_message_textarea.send_keys("TESTING... Please ignore.")
        self.form_submit_btn.click()
        # The form takes a few seconds to send so I've added a wait here until I see the message.
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.et-pb-contact-message p'), "Your message was sent successfully. One of our Lash Experts will get back to you within 48 hours. Love and Lashes."))
