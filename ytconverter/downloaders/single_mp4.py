import datetime
import os
import shutil
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
        + "\033[36;1mEnter the URL of the video you want to download as MP4:\033[0m"
    )
    url = input(">> ").strip()
    if not URL_RE.match(url):
        print("\033[31;1mInvalid URL. Please enter a valid YouTube URL.\033[0m")
        return

    print(
        "\033[36;1m\nFetching available video formats "
        "(this process could take 5 to 10s)...\033[0m\n"
    )
    try:
        proc = sp.Popen(
            ["yt-dlp", "--list-formats", url], stdout=sp.PIPE, stderr=sp.PIPE
        )
        stdout, stderr = proc.communicate()
        if stderr:
            print(
                "\033[33;1mWarning:\033[0m "
                f"{stderr.decode('utf-8', errors='replace')}"
            )
        print(stdout.decode("utf-8", errors="replace"))
    except Exception as e:
        pass
        print(f"\033[31;1mError listing formats: {e}\033[0m")
        return

    ydl_opts = {"quiet": True, "no_warnings": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get("formats", [])
    except yt_dlp.utils.DownloadError as e:
        pass
        print(f"\033[31;1mAn error occurred: {e}\033[0m")
        return

    title = sanitize(info.get("title", "Unknown title"))

    # Display formats with size
    for idx, fmt in enumerate(formats, 1):
        res = (
            fmt.get("resolution", "Audio Only")
            if fmt.get("vcodec") != "none"
            else "Audio Only"
        )
        ext = fmt.get("ext", "Unknown")
        acodec = fmt.get("acodec", "None")
        vcodec = fmt.get("vcodec", "None")

        filesize = fmt.get("filesize")
        if filesize is None:
            filesize = fmt.get("filesize_approx")
            if filesize:
                filesize_str = f"{filesize / (1024*1024):.2f} MB (approx.)"
            else:
                filesize_str = "Unknown size"
        else:
            filesize_str = f"{filesize / (1024*1024):.2f} MB"

        print(
            f"\033[33;1m[{idx}]\033[0m "
            f"\033[36m{res}\033[0m (\033[35m{ext}\033[0m) "
            f"ID: \033[32m{fmt['format_id']}\033[0m "
            f"Audio: \033[35m{acodec}\033[0m Video: \033[35m{vcodec}\033[0m "
            f"Size: \033[34;1m{filesize_str}\033[0m"
        )

    while True:
        try:
            choice = int(input("\033[32;1mEnter format number: \033[0m")) - 1
            if 0 <= choice < len(formats):
                selected = formats[choice]
                break
            print("\033[31;1mInvalid choice.\033[0m")
        except ValueError:
            print("\033[31;1mEnter a valid number.\033[0m")

    selected_id = selected["format_id"]
    has_audio = selected.get("acodec") != "none"
    has_video = selected.get("vcodec") != "none"

    audio_downloaded = False
    audio_path = None
    if has_video and not has_audio:
        print(
            "\033[33;1mSelected format has NO AUDIO. "
            "Downloading audio separately...\033[0m"
        )
        try:
            temp_dir = Path.cwd() / "audio_temp"
            temp_dir.mkdir(exist_ok=True)
            sp.run(
                [
                    "yt-dlp",
                    "-x",
                    "--restrict-filenames",
                    "--audio-format",
                    "mp3",
                    "-o",
                    str(temp_dir / "%(title)s.%(ext)s"),
                    url,
                ],
                check=True,
            )
            for file in temp_dir.iterdir():
                if file.suffix == ".mp3":
                    audio_path = str(file)
                    audio_downloaded = True
                    break
            if not audio_downloaded:
                print("\033[31;1mAudio file not found.\033[0m")
                return
        except Exception as e:
            print(f"\033[31;1mError downloading audio: {e}\033[0m")
            return

    dest = Path(get_download_path("mp4"))
    safe_title = sanitize(title)[:60]
    video_out = dest / f"{safe_title}.mp4"
    ydl_opts = {
             "format": selected_id,
             "restrictfilenames": True,
             "outtmpl": str(video_out)
    }




    print("\033[36;1mStarting Video Download...\033[0m\n")
    t0 = int(time.time())
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"\033[31;1mDownload error: {e}\033[0m")
        return
    t1 = int(time.time())
    print("\033[32;1mVideo downloaded.\033[0m")
    print(f"\033[36;1mTime taken: {t1-t0} sec\033[0m")

    if audio_downloaded:
        merged = dest / f"{safe_title}_merged.mp4"
        cmd = [
            "ffmpeg",
            "-y",
            "-i",
            str(video_out),
            "-i",
            audio_path,
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            str(merged),
        ]
        print("\033[33;1mMerging audio & video...\033[0m")
        try:
            sp.run(cmd, check=True, stdout=sp.PIPE, stderr=sp.PIPE)
            video_out.unlink()
            Path(audio_path).unlink()
            merged.rename(video_out)
        except Exception as e:
            print(f"\033[31;1mMerge error: {e}\033[0m")
            return
        print("\033[32;1mMerge complete.\033[0m")

    if Path("audio_temp").exists():
        shutil.rmtree("audio_temp", ignore_errors=True)

if __name__=="__main__":
  run()
