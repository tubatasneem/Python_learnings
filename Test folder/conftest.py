import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == "chrome":
       web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver= web_driver
    yield
    web_driver.close()