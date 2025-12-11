import json
import subprocess as sp
import time
from pathlib import Path

import yt_dlp

from ytconverter.constants import URL_RE
from ytconverter.utils import (
    apply_style,
    get_download_path,
    sanitize,
)


def run():
    from ytconverter.config import load_local_version

    down_list = []
    i = 1
    while True:
        text = (
            f"Enter URL of the video {i} you want to download as MP4 "
            f"or enter '0' to start download:"
        )
        prompt = apply_style(text, "/green/bold")
        print("\n" + prompt)
        url = input(">> ").strip()
        if url == "0":
            break
        if not URL_RE.match(url):
            print(
                apply_style("Invalid URL. Please enter a valid YouTube URL.", "/red/bold")
            )
            continue
        down_list.append(url)
        i += 1

    if not down_list:
        print(apply_style("No url given, skipping download", "/red/bold"))
        return

    format_map = {
        "1": "bestvideo[height>=1080]+bestaudio/best[height>=1080]",
        "2": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "3": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "4": "bestvideo[height<=480]+bestaudio/best[height<=480]",
        "5": "bestvideo[height<=360]+bestaudio/best[height<=360]",
    }

    quality_title = """
                  ╔════════════════════════════════════╗
                  ║      SELECT VIDEO QUALITY          ║
                  ╠════════════════════════════════════╣
                  ║  [1]  >= 1080p Full HD+/4K         ║
                  ║  [2]  1080p  Full HD               ║
                  ║  [3]  720p  HD                     ║
                  ║  [4]  480p  SD                     ║
                  ║  [5]  <= 360p  Low                 ║
                  ╚════════════════════════════════════╝
                """
    print(apply_style(quality_title, "/cyan/bold"))
    while True:
        qua_text = apply_style("Enter choice number (1-5): ", "/green/bold")
        choice = input(qua_text).strip()
        if choice in format_map:
            break
        print(
            apply_style(
                "Invalid choice. Please select a number from 1 to 5.", "/red/bold"
            )
        )

    destination = Path(get_download_path("mp4"))
    k = 1
    for url in down_list:
        ydl_opts = {"quiet": True, "no_warnings": True}
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
        except yt_dlp.utils.DownloadError as e:
            print(apply_style(f"An error occurred: {e}", "/red/bold"))
            continue

        vid_title = sanitize(info["title"])[:60]
        print(apply_style(f"\nStarting Video {k} Download...\n", "/cyan/bold"))
        time1 = int(time.time())
        ydl_opts = {
            "format": format_map[choice],
            "outtmpl": str(destination / f"{vid_title}.%(ext)s"),
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(apply_style("Video has been successfully downloaded.", "/green/bold"))
        except Exception as e:
            pass
            print(apply_style(f"Failed to download '{vid_title}': {e}", "/red"))
            continue

        time2 = int(time.time())
        ftime = time2 - time1
        print(
            "\n"
            + apply_style("Time taken to download:", "/cyan/bold"),
            apply_style(f"{ftime} sec", "/cyan"),
        )
        k += 1


if __name__ == "__main__":
  run()
