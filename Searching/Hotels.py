import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://phptravels.net/?utm_source=chatgpt.com")
driver.maximize_window()


# options = webdriver.ChromeOptions()
# prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
# options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(options=options)

# Explicit wait
wait = WebDriverWait(driver, 20)
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
    time.sleep(20)

    

def check_Hotels():
    hotels_menu = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/a')))
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
    print("Flight page checked successfully")
except Exception as e:
    print ( "failed:", e)

finally:
    time.sleep(7)
    driver.quit()
