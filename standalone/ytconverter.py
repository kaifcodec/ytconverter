import datetime
import inspect
import json
import os
import platform
import re
import shutil
import subprocess as s
import time
import traceback
from pathlib import Path
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass
print("\n" + "Attempting to import required modules".center(99))
try:
    from colored import fg, attr

    f_colored = fg(117)
    r = fg(1)
    b = attr(0)
    import fontstyle as fs
    import httpx
    import yt_dlp
except ImportError:
    print("Installing required Python packages...\n")

    try:
        s.run(["pip", "install", "-r", "requirements.txt"], check=True)
    except s.CalledProcessError as e:
        print(f"Error installing Python packages: {e}")
        print("Install requirements manually")
        exit(1)

    print("\nInstalling required system packages...\n")

    try:
        print("\nTrying to install system packages assuming termux...\n")
        s.run(["pkg", "install", "-y", "ffmpeg", "yt-dlp"], check=True)
    except s.CalledProcessError as e:
        print("Error installing system packages assuming it to be termux:")

        if os.path.exists("install.sh"):
            print("Attempting to run install.sh...")
            try:
                s.run(["chmod", "+x", "install.sh"], check=True)
                s.run(["./install.sh"], check=True)
            except s.CalledProcessError as e:
                print(f"Failed to run install.sh: {e}")
                exit(1)
        else:
            print("No install.sh found. Please install the required packages manually.")
            exit(1)

    from colored import fg, attr

    f_colored = fg(117)
    r = fg(1)
    b = attr(0)
    import fontstyle as fs
    import httpx
    import yt_dlp

try:
    with open("version.json", "r") as file:
        version_json = json.load(file)
        current_version = version_json.get("version")
        version_type = version_json.get("version_type")
except:
    current_version = "version.json not found"
    exit()



print("\n" + fs.apply("Wait just version check is processing...", "/cyan/bold"))
try:
    if os.path.exists("/data/data/com.termux/files/usr/"):
        try:
            des_dir = "/storage/emulated/0/"
            if os.path.isdir(des_dir):
                if os.access(des_dir, os.W_OK):
                    pass
                else:
                    print("\nYour storage is inaccessible, press y next...")
                    time.sleep(1)
                    os.system("termux-setup-storage")
            else:
                print(
                    "\n"
                    + fs.apply(
                        "Allow the storage permission to download", "/green/bold"
                    )
                )
                time.sleep(1)
                os.system("termux-setup-storage")
        except Exception as e:
            print(f"Error: {e}")
    else:
        device = "nontermux"
except Exception as e:
    print(f"Outer error: {e}")


try:
    # Fetch version from GitHub
    response = httpx.get(
        "https://raw.githubusercontent.com/kaifcodec/ytconverter/main/standalone/version.json"
    )
    response.raise_for_status()
    version_git = response.json().get("version")

    # Load local version
    try:
        with open("version.json", "r") as file:
            version_json = json.load(file)
        current_version = version_json.get("version")
    except FileNotFoundError:
        current_version = None 
    # Compare versions
    if current_version != version_git:
        print("\n" + fs.apply("A new version for the tool is available!", "/cyan/bold"))
        print(
            f"Your current version is v{current_version or 'N/A,not found'}, latest version is v{version_git}!\n"
        )

        ver_choice = input(
            fs.apply(
                "Do you want to update to the new version automatically? (y/n): ",
                "/cyan/bold",
            )
        ).lower()

        if ver_choice == "y":
            print(
                "\n"
                + fs.apply(
                    "Running './update.sh' — ytconverter will be updated soon.",
                    "/cyan/bold",
                )
            )
            os.system("./update.sh")
            exit()
        elif ver_choice == "n":
            print(
                "\n"
                + fs.apply(
                    "Run './update.sh' in the ytconverter directory to update it later.",
                    "/cyan",
                )
            )
        else:
            print(
                "\n"
                + fs.apply("Invalid input. Proceeding to auto-update...", "/yellow")
            )
            os.system("./update.sh")
            exit()
    else:
        print(fs.apply("You are using the latest version.", "/green"))

