import platform
from pathlib import Path

from ytconverter.utils.styling import apply_style


def is_android() -> bool:
    env = __import__("os").environ
    return any(
        k in env for k in ("ANDROID_ROOT", "TERMUX_VERSION")
    ) or "com.termux" in env.get("HOME", "")


def get_download_path(format_str: str) -> str:
    system = platform.system()
    home = Path.home()

    if system == "Windows":
        base = home / "Downloads"
    elif system == "Darwin":
        base = home / "Downloads"
    elif is_android():
        base = Path("/storage/emulated/0/Download")
    else:
        base = home / "Downloads"

    if format_str.lower() == "mp3":
        default = base / "audio"
    elif format_str.lower() == "mp4":
        default = base / "videos"
    else:
        default = base

    print(
        f"\nDefault download path for {format_str}: "
        f"{apply_style(str(default), '/green/bold')}\n"
    )
    user = input("Enter a different path or press Enter to accept default: ").strip()
    final = Path(user) if user else default
    final.mkdir(parents=True, exist_ok=True)
    return str(final)
