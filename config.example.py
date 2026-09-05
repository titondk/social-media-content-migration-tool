"""
Configuration file for the Social Media Content Automation Pipeline.
Copy this file to config.py and fill in your local paths and settings.
Do NOT commit config.py to version control (it is gitignored).
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# CHROME PATHS (Update these)
# ============================================================

CHROME_BINARY = os.path.join(BASE_DIR, "chrome", "chrome-win64", "chrome.exe")
CHROMEDRIVER_PATH = os.path.join(BASE_DIR, "chromedriver", "chromedriver.exe")
CHROME_USER_DATA_DIR = r"C:\Users\YOUR_USERNAME\AppData\Local\Google\Chrome for Testing\User Data"

# ============================================================
# CONTENT DIRECTORIES
# ============================================================

CAT_VIDEOS = os.path.join(BASE_DIR, "cat_videos")
DOG_VIDEOS = os.path.join(BASE_DIR, "dog_videos")

# ============================================================
# PROFILES (Update these)
# ============================================================

PROFILES = {
    "cat": "1",
    "dog": "2",
}

# ============================================================
# INDEX LISTS
# ============================================================

INDEX_LISTS = {
    "cat_2": [0, 1, 2],
    "dog_2": [0, 1, 2],
}

# ============================================================
# YT-DLP OPTIONS
# ============================================================

DOWNLOAD_DIR = os.path.join(BASE_DIR, "creator_content")

YTDL_OPTS = {
    'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
    'quiet': True,
    'no_warnings': True,
    'sleep_interval': 3,
    'max_sleep_interval': 5,
    'sleep_requests': 1,
    'ignoreerrors': True,
    'extract_flat': 'in_playlist',
    'cookiefile': None,
}
