"""
Social Media Upload Scheduler
"""
from config import (
    CHROME_BINARY,
    CHROMEDRIVER_PATH,
    CHROME_USER_DATA_DIR,
    CAT_VIDEOS,
    DOG_VIDEOS,
    PROFILES,
    INDEX_LISTS,
)
import schedule
import time
import os

from youtube_uploader import upload_to_youtube
from tiktok_uploader import upload_to_tiktok
from instagram_uploader import upload_to_instagram




def setup_schedule():
    # Cat videos - YouTube
    schedule.every().day.at("12:00").do(
        lambda: upload_to_youtube(PROFILES["cat"], CAT_VIDEOS, INDEX_LISTS["cat_2"], "Cat", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("12:15").do(
        lambda: upload_to_youtube(PROFILES["cat"], CAT_VIDEOS, INDEX_LISTS["cat_2"], "Cat", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("12:30").do(
        lambda: upload_to_youtube(PROFILES["cat"], CAT_VIDEOS, INDEX_LISTS["cat_2"], "Cat", CHROMEDRIVER_PATH)
    )

    # Cat videos - Instagram
    schedule.every().day.at("18:00").do(
        lambda: upload_to_instagram(PROFILES["cat"], CAT_VIDEOS, INDEX_LISTS["cat_2"], "Cat", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("18:15").do(
        lambda: upload_to_instagram(PROFILES["cat"], CAT_VIDEOS, INDEX_LISTS["cat_2"], "Cat", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("18:30").do(
        lambda: upload_to_instagram(PROFILES["cat"], CAT_VIDEOS, INDEX_LISTS["cat_2"], "Cat", CHROMEDRIVER_PATH)
    )

    # Cat videos - TikTok
    schedule.every().day.at("10:00").do(
        lambda: upload_to_tiktok(PROFILES["cat"], CAT_VIDEOS, INDEX_LISTS["cat_2"], "Cat", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("10:05").do(
        lambda: upload_to_tiktok(PROFILES["cat"], CAT_VIDEOS, INDEX_LISTS["cat_2"], "Cat", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("10:10").do(
        lambda: upload_to_tiktok(PROFILES["cat"], CAT_VIDEOS, INDEX_LISTS["cat_2"], "Cat", CHROMEDRIVER_PATH)
    )

    # Dog videos - YouTube
    schedule.every().day.at("13:00").do(
        lambda: upload_to_youtube(PROFILES["dog"], DOG_VIDEOS, INDEX_LISTS["dog_2"], "Dog", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("13:15").do(
        lambda: upload_to_youtube(PROFILES["dog"], DOG_VIDEOS, INDEX_LISTS["dog_2"], "Dog", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("13:30").do(
        lambda: upload_to_youtube(PROFILES["dog"], DOG_VIDEOS, INDEX_LISTS["dog_2"], "Dog", CHROMEDRIVER_PATH)
    )

    # Dog videos - Instagram
    schedule.every().day.at("19:00").do(
        lambda: upload_to_instagram(PROFILES["dog"], DOG_VIDEOS, INDEX_LISTS["dog_2"], "Dog", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("19:15").do(
        lambda: upload_to_instagram(PROFILES["dog"], DOG_VIDEOS, INDEX_LISTS["dog_2"], "Dog", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("19:30").do(
        lambda: upload_to_instagram(PROFILES["dog"], DOG_VIDEOS, INDEX_LISTS["dog_2"], "Dog", CHROMEDRIVER_PATH)
    )

    # Dog videos - TikTok
    schedule.every().day.at("11:00").do(
        lambda: upload_to_tiktok(PROFILES["dog"], DOG_VIDEOS, INDEX_LISTS["dog_2"], "Dog", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("11:05").do(
        lambda: upload_to_tiktok(PROFILES["dog"], DOG_VIDEOS, INDEX_LISTS["dog_2"], "Dog", CHROMEDRIVER_PATH)
    )
    schedule.every().day.at("11:10").do(
        lambda: upload_to_tiktok(PROFILES["dog"], DOG_VIDEOS, INDEX_LISTS["dog_2"], "Dog", CHROMEDRIVER_PATH)
    )


def run_scheduler():
    print("Starting scheduler...")
    print("Scheduled jobs:")
    for job in schedule.jobs:
        print(f"  {job}")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    setup_schedule()
    run_scheduler()



