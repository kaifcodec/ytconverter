import os
import sys
from pathlib import Path

from ytconverter.cli.banner import print_banner, des4
from ytconverter.config import load_local_version
from ytconverter.core.bootstrap import ensure_dependencies, setup_termux_storage
from ytconverter.utils.update import update_self
from ytconverter.core.version import check_version
from ytconverter.downloaders import multi_mp3, multi_mp4, single_mp3, single_mp4
from ytconverter.utils.styling import apply_style

ensure_dependencies()
setup_termux_storage()

# Version check
local, remote = check_version()
if remote and local != remote:
    print(
        apply_style("\nA new version for the tool is available!\n", "/cyan/bold")
        + f"Current: v{local}, Latest: v{remote}\n"
    )
    choice = input(
        apply_style("Update automatically? (y/n): ", "/cyan/bold")
    ).lower()
    if choice in {"y", ""}:
        update_self()
        exit()

def main_loop():
    while True:
        os.system("clear")
        version, version_type = load_local_version()
        print_banner(version+"_pypi")
        choice = input(des4).strip()
        if choice == "1":
            single_mp3.run()
        elif choice == "2":
            single_mp4.run()
        elif choice == "3":
            multi_mp4.run()
        elif choice == "4":
            multi_mp3.run()
        elif choice == "5":
            print("Have a nice day, Bye!")
            sys.exit()
        else:
            print("Have a nice day, Bye!")
            sys.exit()

        exitc = apply_style(
            "Press [ENTER] to continue downloading another content  ", "/green/bold"
        )
        input(exitc)



