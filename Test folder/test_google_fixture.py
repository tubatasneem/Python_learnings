import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-------------------setup method----------------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")

    yield
    print("-------------------teardown-------------------------")
    driver.quit()

# this is way where we pass the fixture as a parameter to the function
# def test_google_title(init_driver):
#     assert driver.title == "Google11"


#this is a way where we use  usefixture decorater to use the fixture
@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"