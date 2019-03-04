import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .base_element import BaseElement

# Define NetSuite

class NewsuitePage(BasePage):
    path = ""

    def is_on_page(self):
        """Verifies that the hardcoded text "HOME - Gundry MD" appears in page title"""
        return "NetSuite" in self.driver.title

    @property
    def logo_link(self):
        return self.driver.find_element(By.ID,"logo")
