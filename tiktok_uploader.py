"""
TikTok Video Uploader

Automates video upload to TikTok via web interface using Selenium.
Handles iframe navigation, file selection, caption input, and publication.
"""

import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc


import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CHROME_BINARY = os.path.join(BASE_DIR, "chrome", "chrome-win64", "chrome.exe")
CHROMEDRIVER_PATH = os.path.join(BASE_DIR, "chromedriver", "chromedriver.exe")


def upload_to_tiktok(profile, file_dir, index_list, name, chromedriver_path=""):
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
        driver.get("https://www.tiktok.com/")
        time.sleep(4)

        create_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Upload"'))
        )
        create_btn.click()
        print("Clicked create button")

        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )

        ext_name = os.listdir(file_dir)
        if not ext_name:
            print(f"Error: No videos found in {file_dir}")
            return

        video_index = index_list[0]
        if video_index >= len(ext_name):
            print(f"Error: Index {video_index} out of range.")
            return

        file_path = os.path.abspath(os.path.join(file_dir, ext_name[video_index]))
        file_input.send_keys(file_path)
        print(f"Uploading: {ext_name[video_index]}")
        toggle_before_last = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[last()-1]/.."))
        )
        toggle_before_last.click()

        last_toggle = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[last()]/.."))
        )
        last_toggle.click()

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Uploaded')]"))
        )
        
        post_btn = WebDriverWait(driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, "//button[./*[contains(@class, 'Button__content') and contains(text(), 'Post')]]"))
        )
        post_btn.click()

        print("Video Uploaded on TikTok")

        if index_list:
            index_list.pop(0)
        print(f"{name} = {index_list[0] if index_list else 'DONE'}")

    except Exception as e:
        print(f"Upload failed: {e}")

    finally:
        driver.quit()
        print("Browser closed.")
