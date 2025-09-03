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

def enter_the_app():
    customer_button = wait.until (EC.presence_of_element_located((By.XPATH,"//*[@id='navbarSupportedContent']/div[2]/ul/li[4]/a")))
    customer_button.click()

    sign_up_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[4]/ul/li[2]/a/small")))
    sign_up_button.click()

def fill_form():
    """Fill the sign-up form """
    first_name= wait.until(EC.presence_of_element_located((By.NAME, "first_name")))
    first_name.send_keys("Muskaan")

    last_name= wait.until(EC.presence_of_element_located((By.NAME, "last_name")))
    last_name.send_keys("Sahu")

    Country_name = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-light")))
    Country_name.click()

    search_country= wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="signup"]/div/div/div/div[3]/div[1]/div/div/div/div[1]/input')))
    search_country.send_keys("India")

    select_country = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='bs-select-1-99']")))
    select_country.click()

    Phone_number = wait.until(EC.visibility_of_element_located((By.NAME,'phone')))
    Phone_number.send_keys('90099874829')

    email = wait.until (EC.presence_of_element_located((By.NAME,'user_email')))
    email.send_keys("muskaan@magure.com")

    password = wait.until (EC.presence_of_element_located((By.NAME,'password')))
    password.send_keys("Muskaan@1234")

    time.sleep(20)

    # check_box = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'label-container')))
    # check_box.click()

    sign_button = wait.until(EC.element_to_be_clickable((By.ID,'submitBTN')))
    sign_button.click()

try:
    enter_the_app()
    fill_form()
    print ("form filled successfully")
except Exception as e:
    print ("Failed:", e)
finally:
    time.sleep(6)
    driver.quit()