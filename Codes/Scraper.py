# installs
!pip install selenium
!apt-get install chromium-driver

# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import pandas as pd

user_agent_string = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'

def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f"user-agent={user_agent_string}")
    driver = webdriver.Chrome(options=options)
    return driver

driver = web_driver()
url = 'https://www.metacritic.com/game/elden-ring/user-reviews/?platform=playstation-5'
driver.get(url)
time.sleep(5)  # Wait for initial page load

reviews = []
users = []
dates = []
ratings = []
platforms = []

prev_height = driver.execute_script("return document.body.scrollHeight")
scroll_pause_time = 10

while True:
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)  # Allow time for content to load

    # Check for new height after scrolling
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == prev_height:  # Stop if no more content to load
        break
    prev_height = new_height

# Extract data after all scrolling is complete
full_review = driver.find_elements(By.CLASS_NAME, "c-siteReview")
for e in full_review:
    reviews.append(e.find_element(By.CLASS_NAME, "c-siteReview_quote").text)
    users.append(e.find_element(By.CLASS_NAME, "c-siteReviewHeader_username").text)
    dates.append(datetime.strptime(e.find_element(By.CLASS_NAME, "c-siteReviewHeader_reviewDate").text, "%b %d, %Y").date())
    ratings.append(e.find_element(By.CLASS_NAME, "c-siteReviewHeader_reviewScore").text)
    platforms.append(e.find_element(By.CLASS_NAME, "c-siteReview_platform").text)

driver.quit()
