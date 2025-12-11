import os
import subprocess as sp
import sys
from pathlib import Path


def ensure_dependencies():
    try:
        import colored
        import fontstyle
        import httpx
        import yt_dlp
    except ImportError:
        print("Installing required Python packages...\n")
        try:
            sp.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        except sp.CalledProcessError as e:
            print(f"Error installing Python packages: {e}")
            sys.exit(1)

        print("\nInstalling required system packages...\n")
        try:
            sp.run(["apt", "install", "-y", "ffmpeg", "yt-dlp"])
        except Exception:
            if Path("install.sh").exists():
                sp.run(["chmod", "+x", "install.sh"])
                sp.run(["./install.sh"])
            else:
                print("Please install ffmpeg & yt-dlp manually.")
                sys.exit(1)


def setup_termux_storage():
    try:
        termux_prefix = Path("/data/data/com.termux/files/usr")
        if termux_prefix.exists():
            storage = Path("/storage/emulated/0")
            if not storage.is_dir() or not os.access(storage, os.W_OK):
                os.system("termux-setup-storage")
    except Exception as e:
        print(f"Outer error: {e}")
