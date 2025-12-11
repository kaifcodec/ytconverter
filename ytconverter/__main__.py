import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

EPILOG = """
Upcoming:
  ytconverter <url> -mp3 -b 128, 192, ...
  ytconverter <url> -mp4 -r 720, 1080, 4K, ...
  ytconverter <url> -multi_<mp4/mp3>
  ytconverter <url> --playlist
"""

def main():
    parser = argparse.ArgumentParser(
        description="YTConverter - YouTube Downloader CLI Tool",
        epilog=EPILOG,
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False)

    mutually_exclusive_group = parser.add_mutually_exclusive_group()

    mutually_exclusive_group.add_argument(
        "-S", "-s", action="store_true", help="Launch the interactive menu and the main script.")

    mutually_exclusive_group.add_argument(
        "-U", "--update",
        action="store_true",
        help="Update YTConverter to the latest version via pip.")

    mutually_exclusive_group.add_argument(
        "-v", "--version", action="store_true", help="Show the current installed version.")

    mutually_exclusive_group.add_argument(
        "-h", "--help", action="help", help="Show this help message.")

    args = parser.parse_args()

    if args.update:
        from ytconverter.utils.update import update_self
        update_self()
        return

    elif args.version:
        from ytconverter.config import load_local_version
        local_version, version_type = load_local_version()
        print(f"YTConverter version: {local_version}")
        return

    elif args.S:
        from ytconverter.cli.menu import main_loop
        main_loop()
        return

    else:
        parser.print_help()
        return

if __name__ == "__main__":
    main()
