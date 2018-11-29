import pytest
import random
import time

from ..products.all_vsls import ALL_VSLS
from ..pages.base_page import BasePage
from ..pages.vsl import VSLPage
from ..pages.base_element import BaseElement

VSL_TO_TEST = [('https://onetwocosmetics.com/presentation/vanish/index181115A.php?n=email', 'One Two Cosmetics | One Two Vanish', '725')]

class TestVSL:  # Must start with 'Test...'
    """ VSL TESTS"""

    #@pytest.mark.parametrize( "site, title", random.sample(ALL_VSLS, 1)) #RANDOM
    @pytest.mark.parametrize("site, title, btn_time", VSL_TO_TEST) # SINGLE VSL
    #@pytest.mark.parametrize("site, title", ALL_VSLS) # ALL VSLS
    def test_vsl_existence(self, browser, site, title, btn_time):
        vsl_page = VSLPage(driver=browser)
        vsl_page.go(site)
        assert browser.title == title

    #@pytest.mark.parametrize("site, title, btn_time", VSL_TO_TEST)  # SINGLE VSL
    @pytest.mark.parametrize("site, title, btn_time", ALL_VSLS)  # SINGLE VSL
    def test_video_cta_pop(self, browser, site, title, btn_time):
        vsl_page = VSLPage(driver=browser)
        vsl_page.go(site)
        time.sleep(3) # Remove and replace with implicit wait
        browser.execute_script("document.getElementsByTagName('video')[0].pause();")
        time.sleep(1)
        browser.execute_script("document.getElementsByTagName('video')[0].currentTime += " + btn_time + ";")
        browser.execute_script("document.getElementsByTagName('video')[0].play();")
        time.sleep(5) # Change out for wait for
        assert vsl_page.cta_btn
        vsl_page.click_on_cta_btn()


"""
Tests: 
Video:
Video auto starts?
Check for CTA pop
Turn on Audio by button?

Page Tests:
Test page <TITLE></TITLE>
Check for console errors
Check for duplicate pixels?
Goes to correct order page
Other links 
Broken images / Links
privacy policy / terms
Copyright date is up to date
Check for Supplements Facts - YES
Pricing - YES if price is known
Check Math - Yes

Shopping Cart: 
Quantity
Product
Price
Promo Code works
Test Order Page goes through
Check SKU is correct Number (1Shopping Cart)
Only one upsell attached
Check for continuity

Mobile Redirects

Player controls:
See: https://www.w3.org/2010/05/video/mediaevents.html

document.getElementsByTagName('video')[0].pause()
document.getElementsByTagName('video')[0].play()
document.getElementsByTagName('video')[0].currentTime
document.getElementsByTagName('video')[0].currentTime=500
document.getElementsByTagName('video')[0].currentSrc
document.getElementsByTagName('video')[0].duration
document.getElementsByTagName('video')[0].muted
document.getElementsByTagName('video')[0].playbackRate=10

"""
