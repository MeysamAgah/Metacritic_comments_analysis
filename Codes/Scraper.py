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
