import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://phptravels.net/?utm_source=chatgpt.com")
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 60)
actions = ActionChains(driver)

# Accept cookie banner if present
try:
    hide_cookie = wait.until(EC.element_to_be_clickable((By.ID, "cookie_stop")))
    hide_cookie.click()
except:
    pass

# ------------------------- Functions -------------------------

def enter_the_app():
    customer_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[4]/a")))
    customer_button.click()

    login_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[4]/ul/li[1]/a")))
    login_button.click()

    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-title'))).text
    print("Entered login page successfully")

def login():
    enter_email = wait.until(EC.presence_of_element_located((By.ID, "email")))
    enter_email.send_keys('user@phptravels.com')  # Dummy demo creds

    password = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    password.send_keys("demouser")

    login_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="login"]/div/div/div/div[4]/div[1]')))
    login_button.click()
    
    # Wait for dashboard/homepage after login
    wait.until(EC.visibility_of_element_located((By.ID, 'fadein')))
    print("Logged in successfully")
   
def check_Hotels():
    hotels_menu = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="navbarSupportedContent"]/div[1]/ul/li[1]/a')))
    hotels_menu.click()
    time.sleep(2)  # Let the Hotels page load

    # Verify Hotels page
    assert wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="fadein"]/main/section[1]/section/div/h2/strong'))).text 
    print("Navigated to the Hotels page successfully")

    # Step 1: Click the city dropdown
    city_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select2-hotels_city-container")))
    city_dropdown.click()

    # Step 2: Enter city name in the search input
    city_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "select2-search__field")))
    city_input.send_keys("Dubai")

    # Step 3: Select the first result
    first_result = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="select2-hotels_city-results"]/li')))
    first_result.click()

    # Step 4: Enter check-in and check-out dates
    check_in_date = wait.until(EC.element_to_be_clickable((By.ID,'checkin'))) 
    check_in_date.clear()
    check_in_date.send_keys("19-11-2025")

    check_out_date = wait.until(EC.element_to_be_clickable((By.ID,'checkout'))) 
    check_out_date.clear()
    check_out_date.send_keys("20-11-2025")

    # Step 5: Click search
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='hotels-search']/div/div[5]/button")))
    search_button.click()

    time.sleep(7)
    print("Hotel search results displayed successfully")



try:
    enter_the_app()
    print("Entered successfully")
    login()
    print("login successfully")
    check_Hotels()
    print("Hotel page checked successfully")
except Exception as e:
    print ( "failed:", e)

finally:
    time.sleep(7)
    driver.quit()
