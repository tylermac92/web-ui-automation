from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    URL = "http://127.0.0.1:5000/dashboard"

    def __init__(self, driver):
        self.driver = driver

    welcome_text = (By.TAG_NAME, "h2")
    form_link = (By.LINK_TEXT, "Data Entry Form")

    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(self.URL))
            return self.driver.current_url == self.URL
        except Exception:
            return False

    def navigate_to_form(self):
        self.driver.find_element(*self.form_link).click()