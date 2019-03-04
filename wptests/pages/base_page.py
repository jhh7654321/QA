from datetime import datetime
import operator
import re
import requests
import time
from urllib.parse import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver


    @property
    def links(self):
        try:
            links = self.driver.find_elements(By.XPATH, "//a[@href]")
            return links
        except:
            links = ""
            return links

    def find_container_types(self, container_types):
        """ Looks at page source and counts the container types, returns the type that is most found """
        type_count = {}
        page_source = self.driver.page_source
        for type in container_types:
            count = len(re.findall(type, page_source, re.I))
            type_count[type] = count
        #print("      Type counts: " + str(type_count))
        most_type_found = max(type_count.items(), key=operator.itemgetter(1))[0]
        return most_type_found


    # NEW TCR CART (May put this in seperate page file)

    @property
    def first_name(self):
        return self.driver.find_element(By.NAME, "firstName")

    @property
    def last_name(self):
        return self.driver.find_element(By.NAME, "lastName")

    @property
    def phone(self):
        return self.driver.find_element(By.NAME, "phone")

    @property
    def email(self):
        return self.driver.find_element(By.NAME, "email")

    @property
    def email_confirm(self):
        return self.driver.find_element(By.NAME, "emailConfirm")

    @property
    def address(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#address-autocomplete input")

    @property
    def address2(self):
        return self.driver.find_element(By.NAME, "addBillAddress")

    @property
    def city(self):
        return self.driver.find_element(By.NAME, "city")

    @property
    def zip(self):
        return self.driver.find_element(By.NAME, "zipPostalCode")

    @property
    def state(self):
        return self.driver.find_element(By.NAME, "state")

    @property
    def name_on_card(self):
        return self.driver.find_element(By.NAME, "nameOnCard")

    @property
    def card_type(self):
        return self.driver.find_element(By.NAME, "typeOfCard")

    @property
    def card_num(self):
        return self.driver.find_element(By.NAME, "card")

    @property
    def exp_month(self):
        return self.driver.find_element(By.NAME, "expmonth")

    @property
    def exp_year(self):
        return self.driver.find_element(By.NAME, "expyear")

    @property
    def cvv2(self):
        return self.driver.find_element(By.NAME, "cardccv")

    @property
    def submit_order_btn(self):
        return self.driver.find_element(By.ID, "submit-btn")

    @property
    def paypal_btn(self):
        return self.driver.find_element(By.ID, "paypal-button")

    # UPSELLS and DOWNSELLS

    @property
    def upsell_yes_btn(self):
        return self.driver.find_element(By.CLASS_NAME, "orange-button")

    @property
    def upsell_no_btn(self):
        return self.driver.find_element(By.CLASS_NAME, "gray-button")

    @property
    def downsell_1_yes_btn(self):
        return self.driver.find_element(By.ID, "")

    @property
    def downsell_1_no_btn(self):
        return self.driver.find_element(By.ID, "")

    @property
    def upsell_2_yes_btn(self):
        return self.driver.find_element(By.ID, "")

    @property
    def upsell_2_no_btn(self):
        return self.driver.find_element(By.ID, "")

    @property
    def downsell_2_yes_btn(self):
        return self.driver.find_element(By.ID, "")

    @property
    def downselll_2_no_btn(self):
        return self.driver.find_element(By.ID, "")

    @property
    def upsell_3_yes_btn(self):
        return self.driver.find_element(By.ID, "")

    @property
    def upsell_3_no_btn(self):
        return self.driver.find_element(By.ID, "")

    @property
    def downsell_3_yes_btn(self):
        return self.driver.find_element(By.ID, "")

    @property
    def downsell_3_no_btn(self):
        return self.driver.find_element(By.ID, "")

    def upsell_click_yes_btn(self):
        self.upsell_yes_btn.click()

    def upsell_click_no_btn(self):
        self.upsell_no_btn.click()

    @property
    def autocomplete(self):
        return self.driver.find_element(By.CLASS_NAME, "autocomplete")

    def fill_in_form(self, pay_by, fname, lname, phone, email, address, address2, city, zip, state,
                     name_on_card, card_type, card_num, exp_month, exp_year, cvv2):
        time.sleep(2)  # NEED TO REMOVE
        self.first_name.send_keys(fname)
        self.last_name.send_keys(lname)
        self.phone.send_keys(phone)
        self.email.send_keys(email)
        self.email_confirm.send_keys(email)
        self.address.send_keys("3840 Lindsey Court, Newbury Park")
        self.autocomplete.click()
        self.address2.send_keys(address2)
        self.city.send_keys(city)
        self.zip.send_keys(zip)
        select_state = Select(self.state)
        select_state.select_by_visible_text(state)
        if pay_by == "cc":
            self.name_on_card.send_keys(name_on_card)
            select_card_type = Select(self.card_type)
            select_card_type.select_by_visible_text(card_type)
            self.card_num.send_keys(card_num)
            select_month = Select(self.exp_month)
            select_month.select_by_visible_text(exp_month)
            select_year = Select(self.exp_year)
            select_year.select_by_visible_text(exp_year)
            self.cvv2.send_keys(cvv2)

    def submit_order_by_cc(self):
        self.submit_order_btn.click()

    def submit_order_by_paypal(self):
        print("clicked on Paypal")
        self.paypal_btn.click()

        # select by value
        # select.select_by_value('1')


    @property
    def images(self):
        return self.driver.find_elements(By.XPATH, "//img[@src]")

    @property
    def favicon(self):
        try:
            favicon = self.driver.find_element(By.XPATH, "//link[@type='image/x-icon']")
        except:
            favicon = ""
        return favicon


    def find_and_compare_phone_number(self, phone_number):
        pass


    def check_links(self):
        if len(self.links):
            for link in self.links:
                try:
                    r = requests.get(link.get_attribute("href"))
                    if r.status_code == 404:
                        status_msg = "*** FAIL ***"
                    else:
                        status_msg = "OK"
                    print('      The link: "{}" with the URL: {} = {} - {}'.format(link.get_attribute("innerText"), link.get_attribute("href"), str(r.status_code), status_msg))
                    r.close()
                except requests.RequestException:
                    #print(link.get_attribute("innerText"))
                    print('      URL: {} = BAD URL - WARNING'.format(link.get_attribute("innerText")))
        else:
            print("      No Links found.")

    def check_images(self):
        for image in self.images:
            img_src = image.get_attribute("src")
            #print(img_src)
            #match = re.compile(r"(.+)googleads(.+)" ).match(img_src)
            #if match:
            #    print("Found Googleleads")
            #else:
            #    print("NOT Found Googleleads")
            #
            status_msg = ""
            img_size = 0
            try:
                r = requests.get(image.get_attribute("src"))
            except:
                print(img_src)
                status_msg = " something went wrong *** WARNING ***"
            if r.status_code == 404:
                status_msg = "*** FAIL ***"
            else:
                status_msg = "OK"
            if r.status_code == 200:
                img_size = int(r.headers['Content-length'])
                if img_size  > 200000:
                    status_msg = status_msg + " *** FAIL *** Image Size > 200kb "
                else:
                    status_msg = "OK"
            #print('      URL: {} = {} - {}'.format(image.get_attribute("src"), str(r.status_code), status_msg))
            #print('      URL: {} = {} - Size: {} - {}'.img_src, str(r.status_code), img_size, status_msg)
            print("       URL: " + img_src + " = " + str(r.status_code) + " - Size: " + str(img_size) + " - " + status_msg)
            r.close()
    def check_favicon(self, url_to_parse):
        """
        Checks that favicon.ico is sitting at the base of the URL
        """
        parsed_uri = urlparse(url_to_parse)
        base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        favicon_locations = ["favicon.ico","favicon.png","images/www_favicon.jpg"]
        for location in favicon_locations:
            favicon_url = base_url + location
            r = requests.get(favicon_url)
            if r.status_code == 200:
                status_msg = "OK"
                break
            else:
                status_msg = "*** FAIL ***"
        print('      URL: {} = {} - {}'.format(favicon_url, str(r.status_code), status_msg))
        r.close()

    def check_title(self, product_name, brand):
        title = self.driver.title
        if product_name.lower() in title.lower():
            print("      " + product_name + " was found in <title>" + self.driver.title + "</title> - OK")
        else:
            print("      WARNING: '" + product_name + "' was NOT found in the <title>" + self.driver.title + "</title> *** FAIL ***")
        if brand.lower() in title.lower():
            print("      '" + brand + "' was found in <title>" + self.driver.title + "</title> - OK")
        else:
            print("      WARNING: " + brand + " was NOT found in the <title>" + self.driver.title + "</title> *** FAIL ***")

    @property
    def copyright_text(self):
        try:
            text = self.driver.find_element(By.XPATH, "//*[contains(text(), '©')]").get_attribute("innerText").rstrip()
        except:
            text = ""
        return text


    def check_copyright_year(self):
        currentYear = datetime.now().year
        # pattern = re.compile(r"(?:©|\(c\)|copyright\b)\s*" + str(currentYear) + "(.+)")  (.+)2019.+
        pattern = re.compile(r"(.+" + str(currentYear) + ".+)")
        #page_content = self.driver.find_element(By.XPATH, "//*[contains(text(), '©')]").text
        page_content = self.copyright_text
        #print([page_content])
        match = pattern.match(page_content)
        #match = pattern.match("© 2018")
        if match:
            print("   Found in: " + page_content + " - OK")
        else:
            print("   NOT FOUND: " + page_content + " - *** FAIL ***")


    def check_console(self):
        console_logs = self.driver.get_log('browser')
        print("      Len of log: " + str(len(console_logs)))
        for log in console_logs:
            print(log)

    def check_video_cta_pop(self, cta_pop_time):
        print("Gonna be cool!")
        print("Time to pop: " + str(cta_pop_time))
        #self.driver.execute_script("document.getElementsByTagName('video')[0].play()")
        #time.sleep(10)


    def get_product_links(self):
        links = self.links
        link_list = []
        for link in links:
            # Get the value of the attribute ahref
            url = link.get_attribute("href")
            if 'pid=' in url:
                url = url + "&bn=2"
                link_list.append(url)
                #print("URL to parse: " + url)
        return link_list

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

