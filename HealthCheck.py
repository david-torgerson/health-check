# Import Libraries
from selenium import webdriver
import time

# Define Variables
username = 'USERNAME_GOES_HERE'
password = 'PASSWORD_GOES_HERE'

# Start Chrome Instance
driver = webdriver.Chrome(executable_path = "CHROMEDRIVER_FILE_PATH_GOES_HERE")
driver.get('https://go.nd.edu/healthchecks')
time.sleep(2)

# Login Redirect
login_button = driver.find_element_by_xpath('//*[@id="root"]/main/div[3]/div/div/button')
login_button.click()
time.sleep(2)

# Switch to Login Tab
driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)
 
# Input Username and Password
username_box = driver.find_element_by_xpath('//*[@id="okta-signin-username"]')
username_box.send_keys(username)
password_box = driver.find_element_by_xpath('//*[@id="okta-signin-password"]')
password_box.send_keys(password)
signin_button = driver.find_element_by_xpath('//*[@id="okta-signin-submit"]')
signin_button.click()
time.sleep(2)

# Prepare for Okta Authentication
push_button = driver.find_element_by_xpath('//*[@id="form74"]/div[2]/input')
push_button.click()
time.sleep(2)

# Refocus Tab and Check Position
driver.switch_to_window(driver.window_handles[0])
run_time = time.time() + (60 * 3)
while time.time() < run_time:
    if len(driver.window_handles) == 1:
        break
time.sleep(3)

# Navigate to Check In Page
checkin_button = driver.find_element_by_xpath('//*[@id="root"]/main/div/div[2]/div[1]/a')
checkin_button.click()
time.sleep(2)

# Submit Health Check
submit_button = driver.find_element_by_xpath('//*[@id="root"]/main/div/div[29]/div/button')
submit_button.click()
time.sleep(5)

# Quit Session
driver.quit()