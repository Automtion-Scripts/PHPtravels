import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()
driver.get("https://phptravels.net/admin/login")
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 10)

def login():
    enter_email = wait.until(EC.presence_of_element_located((By.ID, "email")))
    enter_email.send_keys('admin@phptravels.com')

    password = wait.until (EC.presence_of_element_located((By.NAME,'password')))
    password.send_keys("demoadmin")

    # Remember_me= wait.until (EC.element_to_be_clickable((By.XPATH,'//*[@id="login"]/div/div/div/div[3]/div[1]/div/span')))
    # Remember_me.click()

    login_button = wait.until(EC.element_to_be_clickable((By.ID,'submit')))
    login_button.click()


def activate_user():
    user_menu = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="admin-nav-menu"]/li[6]/button')))
    user_menu.click()

    customers_option = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="users-collapse"]/ul/li[5]/a')))
    customers_option.click()

    # search_user = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="DataTables_Table_0_filter"]/label/input')))
    # search_user.send_keys('Muskaan')

    time.sleep(2)  # Wait for search results to load    

    activate_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="checkedbox"]')))
    activate_button.click()
    print("User activated successfully")


try:
    login()
    print("login successfully")

    activate_user()
    print("User activation process completed")

except Exception as e:
    print ( "failed:", e)

finally:
    time.sleep(7)
    driver.quit()
