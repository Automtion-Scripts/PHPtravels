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

def check_flights():
    flights_menu = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[1]/a')))
    flights_menu.click()

    # Wait for flights form
    wait.until(EC.visibility_of_element_located((By.ID, 'flights-search')))
    print("Flights page loaded successfully")

    """featured flights search"""

    click_oneway = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='myTabContent4']/div/div/div/div/div[1]/a")))
    actions.move_to_element(click_oneway).click().perform() 

    # Wait for results
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='fadein']/main/section/div[1]/div[1]/div[2]/h4")))
    print("Flight search results displayed successfully")

    time.sleep(7)  # Allow time to view results

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

def book_flight():
    # Select first flight
    first_flight_select = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='flight-list']/li[1]/form/div/div/div/div[2]/div/div/div[1]/button")
    ))
    first_flight_select.click()

    # Wait for booking page
    booking_header = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="fadein"]/main/section/div/div[1]/h2'))
    )
    print("Booking page loaded successfully")

    # Traveler information
    Select(wait.until(EC.element_to_be_clickable((By.ID, 'title_1')))).select_by_visible_text("Miss")

    # First Name
    first_name = wait.until(EC.presence_of_element_located((By.ID, 't-first-name-1')))
    driver.execute_script("arguments[0].scrollIntoView(true);", first_name)
    first_name.send_keys("Muskaan")

    # Last Name
    last_name = wait.until(EC.presence_of_element_located((By.ID, 't-last-name-1')))
    last_name.send_keys("Magure")

    # Nationality
    Select(wait.until(EC.element_to_be_clickable((By.ID, 't-nationality-1')))).select_by_visible_text("India")

    # Email
    wait.until(EC.presence_of_element_located((By.ID, 't-email-1'))).send_keys("muskaan@ma.com")

    # Phone
    wait.until(EC.presence_of_element_located((By.ID, 't-phone-1'))).send_keys("90099874829")

    # Agree to terms
    wait.until(EC.element_to_be_clickable((By.NAME, 'agree'))).click()

    # Book Now
    wait.until(EC.element_to_be_clickable((By.ID, 'booking'))).click()

    # Confirmation
    confirmation_header = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="fadein"]/main/section/div/div[1]/h2'))
    )
    print("✅ Flight booked successfully and confirmation page displayed:", confirmation_header.text)


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