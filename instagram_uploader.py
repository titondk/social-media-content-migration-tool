"""
Instagram Reel Uploader
"""

import os
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from config import (
    CHROME_BINARY,
    CHROMEDRIVER_PATH,
)




def upload_to_instagram(profile, file_dir, index_list, name, chromedriver_path=""):
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
        driver.get("https://www.instagram.com/")
        time.sleep(4)

        create_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='New post']/.."))
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

        for _ in range(2):
            next_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[text()="Next"]'))
            )
            next_btn.click()
            print("Clicked Next")
            time.sleep(2)

        caption = re.sub(r"\.mp4$", "", ext_name[video_index])
        caption_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Write a caption...']"))
        )
        caption_input.click()
        caption_input.send_keys(caption)
        print(f"Added caption: {caption}")

        share_btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@role="button" and @tabindex="0" and text()="Share"]'))
        )
        share_btn.click()
        print("Clicked Share.")

        done_btn = WebDriverWait(driver, 300).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Done']/.."))
        )
        done_btn.click()
        print("Video Uploaded on Instagram")

        if index_list:
            index_list.pop(0)
        print(f"{name} = {index_list[0] if index_list else 'DONE'}")

    except Exception as e:
        print(f"Upload failed: {e}")

    finally:
        driver.quit()
        print("Browser closed.")
