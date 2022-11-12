import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver
    yield
    ch_driver.close()

@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome:
    pass

class Test_Google(Base_Chrome):

    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
