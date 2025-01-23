import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.implicitly_wait(10)
    login_page = LoginPage(driver)
    login_page.open_page("https://cms-mojo.chips.care/login")
    # login_page.enter_username("eslam@outlook.com")
    # login_page.enter_password("12345678")
    # login_page.click_login()
    yield driver
    driver.close()
    driver.quit()
