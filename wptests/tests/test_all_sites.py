import pytest
import random
import time

from ..products.all_sites import ALL_SITES
from ..pages.base_page import BasePage
from ..pages.base_element import BaseElement


class AllPages(BasePage):
    path = ""

    def is_on_page(self):
        """Verifies the page title, so we know we're on the right page. """
        return "" in self.driver.title

    @property
    def page_title(self):
        return self.driver.title


class TestAllSites:  # Must start with 'Test...'
    """ Tests for All Sites"""

    #@pytest.mark.parametrize( "site, title", random.sample(ALL_SITES, 1))
    #@pytest.mark.parametrize("site, title", [
    #    ('http://bevhillsmd.com/csc/indexOB2.php', 'Beverly Hills MD: Crepe Correction | Video'),
    #    ('http://thenewgutfix.com/leaky-gut-fix_181017A_m.php', 'Gundry MD - Is There A Solution For Leaky Gut?')
    #])
    @pytest.mark.parametrize("site, title", ALL_SITES)
    def test_site_existence(self, browser, site, title):
        """ Quick test to know the home mpage is accessable. """
        #site_title_list = []
        home_page = AllPages(driver=browser)
        home_page.go(site)
        time.sleep(10)
        # Use below to create a site, title list.
        #f = open("output.txts", "a+")
        #f.write("('" + site + "', '" + home_page.page_title + "'),\n")
        #f.close()
        #print("('" + site + "', '" + home_page.page_title + "'),")
        assert home_page.page_title == title
        #time.sleep(5)

