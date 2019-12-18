from selenium import webdriver
from source.utilities import globals
from source.utilities.properties import ReadConfig


def start_browser(browser_name, url):
    driver = None
    if browser_name == "Chrome" or browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=globals.CHROME_PATH)
    elif browser_name == "Firefox" or browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=globals.FIREFOX_PATH)

    driver.implicitly_wait(ReadConfig.get_implicit_wait())
    driver.maximize_window()
    driver.get(url)

    return driver
