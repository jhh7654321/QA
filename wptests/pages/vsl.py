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


class VSLPage(BasePage):
    path = '/'

    def is_on_page(self):
        return "" in self.driver.title

    @property
    def video(self):
        return self.driver.find_element(By.TAG_NAME, "video")

    @property
    def cta_btn(self):
        try:
            cta_btn = self.driver.find_element(By.LINK_TEXT, "NEXT STEP")
        except:
            cta_btn = self.driver.find_element(By.LINK_TEXT, "Next Step")
        return cta_btn

    def click_on_cta_btn(self):
        self.cta_btn.click()
