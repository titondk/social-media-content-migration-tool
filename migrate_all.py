from youtube_uploader import upload_to_youtube
from instagram_uploader import upload_to_instagram
from tiktok_uploader import upload_to_tiktok


def migrate_all(profile, folder_path, upload_queue, platform, label):
    """
    Migrate all videos in a folder to a specific platform immediately.
    """
    if platform == "youtube":
        upload_func = upload_to_youtube
    elif platform == "instagram":
        upload_func = upload_to_instagram
    elif platform == "tiktok":
        upload_func = upload_to_tiktok
    else:
        print(f"Error: Unknown platform '{platform}'")
        return
    
    # As long as there are videos in the queue, keep uploading
    while upload_queue:
        print(f"Remaining videos: {len(upload_queue)}")
        upload_func(profile, folder_path, upload_queue, label, "")
    
    print(f"All videos migrated to {platform}.")