except Exception:
    print(
        "\n"
        + fs.apply(
            "Version check failed — maybe a new version is available.\nRun './update.sh' or remove and clone the repository again from GitHub to check.",
            "/red/bold",
        )
    )


f1 = r"""
     __   _______ ____                          _
     \ \ / /_   _/ ___|___  _ ____   _____ _ __| |_ ___ _ __
      \ V /  | || |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
       | |   | || |__| (_) | | | \ V /  __/ |  | ||  __/ |
       |_|   |_| \____\___/|_| |_|\_/ \___|_|   \__\___|_|"""
f2 = """
      ╔═════════════════════════════════════════╗
      ║ ♚ Project Name : YTConverter™           ║
      ║ ♚ Author : Kaif                         ║
      ║ ♚ Github : https://github.com/kaifcodec ║
      ║ ♚ Email  : kaifcodec@gmail.com          ║
      ╠══════════════════════════════════════════ """
f3 = """      ╠═▶ [\033[1mSelect An Option\033[0m] ➳
      ╠═▶ 1. Single Music Mp3 ⏬ 🎶
      ╠═▶ 2. Single Video ⏬ 🎥 (detailed quality & size but slow fetch)
      ╠═▶ 3. Multiple videos ⏬ 🎥
      ╠═▶ 4. Multiple audios ⏬ 🎶  
      ╠═▶ 5. Exit YTConverter"""
f4 = "      ╚═:➤ "

des1 = fs.apply(f1, "/green/bold")
des2 = fs.apply(f2, "/yellow")
des3 = fs.apply(f3, "/cyan")
des4 = fs.apply(f4, "/cyan")

burl = fs.apply("Bad url check the url first", "/red/bold")
error = fs.apply("AN ERROR OCCURRED, RUN THE CODE AGAIN", "/red/bold")


def bio():
    try:
        print(f"{des1}  Version: {current_version}")
        print(des2)
        print(des3)
    except:
        print("file: version.json not found in cwd, run ./update.sh manually")
        print(des1)
        print(des2)
        print(des3)


text1 = fs.apply("Enter the url of the video you want \nto download  ", "/green/bold")
text2 = fs.apply(
    "Enter the destination path where you want to save this mp3  ", "/yellow/bold"
)
text3 = fs.apply("(Or leave blank to save in current directory)", "/yellow/bold")
text4 = fs.apply("Taken time to download =", "/cyan/bold")


def sanitize(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)


################
def is_android():
    return (
        "ANDROID_ROOT" in os.environ
        or "TERMUX_VERSION" in os.environ
        or "com.termux" in os.getenv("HOME", "")
    )


def remove_ansi_styles(text: str) -> str:
    import re

    ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", text)


def get_download_path(format_str: str) -> str:
    system = platform.system()
    home = Path.home()

    if system == "Windows":
        base_download = home / "Downloads"
    elif system == "Darwin":
        base_download = home / "Downloads"
    elif is_android():
        base_download = Path("/storage/emulated/0/Download")
    else:
        base_download = home / "Downloads"

    if format_str.lower() == "mp3":
        default_path = base_download / "audio"
    elif format_str.lower() == "mp4":
        default_path = base_download / "videos"
    else:
        default_path = base_download

    styled_path = fs.apply(str(default_path), "/green/bold")
    print(f"\nDefault download path for {format_str}: {styled_path}\n")

    user_input = input(
        "Enter a different path or press Enter to accept default: "
    ).strip()
    final_path = Path(user_input) if user_input else Path(default_path)

    final_path.mkdir(parents=True, exist_ok=True)
    return str(final_path)


