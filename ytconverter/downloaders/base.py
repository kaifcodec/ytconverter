import subprocess as sp
from pathlib import Path

from ytconverter.utils import sanitize


def safe_filename(title: str) -> str:
    return sanitize(title)


def yt_dlp_run(args):
    """Thin wrapper to run yt-dlp and raise on error."""
    sp.run(["yt-dlp"] + args, check=True)
