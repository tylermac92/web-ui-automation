from selenium.webdriver.common.by import By

class LoginPage:
    URL = "http://127.0.0.1:5000/login"

    def __init__(self, driver):
        self.driver = driver

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.XPATH, "//li[contains(., 'Error')]")

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()