## YTConverter™
<img width="1020" height="732" alt="1000136389" src="https://github.com/user-attachments/assets/ef9eef49-e366-46cd-937f-834b6d85167b" />

---

<p align="center">
  <img src="https://img.shields.io/badge/Version-4.0.2-blueviolet?style=for-the-badge&logo=github" />
<!--  <img src="https://img.shields.io/github/forks/kaifcodec/ytconverter?style=for-the-badge&logo=git" />
  <img src="https://img.shields.io/github/stars/kaifcodec/ytconverter?style=for-the-badge&logo=github" /> -->
  <img src="https://img.shields.io/github/issues/kaifcodec/ytconverter?style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tested%20on-Termux-black?style=for-the-badge&logo=termux" />
  <img src="https://img.shields.io/badge/Tested%20on-Windows-cyan?style=for-the-badge&logo=Windows" />
  <img src="https://img.shields.io/badge/Tested%20on-Linux-balck?style=for-the-badge&logo=Linux" />
 <!--- <img src="https://img.shields.io/pypi/dm/ytconverter?label=PyPI%20Downloads&color=blue&logo=pypi" /> --->
  <img src="https://static.pepy.tech/badge/ytconverter?left_color=black&right_color=brightgreen" />
</p>

---
> **Preface (optional):** A subtle reflection before diving into the technical details, feel free to skip to main content.

|                                                                 |
|-----------------------------------------------------------------|
| **❓ Born from silent hands, shaping what they cannot fully feel.** |
| **❓ Weighted and left alone, with no hand to guide through the quiet.** |
| **❓ Moving the world’s sound, while never feeling its pulse.** |
| <sub>— Author: 401</sub> |
---
`YTConverter™` is a Python-based project developed by [kaifcodec](https://github.com/kaifcodec) designed to provide a robust tool for converting YouTube videos into various formats. This tool simplifies the process of downloading and converting videos from YouTube.

---
## ✅ Features
- *Video Downloading* : Fetch videos directly from YouTube.
- *Audio Downloading*.: Downloads audio of any video with wide range of bitrate selection.
- *Multiple video download*.: Now you can download multiple videos using the tool, just paste the urls one by one.
- *Detailed Quality* : It fetches all the available resolutions for the video and let you select as per your need.
- *Path selections* : It have inbuilt features to detect `Downloads` folder according to what platform user in.
- *Custom Path* : Also you can enter your suitable path for every video.
- *Title sanitization* : It have inbuilt `re` module implementation that converts special characters to text, avoiding errors
- *Format Conversion*.: Convert downloaded videos into different formats such as MP3, MP4, etc.
- *Metadata Handling* : Extract and manage metadata associated with YouTube videos.
- *Colored output* : Colorful terminal output that make it easier to select options.

- Many more features inside try them all...
---
## Screenshots
<p align= "left">
 <img width="1080" height="495" alt="1000132505" src="https://github.com/user-attachments/assets/4087d8e8-5266-4fb0-8135-a51eda1fdcc1" />
</p>
<p align="left">
<img src= "https://github.com/user-attachments/assets/8e9d00ce-b698-4b1f-8870-badd5d274442" width="600" height="600"/>
</p>

---

## Requirements
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)
- ffmpeg & yt-dlp binary

## 🧩 Installation

### 🐧 Linux / Termux / macOS
```bash
git clone https://github.com/kaifcodec/ytconverter.git
cd ytconverter/standalone/
./install.sh # Auto-setup ffmpeg + dependencies
```
### If install.sh fails, install ffmpeg manually
```bash
sudo apt install ffmpeg       # Debian/Ubuntu  
pkg install ffmpeg            # Termux  
sudo dnf install ffmpeg       # Fedora  
sudo pacman -S ffmpeg         # Arch
```
### Install ytconverter from PyPI
```bash
pip install ytconverter
ytconverter -S
```

## ⚙️ Update
### Update ytconverter
```bash
./update.sh # update to new repo, new yt-dlp version 

ytconverter -U # pypi package 

```
## 🪟 Windows
### Clone the repository
```bash
git clone https://github.com/kaifcodec/ytconverter.git
cd ytconverter/standalone/
install.bat # Or manually install ffmpeg and add it to PATH
```
### Then run:
```bash
python3 ytconverter.py
```

---

## Contact
For any questions or feedback, open an issue or write an email on kaifcodec@gmail.com

---

### If you found this tool helpful leave a star that will motivate me to maintain this project and add new features 

<a href="https://www.star-history.com/#kaifcodec/ytconverter&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=kaifcodec/ytconverter&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=kaifcodec/ytconverter&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=kaifcodec/ytconverter&type=date&legend=top-left" />
 </picture>
</a>
---
