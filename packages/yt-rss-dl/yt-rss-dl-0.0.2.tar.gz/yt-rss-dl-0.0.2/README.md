# yt-rss-dl

# YouTube RSS Video Downloader

This Python script allows you to download videos from YouTube channels using their RSS feeds. The script organizes the downloaded videos by channel name and year, and names each video using the format `[Upload date] - 'Name' - [Video ID]`.

## Features

- **Automatic Download**: Fetches and downloads videos from specified YouTube channels via their RSS feeds.
- **Organized Storage**: Videos are sorted into directories based on channel name and upload year.
- **Avoid Duplicate Downloads**: Tracks downloaded videos in a `downloaded.dat` file to prevent re-downloading the same video.
- **Customizable Naming Convention**: Each video is named according to the format `[Upload date] - 'Name' - [Video ID]`.

## Prerequisites

- Python 3.6+
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) installed (`pip install yt-dlp`)
- feedparser

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/yt-rss-dl.git
   cd yt-rss-dl```

2. Install the required dependencies:
   ```pip install -r requirements.txt```

## Setup

1. Add Channel IDs: Create a channel_ids.txt file in the root directory. Add the YouTube channel IDs, each on a new line. For example:
```
UCCWLtpQNoq7gbiHqssF4rPg
UC_x5XG1OV2P6uZZ5FSM9Ttw
```
2. Run the Script:
```
python yt-rss-dl.py
```

## How It Works
1. The script reads the YouTube channel IDs from channel_ids.txt.
2. It fetches the latest videos for each channel using their RSS feed.
3. The script checks if a video has already been downloaded (tracked in downloaded.dat).
4. If not downloaded, the video is downloaded using yt-dlp, saved in a directory structure organized by channel name and year.
5. The script renames the video according to the format [Upload date] - 'Name' - [Video ID].

## Example Output Structure
```
downloaded_videos/
└── Channel Name [Channel ID]/
    ├── 2023/
    │   ├── 2023-05-12 - Example Video 1 - [dQw4w9WgXcQ].mp4
    │   └── 2023-06-15 - Example Video 2 - [yPYZpwSpKmA].mp4
    └── 2024/
        └── 2024-07-11 - Example Video 3 - [zZZ5FSM9Ttw].mp4
```