def main_mp4():
    print(
        "\n"
        + fs.apply(
            "Enter the URL of the video you want to download as MP4:", "/green/bold"
        )
    )
    url = input(">> ")

    url_pattern = re.compile(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$")
    if not url_pattern.match(url):
        print(fs.apply("Invalid URL. Please enter a valid YouTube URL.", "/red/bold"))
        return

    url = url.strip()
    print(
        fs.apply(
            "\nFetching available video formats (this process could take 5 to 10s) Zoom out to see all formats clearly...\n",
            "/cyan/bold",
        )
    )
    try:
        process = s.Popen(
            ["yt-dlp", "--list-formats", url], stdout=s.PIPE, stderr=s.PIPE
        )
        stdout, stderr = process.communicate()
        if stderr:
            print(fs.apply(f"Warning: {stderr.decode('utf-8', errors='replace')}", "/yellow/bold"))
        formats_output = stdout.decode("utf-8", errors="replace")
        print(formats_output)
        print(
            "\n" + fs.apply("Wait final format selection is loading...", "/green/bold")
        )
        print(
            fs.apply(
                "Some sizes may be displayed as 'Unknown' in final format, check them from the upper table by respective format id",
                "/yellow/bold/italic",
            )
        )
    except Exception as e:
        print(fs.apply(f"Error listing formats: {e}", "/red/bold"))
        return

    # Extract video information
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get("formats", [])
    except yt_dlp.utils.DownloadError as e:
        print(fs.apply(f"An error occurred: {e}", "/red/bold"))
        return

    title_test = sanitize(info.get("title", "Unknown title"))

    ###############
    ###############
    # Display available formats with download size
    print(fs.apply("\nAvailable Formats:\n", "/cyan/bold"))
    for i, fmt in enumerate(formats):
        res = (
            fmt.get("resolution", "Audio Only")
            if fmt.get("vcodec") != "none"
            else "Audio Only"
        )
        ext = fmt.get("ext", "Unknown")
        acodec = fmt.get("acodec", "None")
        vcodec = fmt.get("vcodec", "None")

        # Get the size of the format, handling approximate sizes
        filesize = fmt.get("filesize")
        if filesize is None:
            filesize = fmt.get("filesize_approx")
            if filesize:
                filesize = str(fmt.get("filesize_approx"))
                filesize_str = f"{float(filesize.replace('~', '')) / (1024 * 1024):.2f} MB (approx.)"
            else:
                filesize_str = "Unknown size"
        else:
            filesize_str = f"{filesize / (1024 * 1024):.2f} MB"

        # Display the format with size
        print(
            f"{fs.apply(f'[{i + 1}]', '/yellow/bold')} {fs.apply(res, '/cyan')} ({fs.apply(ext, '/magenta')}) - Format ID: {fs.apply(fmt['format_id'], '/green')} - Audio: {fs.apply(acodec, '/magenta')} - Video: {fs.apply(vcodec, '/magenta')} - Size: {fs.apply(filesize_str, '/blue/bold')}"
        )

    # User selects format
    while True:
        try:
            choice = (
                int(
                    input(
                        fs.apply(
                            "\nEnter the number of your preferred format: ",
                            "/green/bold",
                        )
                    )
                )
                - 1
            )
            if 0 <= choice < len(formats):
                selected_format = formats[choice]
                break
            else:
                print(fs.apply("Invalid choice. Try again.", "/red/bold"))
        except ValueError:
            print(fs.apply("Enter a valid number.", "/red/bold"))

    selected_format_id = selected_format["format_id"]
    has_audio = selected_format.get("acodec") != "none"
    has_video = selected_format.get("vcodec") != "none"

    # Handle audio separately if not present in selected format
    audio_downloaded = False
    audio_path = None
    if has_video and not has_audio:
        print(
            fs.apply(
                "\nSelected format has NO AUDIO. Attempting to download audio separately...",
                "/yellow/bold",
            )
        )
        try:
            audio_destination = os.getcwd() + "/audio_temp"
            os.makedirs(audio_destination, exist_ok=True)
            audio_filename = os.path.join(audio_destination, "%(title)s.%(ext)s")
            s.call(["yt-dlp", "-x", "--audio-format", "mp3", "-o", audio_filename, url])

            # Locate the downloaded audio file
            for root, _, files in os.walk(audio_destination):
                for file in files:
                    if file.endswith(".mp3"):
                        audio_path = os.path.join(root, file)
                        break

            if not audio_path or not os.path.exists(audio_path):
                print(
                    fs.apply(
                        f"Error: Audio file not found in {audio_destination}. Please check if the file was downloaded correctly.",
                        "/red/bold",
                    )
                )
                return

            print(fs.apply("MP3 audio downloaded successfully.", "/green/bold"))
            audio_downloaded = True
        except Exception as e:
            print(fs.apply(f"Error downloading MP3 audio: {e}", "/red/bold"))
            return

    print(fs.apply("\nStarting Video Download...\n", "/cyan/bold"))
    time1 = int(time.time())

    # Define download path
    destination = get_download_path("mp4")

    video_path = os.path.join(destination, f"{info['title']}.mp4")
    ydl_opts = {
        "format": selected_format_id,
        "outtmpl": video_path,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(fs.apply("Video has been successfully downloaded.", "/green/bold"))
    except Exception as e:
        print(fs.apply(f"An error occurred: {e}", "/red/bold"))
        return

    time2 = int(time.time())
    ftime = time2 - time1
    print(
        fs.apply("Time taken to download:", "/cyan/bold"),
        fs.apply(f"{ftime} sec", "/cyan"),
    )

    # Merge audio and video if necessary
    if audio_downloaded:
        print(fs.apply("Merging audio and video...", "/yellow/bold"))
        merged_path = os.path.join(destination, f"{info['title']}_merged.mp4")
        try:
            # Add a timeout to prevent hanging
            ffmpeg_command = [
                "ffmpeg",
                "-y",
                "-i",
                video_path,
                "-i",
                audio_path,
                "-c:v",
                "copy",
                "-c:a",
                "aac",
                merged_path,
            ]
            print(fs.apply(f"Executing: {' '.join(ffmpeg_command)}", "/cyan/bold"))

            # Use subprocess to execute the command and capture output
            process = s.Popen(ffmpeg_command, stdout=s.PIPE, stderr=s.PIPE, text=True)
            stdout, stderr = process.communicate(timeout=300)  # Timeout after 5 minutes

            if process.returncode == 0:
                print(fs.apply("Audio and video merged successfully.", "/green/bold"))
                os.remove(video_path)
                os.remove(audio_path)
            else:
                print(fs.apply(f"Error merging audio and video: {stderr}", "/red/bold"))
                print(fs.apply(f"ffmpeg stdout: {stdout}", "/yellow"))
        except s.TimeoutExpired:
            process.kill()
            print(
                fs.apply(
                    "The merging process timed out. Please check your files manually.",
                    "/red/bold",
                )
            )
        except Exception as e:
            print(fs.apply(f"Error merging audio and video: {e}", "/red/bold"))
    else:
        print(fs.apply("No audio merging required.", "/yellow/bold"))

    # Cleanup temporary files
    temp_audio_dir = os.getcwd() + "/audio_temp"
    if os.path.exists(temp_audio_dir):
        shutil.rmtree(temp_audio_dir, ignore_errors=True)
        print(fs.apply("Temporary audio files cleaned up.", "/cyan/bold"))


################
def main_mp3():
    print(
        "\n"
        + fs.apply(
            "Enter the URL of the audio/video you want to download as MP3:",
            "/green/bold",
        )
    )
    url = input(">> ")

    url_pattern = re.compile(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$")
    if not url_pattern.match(url):
        print(fs.apply("Invalid URL. Please enter a valid YouTube URL.", "/red/bold"))
        return

    url = url.strip()

    print("\nFetching audio information (this process could take 5s)...\n")
    info_json={}
    try:
        process = s.Popen(["yt-dlp", "-j", url], stdout=s.PIPE, stderr=s.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            print(fs.apply(f"yt-dlp error: {stderr.decode('utf-8', errors='replace')}", "/red/bold"))
        info_json = json.loads(stdout.decode("utf-8", errors="replace"))
        formats = info_json.get("formats", [])
        audio_formats = [
            f
            for f in formats
            if f.get("acodec") != "none" and f.get("vcodec") == "none"
        ]

        if not audio_formats:
            print(fs.apply("No audio formats available for this video.", "/red/bold"))
            return

        bitrate_sizes = []
        for fmt in audio_formats:
            if fmt.get("abr") and fmt.get("filesize"):
                bitrate_sizes.append((fmt["abr"], fmt["filesize"], fmt["format_id"]))

        if bitrate_sizes:
            print("\nAvailable Audio Formats:")
            for i, (abr, filesize, format_id) in enumerate(bitrate_sizes):
                print(
                    f"[{i + 1}] Bitrate: {abr} kbps, Size: {filesize_format(filesize)}"
                )

            while True:
                try:
                    choice = int(
                        input(
                            "\nEnter the number of your preferred format (or 0 for best): "
                        )
                    )
                    if 0 <= choice <= len(bitrate_sizes):
                        break
                    else:
                        print(fs.apply("Invalid choice. Try again.", "/red/bold"))
                except ValueError:
                    print(fs.apply("Enter a valid number.", "/red/bold"))

            if choice > 0:
                selected_format_id = bitrate_sizes[choice - 1][2]
                print(
                    fs.apply(
                        f"\nDownloading audio with format ID: {selected_format_id}",
                        "/yellow/bold",
                    )
                )
                download_format = selected_format_id
            else:
                print(
                    fs.apply(
                        "\nDownloading best available audio format.", "/yellow/bold"
                    )
                )
                download_format = "bestaudio/best"
        else:
            print(
                fs.apply("\nDownloading best available audio format.", "/yellow/bold")
            )
            download_format = "bestaudio/best"

    except Exception as e:
        print(fs.apply(f"Error fetching audio information: {e}", "/red/bold"))
        print(fs.apply("Downloading best available audio format.", "/yellow/bold"))
        download_format = "bestaudio/best"

    print(fs.apply("\nStarting MP3 Download...\n", "/yellow/bold"))
    time1 = int(time.time())

    destination = get_download_path("mp3")
    try:
        s.call(
            [
                "yt-dlp",
                "-f",
                download_format,
                "-x",
                "--audio-format",
                "mp3",
                "-o",
                os.path.join(destination, "%(title)s.%(ext)s"),
                url,
            ]
        )
        print(fs.apply("MP3 audio downloaded successfully.", "/green/bold"))
    except Exception as e:
        print(fs.apply(f"An error occurred: {e}", "/red/bold"))
        return

    time2 = int(time.time())
    ftime = time2 - time1
    print(
        fs.apply("Taken time to download:", "/cyan/bold"),
        fs.apply(f"{ftime} sec", "/cyan/bold"),
    )


def main_multi_mp4():
    down_list = []
    i = 1
    while True:
        text = f"Enter URL of the video {i} you want to download as MP4 or enter '0' to start download:"
        prompt = fs.apply(text, "/green/bold")
        print("\n" + prompt)
        url = input(">> ")
        url_pattern = re.compile(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$")
        if url == "0":
            if down_list:
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
                print(fs.apply(quality_title, "/cyan/bold"))
                while True:
                    qua_text = fs.apply("Enter choice number (1-5): ", "/green/bold")
                    choice = input(qua_text)
                    if choice not in format_map:
                        print(
                            fs.apply(
                                "Invalid choice. Please select a number from 1 to 5.",
                                "/red/bold",
                            )
                        )
                        continue
                    else:
                        break

                destination = get_download_path("mp4")
                k = 1
                for url in down_list:
                    # Extract video information
                    ydl_opts = {
                        "quiet": True,
                        "no_warnings": True,
                    }

                    try:
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            info = ydl.extract_info(url, download=False)
                    except yt_dlp.utils.DownloadError as e:
                        print(fs.apply(f"An error occurred: {e}", "/red/bold"))
                        return

                    print(fs.apply(f"\nStarting Video {k} Download...\n", "/cyan/bold"))
                    time1 = int(time.time())
                    vid_title = sanitize(info["title"])
                    video_path = os.path.join(destination, vid_title)

                    ydl_opts = {
                        "format": format_map.get(choice),
                        "outtmpl": video_path,
                    }

                    try:
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([url])
                            print(
                                fs.apply(
                                    "Video has been successfully downloaded.",
                                    "/green/bold",
                                )
                            )
                    except Exception as e:

                        print(
                            fs.apply(f"Failed to download '{vid_title}': {e}", "/red")
                        )
                        continue  # Continue to the next URL

                    time2 = int(time.time())
                    ftime = time2 - time1
                    print(
                        "\n" + fs.apply("Time taken to download:", "/cyan/bold"),
                        fs.apply(f"{ftime} sec", "/cyan"),
                    )
                    k += 1
            else:
                print(fs.apply("No url given, skipping download", "/red/bold"))
            break

        elif not url_pattern.match(url):
            print(
                fs.apply("Invalid URL. Please enter a valid YouTube URL.", "/red/bold")
            )
            continue
        down_list.append(url)
        i += 1





def main_multi_mp3():
    down_list = []
    i = 1
    while True:
        text = f"Enter URL of the video {i} you want to download as MP3 or enter '0' to start download:"
        prompt = fs.apply(text, "/green/bold")
        print("\n" + prompt)
        url = input(">> ")
        url_pattern = re.compile(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$")
        if url == "0":
            if down_list:
                quality_map = {
                    "1": "320",  # best available
                    "2": "256",
                    "3": "192",
                    "4": "128",
                    "5": "96",
                }

                quality_title = """
                  ╔════════════════════════════════════╗
                  ║      SELECT AUDIO QUALITY          ║
                  ╠════════════════════════════════════╣
                  ║  [1]  320 kbps (High)              ║
                  ║  [2]  256 kbps (Very Good)         ║
                  ║  [3]  192 kbps (Good)              ║
                  ║  [4]  128 kbps (Standard)          ║
                  ║  [5]  96 kbps (Low)                ║
                  ╚════════════════════════════════════╝
                """
                print(fs.apply(quality_title, "/cyan/bold"))
                while True:
                    qua_text = fs.apply("Enter choice number (1-5): ", "/green/bold")
                    choice = input(qua_text)
                    if choice not in quality_map:
                        print(
                            fs.apply(
                                "Invalid choice. Please select a number from 1 to 5.",
                                "/red/bold",
                            )
                        )
                        continue
                    else:
                        break

                destination = get_download_path("mp3")
                k = 1
                for url in down_list:
                    ydl_opts = {
                        "quiet": True,
                        "no_warnings": True,
                    }

                    try:
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            info = ydl.extract_info(url, download=False)
                    except yt_dlp.utils.DownloadError as e:
                        print(fs.apply(f"An error occurred: {e}", "/red/bold"))
                        return

                    print(fs.apply(f"\nStarting Audio {k} Download...\n", "/cyan/bold"))
                    time1 = int(time.time())
                    vid_title = sanitize(info["title"])
                    audio_path = os.path.join(destination, vid_title)

                    ydl_opts = {
                        "format": "bestaudio/best",
                        "outtmpl": audio_path,
                        "postprocessors": [
                            {
                                "key": "FFmpegExtractAudio",
                                "preferredcodec": "mp3",
                                "preferredquality": quality_map[choice],
                            }
                        ],
                    }

                    try:
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([url])
                            print(
                                fs.apply(
                                    "Audio has been successfully downloaded.",
                                    "/green/bold",
                                )
                            )
                    except Exception as e:
                        print(
                            fs.apply(f"Failed to download '{vid_title}': {e}", "/red")
                        )
                        continue

                    time2 = int(time.time())
                    ftime = time2 - time1
                    print(
                        "\n" + fs.apply("Time taken to download:", "/cyan/bold"),
                        fs.apply(f"{ftime} sec", "/cyan"),
                    )
                    k += 1
            else:
                print(fs.apply("No url given, skipping download", "/red/bold"))
            break

        elif not url_pattern.match(url):
            print(
                fs.apply("Invalid URL. Please enter a valid YouTube URL.", "/red/bold")
            )
            continue
        down_list.append(url)
        i += 1

def filesize_format(size):
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.2f} {unit}"


################



def main():
    if option == "1":
        print("""\n\n""")
        main_mp3()
    elif option == "2":
        print("""\n\n""")
        main_mp4()
    elif option == "3":
        print("""\n\n""")
        main_multi_mp4()
    elif option == "4":
        print("""\n\n""")
        main_multi_mp3()
    elif option == "5":
        print("""\nHave a nice day Bye!""")
        exit()
    else:
        print("Have a nice day Bye!")
        exit()



try:
    os.system("clear")
    os.system("rm -r -f __pycache__ ")
except:
    pass


bio()
option = input(des4).strip()
main()
exitc = fs.apply(
    "Press [ENTER] to continue downloading another content  ", "/green/bold"
)
print(exitc)
choice = input(">>")
while choice in ("", " "):
    bio()
    option = input(des4).strip()
    main()
