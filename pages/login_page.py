from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "login-email")
        self.password = (By.ID, "password")
        self.submit = (By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[2]/form/button")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.submit).click()
