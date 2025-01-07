# -*- coding: utf-8 -*-
"""
Fetch titles using Google
"""

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import os

# Path to the headless Chrome binary
# CHROME_BINARY_PATH = r"E:\Work here\Research-Quest-AI\ProdResearchQuestAI\Lambda\tmp\bin\chrome-headless-shell-win64\chrome-headless-shell.exe"
CHROME_BINARY_PATH = os.path.join(os.path.dirname(__file__), "tmp", "bin", "chrome-headless-shell-win64", "chrome-headless-shell.exe")

# Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1280x1696')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.binary_location = CHROME_BINARY_PATH


def driver_configuration():
    """
    Initialize the Selenium Chrome WebDriver using the headless Chrome binary.
    """
    return webdriver.Chrome(options=chrome_options)


def fetch_google_titles(keywords, num_papers):
    """
    Fetch titles from Google search results for the given keywords.
    """
    driver = driver_configuration()
    try:
        driver.get("https://www.google.com")
        time.sleep(2)

        # Search for the keywords
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(" ".join(keywords))
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # Parse the results
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        titles = [h3.text.strip() for h3 in soup.select('h3')[:num_papers]]

        # Log the titles
        print("Fetched Titles:")
        for idx, title in enumerate(titles, 1):
            print(f"{idx}. {title}")

        return titles
    except Exception as e:
        print(f"Error fetching titles: {e}")
        return []
    finally:
        driver.quit()


def lambda_handler(event, context):
    """
    AWS Lambda handler function.
    """
    print("Lambda invoked with event:", event)
    try:
        body = event.get('body', {})
        if isinstance(body, str):
            body = json.loads(body)
        
        keywords = body.get("keywords")
        num_papers = body.get("num_papers")
        
        titles = fetch_google_titles(keywords, num_papers)
        return {
            'statusCode': 200,
            'body': {
                "message": "Fetched titles successfully",
                "titles": titles
            }
        }
    except Exception as e:
        print(f"Lambda error: {e}")
        return {
            'statusCode': 500,
            'body': {
                "message": "Failed to fetch titles",
                "error": str(e)
            }
        }
