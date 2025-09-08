import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://phptravels.net/?utm_source=chatgpt.com")
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 10)
Cookie_banner = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cookie_disclaimer")))

def enter_the_app():
    customer_button = wait.until (EC.presence_of_element_located((By.XPATH,"//*[@id='navbarSupportedContent']/div[2]/ul/li[4]/a")))
    customer_button.click()

    login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[4]/ul/li[1]/a")))
    login_button.click()

    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'login-title'))).text
    print("entered on the login page")

def login():
    enter_email = wait.until(EC.presence_of_element_located((By.ID, "email")))
    enter_email.send_keys('muskaan@magure.com')

    password = wait.until (EC.presence_of_element_located((By.NAME,'password')))
    password.send_keys("Muskaan@1234")

    # Remember_me= wait.until (EC.element_to_be_clickable((By.XPATH,'//*[@id="login"]/div/div/div/div[3]/div[1]/div/span')))
    # Remember_me.click()
    # wait for cookie banner

    # click accept button inside cookie disclaimer
    Hide_cookie= driver.find_element(By.XPATH, "//*[@id='cookie_stop']")
    Hide_cookie.click()


    login_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login"]/div/div/div/div[4]/div[1]')))
    login_button.click()
    time.sleep(10)

def check_flights():
    flights_menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#navbarSupportedContent > div.nav-item--left.ms-lg-0 > ul > li:nth-child(1) > a')))
    flights_menu.click()

    time.sleep(2)  # Wait for the page to load

    # Verify that the flights page is displayed
    assert wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="fadein"]/main/section/section/div/h2/strong'))).text 
    print("Navigated to the flights page successfully")

    


try:
    enter_the_app()
    print("Entered successfully")
    login()
    print("login successfully")
    check_flights()
    print("Flight page checked successfully")
except Exception as e:
    print ( "failed:", e)

finally:
    time.sleep(7)
    driver.quit()
