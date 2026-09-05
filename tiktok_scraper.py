"""
TikTok Video Scraper

Scrapes trending TikTok videos by niche/keyword, extracts metadata,
and downloads videos for content curation and redistribution.

Uses undetected-chromedriver to bypass anti-bot measures and
BeautifulSoup for HTML parsing.
"""
from scheduler import cats
import yt_dlp
import re
import time
import requests
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from undetected_chromedriver import Chrome
from config import YTDL_OPTS

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



#helper function
def is_video_link(tag):
    if tag.name == 'a' and tag.get('href'):
        return '/video/' in tag.get('href')
    return False


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CHROME_BINARY = os.path.join(BASE_DIR, "chrome", "chrome-win64", "chrome.exe")
CHROMEDRIVER_PATH = os.path.join(BASE_DIR, "chromedriver", "chromedriver.exe")




def scrape_tiktok(profile):
    videos_links = []
    options = uc.ChromeOptions()
    options.headless = False

    options.binary_location = CHROME_BINARY
    options.add_argument(f"--profile-directory=Profile {profile}")
    options.add_argument("--user-data-dir={CHROME_USER_DATA_DIR}")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')

    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = uc.Chrome(
        options=options,
        service=service,
        version_main=126,
        browser_executable_path=CHROME_BINARY
    )

    try:
        driver.get("https://www.tiktok.com/search?q=Cat%20Video&t=1788414713803")
        #Scroling part 
        #used send keys method because the javascript injection method doesnt work no more 
        body = driver.find_element(By.TAG_NAME, 'body')
        body.click()  # Focus the page
        for _ in range(10):  # Press down arrow 10 times
            body.send_keys(Keys.PAGE_DOWN)

            time.sleep(2)  # Wait for new videos to load

        #scrape part 
        # Parse the page (AFTER scrolling is done)
        soup = BeautifulSoup(driver.page_source, "html.parser")
    
        # Extract video links (INSIDE this function, but AFTER soup is created)
        video_links = soup.find_all(is_video_link)
        print(f"Found {len(video_links)} video links.")

        # Loop through the links to extract URLs
        for link in video_links:
            video_url = link.get('href')
            videos_links.append(link.get('href'))
            print(video_url)

    finally:
        driver.quit()
        print("Browser closed.")
        return videos_links

def download_tiktok(links):
    ydl = yt_dlp.YoutubeDL(YTDL_OPTS)
    ydl.download(links)


download_tiktok(scrape_tiktok('1'))
