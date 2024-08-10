# ytrssdl/downloader.py

import os
import feedparser
import subprocess
from datetime import datetime

CHANNEL_IDS_FILE = "channel_ids.txt"
VIDEO_DOWNLOAD_DIR = "downloaded_videos"
DOWNLOADED_VIDEOS_FILE = "downloaded.dat"

def sanitize_filename(filename):
    """Sanitize the filename to avoid any illegal characters."""
    return "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_')).rstrip()

def load_downloaded_videos():
    """Load the set of downloaded video IDs from the file."""
    if not os.path.exists(DOWNLOADED_VIDEOS_FILE):
        return set()
    with open(DOWNLOADED_VIDEOS_FILE, 'r') as file:
        return set(line.strip() for line in file.readlines())

def save_downloaded_video(video_id):
    """Save a video ID to the downloaded videos file."""
    with open(DOWNLOADED_VIDEOS_FILE, 'a') as file:
        file.write(f"{video_id}\n")

def download_video(video_url, video_title, video_id, published_date, channel_name, channel_id):
    """Download the video using yt-dlp."""
    os.makedirs(VIDEO_DOWNLOAD_DIR, exist_ok=True)

    channel_dir = os.path.join(
        VIDEO_DOWNLOAD_DIR, 
        f"{sanitize_filename(channel_name)} [{channel_id}]", 
        published_date.strftime('%Y')
    )
    os.makedirs(channel_dir, exist_ok=True)
    
    output_template = os.path.join(
        channel_dir, 
        f"{published_date.strftime('%Y-%m-%d')} - {sanitize_filename(video_title)} - [{video_id}].%(ext)s"
    )
    
    command = [
        "yt-dlp",
        video_url,
        "-o", output_template
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Downloaded: {video_url}")
        save_downloaded_video(video_id)
    except subprocess.CalledProcessError:
        print(f"Failed to download: {video_url}")

def fetch_videos_for_channel(channel_id, downloaded_videos):
    rss_feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    feed = feedparser.parse(rss_feed_url)

    for entry in feed.entries:
        video_url = entry.link
        video_id = entry.id.split(':')[-1]
        video_title = entry.title
        published_date = datetime.strptime(entry.published, '%Y-%m-%dT%H:%M:%S%z')
        channel_name = entry.author
        
        if video_id in downloaded_videos:
            print(f"Skipping already downloaded video: {video_title}")
            continue
        
        print(f"Found video: {video_title} published on {published_date} from channel {channel_name}")
        
        download_video(video_url, video_title, video_id, published_date, channel_name, channel_id)

def load_channel_ids():
    with open(CHANNEL_IDS_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

def fetch_videos():
    downloaded_videos = load_downloaded_videos()
    channel_ids = load_channel_ids()
    for channel_id in channel_ids:
        print(f"Fetching videos for channel: {channel_id}")
        fetch_videos_for_channel(channel_id, downloaded_videos)