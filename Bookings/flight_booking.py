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
wait = WebDriverWait(driver, 30)
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

def check_flights():
    """by selecting one way- adding the date and time"""
    flights_menu = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[1]/a')))
    flights_menu.click()

    # Wait for flights form
    wait.until(EC.visibility_of_element_located((By.ID, 'flights-search')))
    print("Flights page loaded successfully")

    # From City (Select2)
    fly_from = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="onereturn"]/div[1]/div/input')))
    fly_from.send_keys("JED")
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='onereturn']/div[1]/div/div/div[1]"))).click()

    # To City (Select2)
    fly_to = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="onereturn"]/div[2]/div[2]/input')))
    fly_to.send_keys("Dubai")
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='onereturn']/div[2]/div[2]/div/div[1]"))).click()

    # Departure Date
    dep_date = wait.until(EC.element_to_be_clickable((By.ID, "departure")))
    driver.execute_script("arguments[0].removeAttribute('readonly')", dep_date)
    dep_date.clear()
    dep_date.send_keys("11-09-2025")  # Example future date

    # Search Flights
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#flights-search")))
    search_button.click()

def book_flight():
    # Select first flight
    first_flight_select = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='flight-list']/li[1]/form/div/div/div/div[2]/div/div/div[1]/button")))
    first_flight_select.click()

    # Wait for booking page
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fadein"]/main/section/div/div[1]/h2')))
    print("Booking page loaded successfully")

    # Fill passenger details (Personal Info)
    wait.until(EC.presence_of_element_located((By.ID, 'p-first-name'))).send_keys("Muskaan")
    wait.until(EC.presence_of_element_located((By.ID, 'p-last-name'))).send_keys("Magure")
    wait.until(EC.presence_of_element_located((By.ID, 'p-email'))).send_keys("muskaan@test.com")
    wait.until(EC.presence_of_element_located((By.ID, 'p-phone'))).send_keys("90099874829")

    # Traveler information
    Select(wait.until(EC.element_to_be_clickable((By.ID, 'title_1')))).select_by_visible_text('Miss')
    wait.until(EC.presence_of_element_located((By.ID, 't-first-name-1'))).send_keys("Muskaan")
    wait.until(EC.presence_of_element_located((By.ID, 't-last-name-1'))).send_keys("Magure")
    Select(wait.until(EC.element_to_be_clickable((By.ID, 't-nationality-1')))).select_by_visible_text('India')
    wait.until(EC.presence_of_element_located((By.ID, 't-email-1'))).send_keys("muskaan@ma.com")
    wait.until(EC.presence_of_element_located((By.ID, 't-phone-1'))).send_keys("90099874829")

    # Agree terms
    wait.until(EC.element_to_be_clickable((By.NAME, 'agree'))).click()

    # Click Book Now
    wait.until(EC.element_to_be_clickable((By.ID, 'booking'))).click()

    # Wait for booking confirmation
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="fadein"]/main/section/div/div[1]/h2')))
    print("Flight booked successfully and confirmation page displayed")

# ------------------------- Execute -------------------------

try:
    enter_the_app()
    login()
    check_flights()
    book_flight()
except Exception as e:
    print("Failed:", e)
finally:
    time.sleep(5)
    driver.quit()
    print("Flight page checked successfully")