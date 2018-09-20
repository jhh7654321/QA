
from selenium import webdriver


def test1():
    driver = webdriver.Chrome()  # Set in PATH
    driver.get('http://staging.newforyou.com/')
    assert driver.title == "HOME - New For You"
    driver.quit()