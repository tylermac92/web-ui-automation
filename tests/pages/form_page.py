from selenium.webdriver.common.by import By

class FormPage:
    URL = "http://127.0.0.1:5000/form"

    def __init__(self, driver):
        self.driver = driver

    data_input = (By.NAME, "data")
    submit_button = (By.XPATH, "//button[@type='submit']")

    def is_loaded(self):
        return self.driver.current_url == self.URL

    def submit_data(self, data):
        self.driver.find_element(*self.data_input).send_keys(data)
        self.driver.find_element(*self.submit_button).click()