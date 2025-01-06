!pip install selenium
!apt-get install chromium-driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

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


quotes = []
while True:
    # Scroll to the bottom of the page
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    sleep(2)  # Sleep to allow time for content to load

    # Find all <div> elements with the class name 'c-siteReview_quote'
    quote_divs = driver.find_elements(By.CLASS_NAME, 'c-siteReview_quote')
    
    # Extract text from each <span>
    new_quotes = []
    for div in quote_divs:
        try:
            span_text = div.find_element(By.TAG_NAME, 'span').text
            if span_text not in quotes:
                new_quotes.append(span_text)
        except NoSuchElementException:
            pass

    # If no new quotes are found, assume end of comments
    if not new_quotes:
        break
    quotes.extend(new_quotes)

# Print all extracted quotes
for i, quote in enumerate(quotes, start=1):
    print(f"Quote {i}: {quote}")

# Close the WebDriver
driver.quit()
