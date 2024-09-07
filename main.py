from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = 'LINKEDIN_EMAIL'
ACCOUNT_PASSWORD = 'PASS'
PHONE = 'PHONE'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2F")

email = driver.find_element(By.CSS_SELECTOR, ".mt-24 input")
password = driver.find_element(By.ID, "password")
button = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")


time.sleep(1)
email.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)

button.click()

# driver.get("https://www.linkedin.com/feed/")
# search
job_search = driver.find_element(By.CSS_SELECTOR, "#global-nav-search input")
job_search.send_keys("Python Developer", Keys.ENTER)

# filters
job = driver.find_element(By.CLASS_NAME, ".reusable-search__entity-cluster--quick-filter-action")
job.click()

