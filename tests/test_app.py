import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage
from tests.pages.form_page import FormPage

@pytest.fixture(scope="module")
def driver():
    # Set up Chrome WebDriver
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run headless if desired
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_login_and_navigation(driver):
    # Instantiate page objects
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    form_page = FormPage(driver)

    # Navigate to Login page and log in with correct credentials
    login_page.load()
    login_page.login("testuser", "password123")

    # Verify that we landed on the Dashboard page
    assert dashboard_page.is_loaded(), "Dashboard did not load as expected."

    # Navigate to the Data Entry Form via dashboard link
    dashboard_page.navigate_to_form()
    assert form_page.is_loaded(), "Data Entry Form page did not load."

    # Submit data via the form and check if we get redirected back to the dashboard
    form_page.submit_data("Hello World")
    # A simple check is that the URL is now the dashboard URL
    assert dashboard_page.is_loaded(), "After submitting form, dashboard did not load."

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    # Use invalid credentials
    login_page.login("invalid", "user")
    # Verify that we are still on the login page due to invalid credentials
    assert driver.current_url == LoginPage.URL, "Should remain on login page with invalid credentials."