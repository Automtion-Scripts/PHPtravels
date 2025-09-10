from selenium.webdriver.common.by import By

class LoginPage:
    # Locators
    EMAIL = (By.ID, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.ID, "submitBTN")  # simpler than full XPath

    def __init__(self, driver, base_url="https://phptravels.net"):
        self.driver = driver
        self.base_url = base_url.rstrip("/")

    def open(self):
        """Open the login page"""
        self.driver.get(f"{self.base_url}/login")

    def login(self, email: str, password: str):
        """Perform login using given credentials"""
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys(email)

        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

        self.driver.find_element(*self.SUBMIT).click()
