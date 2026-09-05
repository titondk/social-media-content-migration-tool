# Social Media Content Automation Pipeline

End-to-end content operations system that identifies trending TikTok videos by niche, curates them, and automates distribution across YouTube, Instagram, and TikTok with scheduled posting and duplicate prevention.

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

### 1. TikTok Scraper (`scraper/tiktok_scraper.py`)
- Searches TikTok by niche/keyword using `undetected-chromedriver`
- Extracts video metadata: views, engagement, hashtags, creator
- Downloads top-performing videos via ssstik.io API integration
- Handles dynamic JavaScript rendering and anti-bot measures
- Filters by minimum view threshold (e.g., >1M views)

### 2. Content Curator (`utils/helpers.py`)
- Randomized index-based selection prevents duplicate uploads
- Emoji removal and title sanitization for cross-platform compatibility
- Filename cleaning to prevent filesystem errors
- State tracking across multiple accounts and niches

### 3. Multi-Platform Uploader
- **YouTube** (`uploader/youtube_uploader.py`): Automated upload with title, visibility settings, and publication workflow
- **TikTok** (`uploader/tiktok_uploader.py`): iframe handling, caption input, and publication via web interface
- **Instagram** (`uploader/instagram_uploader.py`): Reel upload with caption automation

### 4. Scheduler (`scheduler/scheduler.py`)
- Cron-like scheduling with `schedule` library
- Optimized posting times per platform (morning, afternoon, evening)
- Multi-account parallel management via Chrome profile separation
- Automated index tracking to prevent reposts

## Tech Stack
- **Python** — core language
- **Selenium + undetected-chromedriver** — browser automation with anti-detection
- **BeautifulSoup** — HTML parsing and metadata extraction
- **requests** — API integration (ssstik.io download endpoint)
- **pynput** — keyboard automation for file dialogs
- **schedule** — task automation and timing

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Paths
```bash
cp config/config.example.py config/config.py
```
Edit `config/config.py` with your local paths:
- Chrome user data directory
- Content directories for each niche
- Chrome profile numbers for each account
- Chromedriver path (optional)

### 3. Prepare Chrome Profiles
Create separate Chrome profiles for each platform account:
- YouTube account → Profile 8
- TikTok Account 1 (Oshi No Ko) → Profile 6
- TikTok Account 2 (Chainsaw Man) → Profile 7
- TikTok Account 3 (Demon Slayer) → Profile 9

### 4. Scrape Content
```bash
python scraper/tiktok_scraper.py
```

### 5. Start Scheduled Uploads
```bash
python scheduler/scheduler.py
```

## Project Structure
```
social-media-content-automation/
├── config/
│   ├── config.example.py      # Configuration template
│   └── config.py              # Your local config (gitignored)
├── scraper/
│   └── tiktok_scraper.py      # Trend scraping & download
├── uploader/
│   ├── youtube_uploader.py    # YouTube automation
│   ├── tiktok_uploader.py     # TikTok automation
│   └── instagram_uploader.py  # Instagram automation
├── scheduler/
│   └── scheduler.py           # Orchestration & timing
├── utils/
│   └── helpers.py             # Text processing & sanitization
├── requirements.txt
├── .gitignore
└── README.md
```

## Design Decisions

### Duplicate Prevention
Initially considered deleting uploaded videos from the directory. Instead, implemented randomized index lists where the used index is popped via `pop()`. This preserves the original files while ensuring no video is reposted.

### Emoji Handling
Cross-platform keyboard encoding limitations required removing emojis from titles. Titles remain clear and informative without emoji characters.

### Profile-Based Multi-Account
Each platform account uses a separate Chrome profile, enabling parallel management without manual login switching.

### Randomized Scheduling
Index lists are pre-shuffled to introduce variety in upload sequences, preventing identical content from being posted simultaneously across platforms.

## Niches Managed
- **Oshi No Ko** — Anime content
- **Chainsaw Man** — Anime content
- **Demon Slayer** — Anime content

## Disclaimer
This project was built as a final project for Harvard CS50. It is designed for educational purposes and personal content management. Respect platform Terms of Service and content creator rights.

## License
MIT License
