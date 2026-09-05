# Social Media Content Migration Tool

A cross-platform automation tool for content creators to migrate their TikTok videos to YouTube, Instagram, and TikTok.

## Demo

[Watch the demo on YouTube](https://www.youtube.com/watch?v=kBXHZz5jOPg)

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  TikTok Scraper │────▶│ Content Curator │────▶│   Scheduler     │
│  (undetected    │     │(Index + Random  │     │ (Multi-Platform │
│   chromedriver) │     │  State Mgmt)    │     │   Upload)       │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## Components

### 1. TikTok Scraper (`tiktok_scraper.py`)
- Searches TikTok by keyword using `undetected-chromedriver`.
- Extracts video links using BeautifulSoup.
- Downloads videos using `yt-dlp` with anti-bot evasion (sleep intervals, impersonation).
- Handles dynamic JavaScript rendering and anti-bot measures.

### 2. Scheduler (`scheduler.py`)
- Cron-like scheduling with the `schedule` library.
- Optimized posting times per platform (morning, afternoon, evening).
- Multi-account management via separate Chrome profiles.
- Automated index tracking prevents duplicate uploads.

### 3. Multi-Platform Uploaders
- **YouTube** (`youtube_uploader.py`): Automated upload with title, visibility settings, and publication workflow.
- **Instagram** (`instagram_uploader.py`): Reel upload with caption automation.
- **TikTok** (`tiktok_uploader.py`): Iframe handling, caption input, and publication via web interface.

### 4. Direct Migration (`migrate_all.py`)
- Uploads all videos in a folder to a specific platform immediately.
- No scheduling required—instant content migration.

## Tech Stack

- **Python** — core language
- **Selenium + undetected-chromedriver** — browser automation with anti-detection
- **BeautifulSoup** — HTML parsing
- **yt-dlp** — video downloading
- **schedule** — task scheduling

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Paths
Copy config_template.py to config.py and fill in your local paths:

```bash
cp config_template.py config.py
```

Edit config.py with:

Chrome binary path.

Chrome user data directory.

Content directories (cat_videos, dog_videos).

Chrome profile numbers.

### 3. Prepare Chrome Profiles
Create separate Chrome profiles for each account:

Profile 1: Cat videos (YouTube, Instagram, TikTok).

Profile 2: Dog videos (YouTube, Instagram, TikTok).

### 4. Scrape Content
```bash
python tiktok_scraper.py
```

### 5. Run Scheduled Uploads
```bash
python scheduler.py
```

### 6. Run Direct Migration
```bash
python migrate_all.py
```

## Project Structure

```
social-media-content-automation/
├── youtube_uploader.py         # YouTube automation
├── instagram_uploader.py       # Instagram automation
├── tiktok_uploader.py          # TikTok upload automation
├── tiktok_scraper.py           # TikTok scraping & downloading
├── scheduler.py                # Orchestration & timing
├── migrate_all.py              # Direct migration (no scheduling)
├── config_template.py          # Configuration template
├── config.py                   # Your local config (gitignored)
├── requirements.txt
├── .gitignore
├── README.md
├── cat_videos/                 # Cat video files
├── dog_videos/                 # Dog video files
├── chrome/                     # Portable Chrome 126 (gitignored)
└── chromedriver/               # Portable ChromeDriver (gitignored)
```

## Design Decisions
### Duplicate Prevention
Implemented randomized index lists where the used index is popped via pop(). This preserves the original files while ensuring no video is reposted.

### Profile-Based Multi-Account
Each platform account uses a separate Chrome profile, enabling parallel management without manual login switching.

### Anti-Bot Evasion
undetected-chromedriver bypasses bot detection.

yt-dlp sleep intervals (sleep_interval, max_sleep_interval) prevent rate limiting.

cookiefile support for logged-in sessions.

### Direct Migration
Added migrate_all() for immediate uploads without waiting for scheduled times.

### Niches Managed
Cat videos

Dog videos

## Disclaimer
This project was built for educational purposes and personal content management. Respect platform Terms of Service and content creator rights.

## License
MIT License
## Disclaimer
This project was built as a final project for Harvard CS50. It is designed for educational purposes and personal content management. Respect platform Terms of Service and content creator rights.

## License
MIT License
