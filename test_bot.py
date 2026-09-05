import os
from scheduler import PROFILES, INDEX_LISTS, CHROMEDRIVER_PATH, cats, dogs
from youtube_uploader import upload_to_youtube
from instagram_uploader import upload_to_instagram
from tiktok_uploader import upload_to_tiktok

niche = "cat"
platform = "tiktok"  
profile = PROFILES[niche]


if niche == "cat":
    folder = cats
else:
    folder = dogs

index_list = INDEX_LISTS[f"{niche}_2"]

print(f"Testing {platform} for {niche}...")
print(f"Video index to upload: {index_list[0]}")

if platform == "youtube":
    upload_to_youtube(profile, folder, index_list, "TestRun", CHROMEDRIVER_PATH)
elif platform == "instagram":
    upload_to_instagram(profile, folder, index_list, "TestRun", CHROMEDRIVER_PATH)
else:
    upload_to_tiktok(profile, folder, index_list, "TestRun", CHROMEDRIVER_PATH)

print("Done!")