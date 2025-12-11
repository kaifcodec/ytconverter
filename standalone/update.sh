#!/usr/bin/env bash


GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RED="\033[1;31m"
NC="\033[0m"


CHECK="✅"
CROSS="❌"
WARN="⚠️"
INFO="ℹ️"
SPARK="✨"
FOLDER="📂"

if [[ "$PREFIX" == *"com.termux"* ]]; then
    echo -e "${INFO} Detected Termux environment."
    home_dir="$HOME"
else
    echo -e "${INFO} Detected Linux environment."
    home_dir="$HOME"
fi

project_dir="$home_dir/ytconverter"
backup_dir="$home_dir/bytconverter"

echo -e "${FOLDER} Changing to home directory..."
cd "$home_dir" || { echo -e "${CROSS} ${RED}Failed to change directory.${NC}"; exit 1; }

if [ -d "$project_dir" ]; then
    echo -e "${WARN} Found existing ytconverter. Backing it up..."
    mv "$project_dir" "$backup_dir"
fi

echo -e "${INFO} Cloning latest version of ytconverter..."
if git clone https://github.com/kaifcodec/ytconverter.git; then
    echo -e "${CHECK} ${GREEN}Cloned successfully.${NC}"
else
    echo -e "${CROSS} ${RED}Failed to clone repo.${NC}"
    if [ -d "$backup_dir" ]; then
        mv "$backup_dir" "$project_dir"
        echo -e "${WARN} Restored backup."
    fi
    exit 1
fi

if [ -d "$backup_dir" ]; then
    echo -e "${INFO} Removing backup..."
    rm -rf "$backup_dir"
fi

echo -e "${SPARK} Updating yt-dlp..."
if pip install --force-reinstall --no-deps yt-dlp; then
    echo -e "${CHECK} ${GREEN}yt-dlp updated successfully.${NC}"
else
    echo -e "${CROSS} ${RED}yt-dlp update failed.${NC}"
    exit 1
fi

echo -e "\n${CHECK} ${GREEN}Update complete!${NC}"
echo -e "${FOLDER} Changing into ytconverter/standalone/ directory..."
cd ytconverter/standalone/ || { echo -e "${CROSS} ${RED}Failed to enter ytconverter directory.${NC}"; exit 1; }

exec bash
