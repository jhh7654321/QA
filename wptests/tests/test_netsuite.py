
"""
TODO: mobile pages (just change screen size? and rerun as parameterization?)
"""
import pytest
import re
import requests
import random
from ..pages.netsuite import *



# SETTINGS


# PAGES



@pytest.mark.ui
class TestNetsuite:

    # Order (READY)
    def test_create_order(self, browser):
        pass

    def test_update_order(self, browser):
        pass

    # Upsell (READY)
    def test_create_upsell(self, browser):
        pass

    def test_update_upsell(self, browser):
        pass

    # Cancel Order
    def test_cancel_order(self, browser):
        pass

    def test_create_coupon(self, browser):
        pass

    def test_create_support_ticket(self, browser):
        pass

    def test_create_subscription(self, browser):
        pass

    def test_update_subscription_frequency(self, browser):
        pass

    # Lead
    def test_create_lead(self, browser):
        pass

    def test_update_lead(self, browser):
        pass

    # Customer
    def test_create_customer(self, browser):
        netsuite_page = NewsuitePage(driver=browser)
        netsuite_page.go(app_config.base_url_netsuite)
        pass

    def test_update_customer(self, browser):
        pass



    # Create subscription

