from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

def test_login_valid():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    lp = LoginPage(driver)
    lp.open()
    lp.login("user@phptravels.com", "demouser")
    assert "dashboard" in driver.current_url.lower()
    driver.quit()
