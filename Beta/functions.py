def scrape_reviews(game_name, platform, reviewer="user", num_comments=50):
  """
  arguments:
    game_name: string indicating game name for example Baulder's Gate 3
    platform: specify platform of game, for example "playstation-5" default will use default platform of website
    reviewer: type of reviewer e.g. user or critic
    num_comments: integer indicating number of comments to evaluate
    ...
  output: will be a dataframe:
    df: represents dataframe of desired reviews
      columns are: reviewer, review_text, score, review_date, platform
  """
  driver = web_driver() #initializing webscrapping
  
  url = f"https://www.metacritic.com/game/{game_name}/{reviewer}-reviews/?platform={platform}" # forming up url according to inputs
  driver.get(url) # loading html of url
  time.sleep(5) # Wait for initial page load

  review_texts = []
  reviewers = []
  review_dates = []
  ratings = []
  platforms = []

  prev_height = driver.execute_script("return document.body.scrollHeight")
  scroll_pause_time = 10

  while len(review_texts) < num_comments:
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)  # Allow time for content to load

    # Check for new height after scrolling
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == prev_height:  # Stop if no more content to load
      no_more_scroll_count += 1
      if no_more_scroll_count >= 2:  # Stop after two consecutive no-scroll detections
        break
    else:
      no_more_scroll_count = 0  # Reset counter if scroll happened
    prev_height = new_height

    # Extract data after scrolling (partial extraction each loop)
    full_review = driver.find_elements(By.CLASS_NAME, "c-siteReview")
    for e in full_review:
      if len(review_texts) >= num_comments:
        break  # Stop collecting if num_comments reached

      try:
        review_texts.append(e.find_element(By.CLASS_NAME, "c-siteReview_quote").text)
        reviewers.append(e.find_element(By.CLASS_NAME, "c-siteReviewHeader_username").text)
        review_dates.append(datetime.strptime(e.find_element(By.CLASS_NAME, "c-siteReviewHeader_reviewDate").text, "%b %d, %Y").date())
        ratings.append(e.find_element(By.CLASS_NAME, "c-siteReviewHeader_reviewScore").text)
        platforms.append(e.find_element(By.CLASS_NAME, "c-siteReview_platform").text)
      except Exception as ex:
        print(f"Error extracting review data: {ex}")

  # Close the browser
  driver.quit()
  
  #forming up a dataframe for output
  df = pd.DataFrame(
      {
          'reviewer': reviewers,
          'review_text': review_texts,
          'rating': ratings,
          'review_date': review_dates,
          'platform': platforms
      }
  )

  return df
