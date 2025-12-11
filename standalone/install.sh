#!/usr/bin/env bash

CHECK="✅"
CROSS="❌"
INFO="ℹ️"
STAR="✨"

# ANSI colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RESET='\033[0m'

# Color support check
supports_color() {
    if [ -t 1 ] && [ -n "$TERM" ] && [ "$TERM" != "dumb" ]; then
        return 0
    else
        GREEN=''; RED=''; YELLOW=''; CYAN=''; RESET=''
    fi
}

detect_os() {
    if [ -f /data/data/com.termux/files/usr/bin/pkg ]; then
        echo "termux"
    elif [ -f /etc/os-release ]; then
        . /etc/os-release
        case "$ID" in
            ubuntu|debian) echo "debian" ;;
            kali) echo "kali" ;;
            arch|manjaro) echo "arch" ;;
            *) echo "unknown" ;;
        esac
    else
        echo "unknown"
    fi
}

detect_sudo() {
    if command -v sudo >/dev/null 2>&1; then
        echo "sudo"
    else
        echo ""
    fi
}

install_system_packages() {
    local os=$1
    local sudo_cmd=$2

    echo -e "${INFO} ${CYAN}Detected OS: $os${RESET}"

    case "$os" in
        termux)
            pkg update -y && pkg install -y python ffmpeg yt-dlp || {
                echo -e "${CROSS} ${RED}Failed to install system packages on Termux.${RESET}"
                exit 1
            }
            ;;
        debian|kali)
            $sudo_cmd apt update && $sudo_cmd apt install -y python3 python3-pip ffmpeg yt-dlp || {
                echo -e "${CROSS} ${RED}Failed to install system packages on Debian-based system.${RESET}"
                exit 1
            }
            ;;
        arch)
            $sudo_cmd pacman -Sy --noconfirm python python-pip ffmpeg yt-dlp || {
                echo -e "${CROSS} ${RED}Failed to install system packages on Arch-based system.${RESET}"
                exit 1
            }
            ;;
        *)
            echo -e "${YELLOW}${INFO} Unsupported OS. Attempting minimal setup...${RESET}"
            command -v python3 >/dev/null || echo -e "${CROSS} ${YELLOW}Install Python 3 manually."
            command -v pip3 >/dev/null || {
                echo -e "${INFO} ${YELLOW}Trying to install pip...${RESET}"
                curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                python3 get-pip.py || echo -e "${CROSS} ${RED}Pip install failed.${RESET}"
            }
            command -v ffmpeg >/dev/null || echo -e "${YELLOW}${INFO} Install ffmpeg manually.${RESET}"
            command -v yt-dlp >/dev/null || echo -e "${YELLOW}${INFO} Try: pip3 install yt-dlp${RESET}"
            ;;
    esac
}

install_python_packages() {
    echo -e "\n${INFO} ${CYAN}Installing Python packages...${RESET}"
    PIP_CMD="pip3"
    command -v pip3 >/dev/null || PIP_CMD="pip"

    if [ "$os_type" != "termux" ]; then
        $PIP_CMD install --upgrade pip || {
            echo -e "${CROSS} ${RED}Failed to upgrade pip.${RESET}"
            exit 1
        }
    else
        echo -e "${YELLOW}${INFO} Skipping pip upgrade on Termux to avoid breaking it.${RESET}"
    fi

    $PIP_CMD install --upgrade yt_dlp fontstyle colored requests || {
        echo -e "${CROSS} ${RED}Python package installation failed.${RESET}"
        exit 1
    }
}

main() {
    supports_color
    echo -e "${STAR} ${GREEN}Starting YTConverter™ universal installer...${RESET}"

    os_type=$(detect_os)
    sudo_cmd=$(detect_sudo)

    install_system_packages "$os_type" "$sudo_cmd"
    install_python_packages

    echo -e "\n${CHECK} ${GREEN}Installation complete! You can now run YTConverter™.${RESET}"
    echo -e "${INFO} ${CYAN}To start: run 'python ytconverter.py' or use your launcher.${RESET}"
}

main
