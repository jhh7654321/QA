"""
TODO: Favicon: Try using: <link rel="shortcut icon" href="..."> tag. If you don't find any such tag, try /favicon.ico.
TODO: Copyright year isn't alway caught like here: https://theplantmystery.com/index_fb_m190129A.php?n=fb and http://lawrencesupplements.com/maxrecovery/secureOrder_190205.php or https://nucific.com/lean_tea/intro.php
TODO: Better reporting at the end. Something I can copy and paste into JIRA
TODO: Favicon test broke on this page: https://gundrymd.com/mct_wellness/secure_order1.php
"""

import pytest
import re
import requests
import random
from ..pages.cart_1sc import *
from ..pages.sf_order_page import *


# Settings
BRAND = "whole body research"
PRODUCT_NAME = "Keybiotics"

HAS_CONTINUITY = False
VIDEO_CTA_POP_TIME = 1250  # In seconds
CONTAINER_TYPES = ['bottle', 'jar', 'bag']


PRELANDER_URL = ""
VSL_URL = ""
ORDER_PAGE_URL = "https://wholebodyresearch.com/p_specials/keybiotics_190309.php"

@pytest.fixture
def my_messages():
    errors = "Error!"
    return errors


@pytest.mark.ui
class TestSalesFunnel:

    def test_sales_funnel(self, my_messages, browser):
        my_error = my_messages
        has_errors = False
        base = BasePage(driver=browser)
        cart_page = CartPage(driver=browser)
        order_page = OrderPage(driver=browser)

        # PRELANDER
        if len(PRELANDER_URL):
            browser.get(PRELANDER_URL)
            print("\n")
            print("Prelander Tests:")
            print("Prelander page: " + PRELANDER_URL)
            print("Check <title>:")
            base.check_title(PRODUCT_NAME, BRAND)
            print("   Check Links:")
            base.check_links()
            print("   Check Images:")
            base.check_images()
            print("   Check Favicon:")
            base.check_favicon(PRELANDER_URL)
            print("   Check Console:")
            base.check_console()
            print("   Check Copyright Year")
            base.check_copyright_year()

        # VSL
        if len(VSL_URL):
            browser.get(VSL_URL)
            print("VSL Tests:")
            print("VSL page: " + VSL_URL)
            print("Check <title>:")
            base.check_title(PRODUCT_NAME, BRAND)
            print("   Check Links:")
            base.check_links()
            print("   Check Images:")
            base.check_images()
            print("   Check Favicon:")
            base.check_favicon(VSL_URL)
            print("   Check Console:")
            base.check_console()
            print("   Check Copyright Year")
            base.check_copyright_year()
            # Check Video CTA Pop
            #print("   Check CTA Pop:")
            #base.check_video_cta_pop(VIDEO_CTA_POP_TIME)
            #browser.execute_script("document.getElementsByTagName('video')[0].play()")
            #browser.execute_script('document.getElementsByTagName("video")[0].play()')
            #time.sleep(10)

        # ORDER PAGE
        if len(ORDER_PAGE_URL):
            browser.get(ORDER_PAGE_URL)
            print("Order Page Tests:")
            print("Order page: " + ORDER_PAGE_URL)
            print("Check <title>:")
            base.check_title(PRODUCT_NAME, BRAND)
            print("   Check Links:")
            base.check_links()
            print("   Check Images:")
            base.check_images()
            print("   Check Favicon:")
            base.check_favicon(ORDER_PAGE_URL)
            print("   Check Console:")
            base.check_console()
            print("   Check Copyright Year")
            base.check_copyright_year()
            print("   Check product name and container type in the cart:")
            most_type_found = base.find_container_types(CONTAINER_TYPES).lower()
            if PRODUCT_NAME == "Total Restore":
                cart_links = order_page.get_product_links2()
            else:
                cart_links = base.get_product_links()  # Returns a link_list

            for link in cart_links:
                browser.get(link)
                if PRODUCT_NAME.lower() in cart_page.item_title.text.lower():
                    #print("      Cart URL: " + link + " " + "'" + PRODUCT_NAME + "'" + " found in: " + cart_page.item_title.text)
                    print('      Cart URL: {} "{}" found in "{}" -- OK!'.format(link, PRODUCT_NAME, cart_page.item_title.text))
                else:
                    print('      Cart URL: {} "{}" NOT found in "{}" *** FAIL ***'.format(link, PRODUCT_NAME, cart_page.item_title.text))

                if most_type_found in cart_page.item_title.text.lower():
                    print("      Found: '" + most_type_found + "' in cart item title - OK")
                else:
                    print("      Not Found: '" + most_type_found + "' in cart item title *** WARNING ***")

                time.sleep(3)

            #base.find_container_types(CONTAINER_TYPES)
            time.sleep(3)
        #print(my_messages['errors'])
        #global_data['test_warnings'].update()
        #global_data['test_warnings']
        # Print out Errors:
        #print(global_data['test_warnings'])
        #print(global_data['test_errors'])
        # Print out Warnings:
        #print(ERRORS)
        if has_errors:
            assert False
        else:
            assert True