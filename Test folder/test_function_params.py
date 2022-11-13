import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_GreenKart(BaseTest):

    @pytest.mark.parametrize(
                                "items",
                                [
                                    "cucumber",
                                    "Cauliflower",
                                    "Beetroot"
                                ]
                            )
    def test_global_search(self, items):
        """
        :param : items
        value : cucumber, cauliflower, beetroot
        the script will run thrice. each time with a different item value.
        """
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search for Vegetables and Fruits"]').send_keys(items)