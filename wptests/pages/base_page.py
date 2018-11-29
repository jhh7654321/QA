import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self, base_url):
        url = base_url + self.path
        self.driver.get(url)

    @property
    def form_username_input(self):
        return self.driver.find_element(By.ID, "user_login")

    @property
    def form_password_input(self):
        return self.driver.find_element(By.ID, "user_pass")

    @property
    def form_login_btn(self):
        return self.driver.find_element(By.ID, "wp-submit")

    def login(self, un, pw):
        """ Logs in user with given un and pw, verifies login by checking for wp_logged_in cookie. """
        time.sleep(.5)  # Need to figure out how to remove this.
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginform"))
        )
        self.form_username_input.send_keys(un)
        self.form_password_input.send_keys(pw)
        self.form_login_btn.click()
        cookies = self.driver.get_cookies()  # returns list of dicts
        login_status = False
        for cookie in cookies:
            if 'wordpress_logged_in' in cookie['name']:
                login_status = True
                break
        if login_status:
            return True
        else:
            return False
