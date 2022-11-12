import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")


def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == "Google"