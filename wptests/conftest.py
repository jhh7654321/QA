from pytest import fixture
from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from .config import Config


def pytest_addoption(parser):
    parser.addoption("--env",action="store", help="Environment to run against"),
    parser.addoption("--browserlocation", action="store", help="Local or Browserstack")

@fixture(scope="session")
def browserlocation(request):
    return request.config.getoption("--browserlocation")

@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@fixture(scope="session")
def app_config(env):
    cfg = Config(env)
    return cfg

@fixture(scope="function")
def browser(browserlocation):  # Had: browserlocation
    # function will give you a browser for each test.
    # session will give you one browser for all tests.
    # Settings for Browserstack. Use tool to change: https://www.browserstack.com/automate/python
    desired_cap = {
        'browser': 'Chrome',
        'browser_version': '62.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '1024x768'
    }
    if browserlocation == 'bs':
        browser = webdriver.Remote(
            command_executor='http://developer372:C1EzDHLAwmW3chVsYZq7@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)
    else:
        browser = webdriver.Chrome()
    yield browser
    # Teardown
    #browser.close()
    browser.quit()  # Required by browserstack to close, otherwise a timeout occurs.
