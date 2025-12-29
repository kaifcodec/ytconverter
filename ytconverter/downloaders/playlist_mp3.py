import subprocess as sp
import time
from pathlib import Path

import yt_dlp

from ytconverter.constants import URL_RE
from ytconverter.utils import apply_style, get_download_path, sanitize


def run():
    from ytconverter.config import load_local_version

    print("\n" + apply_style("Enter the playlist URL you want to download as MP3 (audio):", "/cyan"))
    url = input(">> ").strip()
    if not URL_RE.match(url):
        print(apply_style("Invalid URL. Please enter a valid YouTube URL.", "/red/bold"))
        return

    ydl_opts = {"quiet": True, "no_warnings": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        print(apply_style(f"Failed to fetch playlist info: {e}", "/red/bold"))
        return

    playlist_title = info.get("title") or info.get("playlist_title") or "playlist"
    safe_playlist_title = sanitize(playlist_title)[:60]

    destination = Path(get_download_path("mp3"))
    playlist_folder = destination / safe_playlist_title
    playlist_folder.mkdir(parents=True, exist_ok=True)

    ask_subs = input(apply_style("\nDownload subtitles for playlist videos? (y/n): ", "/cyan")).strip().lower()
    sub_flags = []
    cookie_path = ""
    if ask_subs == "y":
        print(apply_style("Note: YouTube may block subtitle extraction with HTTP 429. If that happens provide a cookies file.", "/yellow"))
        cookie_path = input(apply_style("Enter path to cookies file for yt-dlp (optional, press Enter to skip): ", "/green")).strip()
        lang = input(apply_style("Enter subtitle language code (e.g. en) or leave blank for all: ", "/green")).strip()
        pref_auto = input(apply_style("Also download automatic subtitles if manual not available? (y/n) [y]: ", "/green")).strip().lower()
        if pref_auto == "":
            pref_auto = "y"
        sub_flags += ["--write-sub"]
        if pref_auto == "y":
            sub_flags += ["--write-auto-sub"]
        if lang:
            sub_flags += ["--sub-lang", lang]
        sub_flags += ["--convert-subs", "srt"]
        if cookie_path:
            sub_flags += ["--cookies", cookie_path]

    out_template = str(playlist_folder / "%(playlist_index)03d - %(title)s.%(ext)s")
    cmd = [
        "yt-dlp",
        "-i",
        "--yes-playlist",
        "-x",
        "--audio-format", "mp3",
        "-o", out_template,
    ]
    if sub_flags:
        cmd += sub_flags

    cmd += [url]

    print(apply_style("\nStarting playlist MP3 download. This may take a while depending on size...\n", "/yellow/bold"))
    start = int(time.time())
    try:
        sp.run(cmd, check=True)
    except Exception as e:
        print(apply_style(f"An error occurred while downloading the playlist: {e}", "/red/bold"))
        return
    end = int(time.time())
    print(apply_style(f"\nPlaylist '{playlist_title}' downloaded to: {playlist_folder}", "/green/bold"))
    print(apply_style(f"Time taken: {end - start} sec", "/cyan"))
