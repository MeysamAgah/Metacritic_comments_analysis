# imports
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

import matplotlib.pyplot as plt
from collections import defaultdict

from scraper import web_driver, scrape_reviews
from clean_data import clean_data
from find_aspects import find_aspects
from comment_analysis import comment_analysis

if __name__ == "__main__":
    # Example inputs
    game_name = input("Enter the game name: ")
    platform = input("Enter the platform (e.g., playstation-5): ")
    aspects = input("Enter aspects to analyze (comma-separated): ").split(", ")
    reviewer = input("Enter reviewer type (user/critic): ") or "user"
    num_comments = int(input("Enter number of comments to analyze: ") or 50)
    user_agent_string = input("Enter user agent string (press Enter for default): ") or \
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

    # Run analysis
    comment_analysis(game_name, aspects, platform, reviewer, num_comments, user_agent_string )
