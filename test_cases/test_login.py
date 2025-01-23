import time
from selenium.webdriver.chrome import webdriver
from pages.login_page import LoginPage
from selenium import webdriver
import pytest
from test_cases.config import driver


class Test_login:

    def test_login_valid(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username("eslam@outlook.com")
        login_page.enter_password("12345678")
        login_page.click_login()
        time.sleep(2)
    def test_login_invalid_username(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username("eslam5875@outlook.com")
        login_page.enter_password("12345678")
        login_page.click_login()
        time.sleep(2)
        login_page.enter_username("eslam@outlook.com")

    def test_login_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username("eslam@outlook.com")
        login_page.enter_password("123456723268")
        login_page.click_login()
        time.sleep(2)

    def test_login_without_data(self, driver):
        login_page = LoginPage(driver)
        login_page.click_login()
        time.sleep(2)
