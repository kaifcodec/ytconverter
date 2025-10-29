import json
import subprocess as sp
import time
from pathlib import Path

import yt_dlp

from ytconverter.constants import URL_RE
from ytconverter.utils import get_download_path, sanitize


def run():
    from ytconverter.config import load_local_version

    print(
        "\n"
        + "\033[32;1mEnter the URL of the audio/video you want as MP3:\033[0m"
    )
    url = input(">> ").strip()
    if not URL_RE.match(url):
        print("\033[31;1mInvalid URL.\033[0m")
        return

    print("\nFetching audio information...\n")
    info_json = json.loads(
        sp.check_output(["yt-dlp", "-j", url], text=True, stderr=sp.DEVNULL)
    )
    formats = info_json.get("formats", [])
    audio_formats = [
        f
        for f in formats
        if f.get("acodec") != "none" and f.get("vcodec") == "none"
    ]

    bitrate_sizes = [
        (f["abr"], f["filesize"], f["format_id"])
        for f in audio_formats
        if f.get("abr") and f.get("filesize")
    ]

    if bitrate_sizes:
        print("Available Audio Formats:")
        for idx, (abr, size, fid) in enumerate(bitrate_sizes, 1):
            print(
                f"[{idx}] Bitrate: {abr} kbps, "
                f"Size: {size/1024/1024:.2f} MB"
            )
        while True:
            try:
                choice = int(input("\nSelect format (0 for best): "))
                if 0 <= choice <= len(bitrate_sizes):
                    break
            except ValueError:
                pass
            print("Invalid choice.")
        dl_format = (
            bitrate_sizes[choice - 1][2] if choice > 0 else "bestaudio/best"
        )
    else:
        dl_format = "bestaudio/best"

    dest = Path(get_download_path("mp3"))
    title = sanitize(info_json.get("title", "Unknown"))[:60]

    t0 = int(time.time())
    sp.run(
        [
            "yt-dlp",
            "-f",
            dl_format,
            "-x",
            "--audio-format",
            "mp3",
            "-o",
            str(dest / f"{title}.%(ext)s"),
            url,
        ],
        check=True,
    )
    print("\033[32;1mMP3 downloaded.\033[0m")
    print(f"Time taken: {int(time.time()) - t0} sec")

if __name__ == "__main__":
  run()
