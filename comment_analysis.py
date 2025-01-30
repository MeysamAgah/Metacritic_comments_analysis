# imports
## Import functions from other Python files
from scraper import web_driver, scrape_reviews
from clean_data import clean_data
from find_aspects import find_aspects

## web scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

## time
import time
from datetime import datetime

## dealing with dataframe
import pandas as pd
from langdetect import detect #detect language

## avoid viewing warning (optional)
import warnings
warnings.filterwarnings('ignore')

## pre-trained model
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

## data visualization
import matplotlib.pyplot as plt

from collections import defaultdict

def comment_analysis(game_name,
                     aspects,
                     platform,
                     reviewer="user",
                     num_comments=50,
                     user_agent_string = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                     ):
  """
  arguments:
    game_name: string indicating game name for example Baulder's Gate 3
    platform: specify platform of game, for example "playstation-5" default will use default platform of website
    reviewer: type of reviewer e.g. user or critic
    num_comments: integer indicating number of comments to evaluate
    user_agent_string: string indicating user agent of browser
    ...
  output: will be multiple diagrams representing each aspect
  """
  print("model loading...")
  model_name = "yangheng/deberta-v3-base-absa-v1.1"
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForSequenceClassification.from_pretrained(model_name)
  classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
  print("model loaded!")

  print("scraping data...")
  df_comments = scrape_reviews(game_name,
                               platform,
                               reviewer,
                               num_comments,
                               user_agent_string)
  print("data scraped!")

  print("cleaning data...")
  df_comments = clean_data(df_comments)
  df_comments[['positive', 'negative']] = df_comments['review_text'].apply(lambda x: pd.Series(find_aspects(x, aspects)))
  print("data cleaned!")

  # Initialize aspect counts
  aspect_counts = {aspect: {'positive': 0, 'negative': 0} for aspect in aspects}

  # Count positive and negative mentions for each aspect
  for pos, neg in zip(df_comments['positive'], df_comments['negative']):
    if pos:
      for aspect in pos.split(', '):
        if aspect in aspect_counts:
          aspect_counts[aspect]['positive'] += 1
    if neg:
      for aspect in neg.split(', '):
        if aspect in aspect_counts:
          aspect_counts[aspect]['negative'] += 1

  # Prepare data for plotting
  labels = list(aspect_counts.keys())
  positive_counts = [aspect_counts[aspect]['positive'] for aspect in labels]
  negative_counts = [aspect_counts[aspect]['negative'] for aspect in labels]

  # Plotting stacked bar chart
  x = range(len(labels))
  plt.figure(figsize=(12, 6))
  plt.bar(x, positive_counts, color='green', label='Positive')
  plt.bar(x, negative_counts, bottom=positive_counts, color='red', label='Negative')
  plt.xticks(x, labels, rotation=45)
  plt.ylabel('Count')
  plt.title(f'{game_name} last {str(num_comments)} comments from {reviewer}s')
  plt.legend()
  plt.tight_layout()
  plt.show()

  print("Analysis complete!")
