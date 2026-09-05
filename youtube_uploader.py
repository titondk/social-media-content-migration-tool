"""
YouTube Video Uploader (Portable Chrome 126)
"""

import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from config import (
    CHROME_BINARY,
    CHROMEDRIVER_PATH,
    CHROME_USER_DATA_DIR,
    CAT_VIDEOS,
    DOG_VIDEOS,
    PROFILES,
    INDEX_LISTS,
)



def upload_to_youtube(profile, file_dir, index_list, name, chromedriver_path=""):
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
        driver.get("https://www.youtube.com/")
        time.sleep(3)

        create_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Create']"))
        )
        create_btn.click()
        print("Clicked Create button.")

        upload_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/upload']"))
        )
        upload_option.click()
        print("Clicked Upload Video option.")

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

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK"))
        )
        driver.find_element(By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK").click()
        print("Set 'Not made for kids'.")

        for i in range(3):
            next_btn = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.ID, "next-button"))
            )
            next_btn.click()
            print(f"Clicked Next ({i+1}/3)")

        public_radio = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-radio-button[contains(@name, 'PUBLIC')]"))
        )
        public_radio.click()
        print("Set visibility to Public.")

        publish_btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Publish"]'))
        )
        publish_btn.click()
        print("Published successfully!")

        print("Waiting for upload to complete...")

        WebDriverWait(driver, 420).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Upload complete ... Processing will begin shortly')]"))
        )
        print(" Upload confirmed! Checks passed.")

        if index_list:
            index_list.pop(0)
        print(f"{name} = {index_list[0] if index_list else 'DONE'}")

    except Exception as e:
        print(f"Upload failed: {e}")

    finally:
        driver.quit()
        print("Browser closed.")
