import json
import urllib.request
from sys import exit

API_URL = "https://nvapi.nicovideo.jp/v1/tmp/videos?_frontendId=0"


def fetch_videos() -> list[dict]:
    response = urllib.request.urlopen(API_URL)
    videos = json.loads(response.read())["data"]["videos"]
    return videos


all_videos = []

while True:
    try:
        videos = fetch_videos()
        for video in videos:
            if video not in all_videos:
                all_videos.append(video)
                print(f'+ [\x1b[33m{str(len(all_videos)).zfill(4)}\x1b[0m]\x1b[32m \x1b[0m[\x1b[35m{video["id"]}\x1b[0m] {video["title"]}')
    except KeyboardInterrupt:
        with open('videos.json', 'w+t', encoding='utf-8') as file:
            json.dump(all_videos, file, indent=4)
        print('\nInterrupted')
        exit(0)
