
"""
TODO:
"""
import pytest
import re
import requests
from random import randint
from ..pages.cart_1sc import *
from ..pages.sf_order_page import *


# Order Page Settings
ORDER_CONT = False
QUANTITY = 1  # 1,3,6

# Checkout Settings
TEST_NUM = "b"
FNAME = "testload" + TEST_NUM
LNAME = "testerload" + TEST_NUM
PHONE = "8885559999"  # + TEST_NUM
EMAIL = FNAME + str(randint(10000, 99999)) + LNAME + ".com"
ADDRESS = "3840 Lindsey Court"
ADDRESS2 = "Suite 101"
ZIP = "91320"
CITY = "Newbury Park"
STATE = "California"

# Pay by
PAY_BY = "cc" # cc = credit card or pp = paypal

# Paypal credentials
PP_USERNAME = ""
PP_PASSWORD = ""

# Credit Card Info
NAME_ON_CARD = FNAME + " " + LNAME
CARD_TYPE = "Visa"
CARD_NUM = "4111111111111111"
EXP_MONTH = "05"
EXP_YEAR = "2021"
CVV2 = "123"

# Upsells and downsells
UP1 = True
DN1 = False
UP2 = False
DN2 = False
UP3 = False
DN3 = False


# PAGES


PRELANDER_URL = "https://uat-f-gundry-md.herokuapp.com/1btotalrestoreland1/"  #
VSL_URL = "https://uat-f-gundry-md.herokuapp.com/1btotalrestoresel1"  #
ASSESSMENT_URL = "https://uat-f-gundry-md.herokuapp.com/1btotalrestorequiz1/"
ORDER_PAGE_URL = "https://uat-f-gundry-md.herokuapp.com/1btotalrestoresel1"  #



@pytest.mark.ui
class TestOrder:

    #@pytest.mark.parametrize("email", [''])
    def test_tcr_create_order(self, browser):
        has_errors = False
        base = BasePage(driver=browser)
        #cart_page = CartPage_TCR(driver=browser)
        order_page = OrderPage(driver=browser)
        browser.get(ORDER_PAGE_URL)
        print("Gonna order some subscriptions!")
        print("How much?: " + str(QUANTITY))
        if ORDER_CONT:
            order_page.select_yes_checkbox()
        order_page.select_quantity(QUANTITY)
        order_page.add_to_cart()
        email = "tester" + str(randint(10000, 99999)) + "@tester.com"
        base.fill_in_form(
            PAY_BY, FNAME, LNAME, PHONE, email, ADDRESS, ADDRESS2, CITY, ZIP, STATE,
            NAME_ON_CARD, CARD_TYPE, CARD_NUM, EXP_MONTH, EXP_YEAR, CVV2)
        if PAY_BY == "cc":
            print("paying by CC")
            #base.submit_order_by_cc()
        if PAY_BY == "pp":
            print("paying by PP")
            base.submit_order_by_paypal()
        # Purchase Upsells
        #if UP1:
        #    base.click_yes_btn()
        #else:
        #    base.click_no_btn()
        #if DN1:
        #    base.click_yes_btn()
        #else:
        #    base.click_no_btn()
        #if UP1:
        #    base.click_yes_btn()
        #else:
        #    base.click_no_btn()


        time.sleep(5)

        if has_errors:
            assert False
        else:
            assert True