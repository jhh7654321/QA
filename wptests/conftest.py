from pytest import fixture
from selenium import webdriver

from .config import Config


def pytest_addoption(parser):
    parser.addoption("--env",action="store", help="Environment to run against"),
    parser.addoption("--emulation", action="store", help="mobile or desktop?"),
    parser.addoption("--browserlocation", action="store", help="Local or Browserstack")

@fixture(scope="session")
def emulation(request):
    return request.config.getoption("--emulation")

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
def browser(browserlocation, emulation):  # Had: browserlocation
    # function will give you a browser for each test.
    # session will give you one browser for all tests.
    # Settings for Browserstack. Use tool to change: https://www.browserstack.com/automate/python
    mobile_emulation = {"deviceName": "iPhone 6 Plus"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
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
    if emulation == 'mobile':
        browser = webdriver.Chrome(chrome_options=chrome_options)
    else:
        browser = webdriver.Chrome()
    yield browser
    # Teardown

    #app_config.close()
    #env.close()
    browser.quit()  # Required by browserstack to close, otherwise a timeout occurs.
    try:
        browser.close()
    except:
        this = 'that' # Getting resource warnings here when I don't use this try / except here. Odd... just using quit() or close(), or both close() and quit() together in either combination give the resource error.



