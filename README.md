## YTConverter™
<p align="center">
  <img src="https://img.shields.io/badge/Version-4.0.2-blueviolet?style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/github/forks/kaifcodec/ytconverter?style=for-the-badge&logo=git" />
  <img src="https://img.shields.io/github/stars/kaifcodec/ytconverter?style=for-the-badge&logo=github" />
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
![file_000000006dfc61fb9c9a2cb865da0157](https://github.com/user-attachments/assets/eadca26f-79a7-4233-90dd-1c850f50a8cc)
---

## Screenshots
<p align= "left">
 <img width="1004" height="469" alt="1000122247" src="https://github.com/user-attachments/assets/80269ce0-1443-4dc4-836f-3bf63905879b" />
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
# Clone the repository
git clone https://github.com/kaifcodec/ytconverter.git
cd ytconverter/standalone/

# Auto-setup ffmpeg + dependencies
./install.sh

# (If install.sh fails, install ffmpeg manually)
sudo apt install ffmpeg       # Debian/Ubuntu  
pkg install ffmpeg            # Termux  
sudo dnf install ffmpeg       # Fedora  
sudo pacman -S ffmpeg         # Arch

# Install ytconverter from PyPI
pip install ytconverter

# Run the program
ytconverter -S


### ⚙️ Update
# Update the repository
./update.sh

# Update PyPI package
pip install -U ytconverter


### 🪟 Windows
# Clone the repository
git clone https://github.com/kaifcodec/ytconverter.git
cd ytconverter/standalone/

# Run installer
install.bat

# Or manually install ffmpeg and add it to PATH
# Then run:
python ytconverter.py

⚠️ The standalone script is recommended for now.  
PyPI version is still in beta — report issues on GitHub.
---

## Tested on
- Linux
- Termux
- Ubuntu
- MacOs
- Windows 10/11

---



## Contact for any error or issue:
- kaifcodec@gmail.com

## Features
- **Video Downloading**: Fetch videos directly from YouTube.
- **Audio Downloading**: Downloads audio of any video with wide range of bitrate selection.
- **Multiple video download**: Now you can download multiple videos using the tool, just paste the urls one by one
- **Format Conversion**: Convert downloaded videos into different formats such as MP3, MP4, etc.
- **Metadata Handling**: Extract and manage metadata associated with YouTube videos.

---



## Contributing

Contributions, issues, and feature requests are welcome!

Please take a moment to read our [CONTRIBUTING.md](CONTRIBUTING.md) guide for details on how to help make **YTConverter™** better.

Feel free to open a pull request or submit an issue.


---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please open an issue or contact [kaifcodec](https://github.com/kaifcodec).

# If you found this tool helpful leave a star that will motivate me to maintain this project and add new features 
---
## Stars ⭐ 
[![Star History Chart](https://api.star-history.com/svg?repos=kaifcodec/ytconverter&type=Date)](https://star-history.com/#kaifcodec/ytconverter&Date)
---
