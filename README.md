
## YTConverter™
<p align="center">
  <img src="https://img.shields.io/badge/Version-3.4.1-blueviolet?style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/github/forks/kaifcodec/ytconverter?style=for-the-badge&logo=git" />
  <img src="https://img.shields.io/github/stars/kaifcodec/ytconverter?style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/github/issues/kaifcodec/ytconverter?style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge" />
</p>

---
`YTConverter™` is a Python-based project developed by [kaifcodec](https://github.com/kaifcodec) designed to provide a robust tool for converting YouTube videos into various formats. This tool simplifies the process of downloading and converting videos from YouTube.

---
![IMG-20250423-WA0001](https://github.com/user-attachments/assets/ef43f4b4-0afa-4682-8c4d-7d19200a40f7)

<p align="centre">
  
  <img src="https://github.com/user-attachments/assets/3f50727f-0927-4b3b-82fa-729c346e66d1" width="600" height ="500" />
</p>

---

## Requirements
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

## Installation (Termux/LinuxOs)

### For Termux:
1. Install Python and update Termux:
   ```bash
   pkg update -y && pkg upgrade -y && pkg install python
   ```
2. Install Git and Curl:
   ```bash
   pkg install git
   pkg install curl
   ```

3. Clone the repository:
   ```bash
   git clone https://github.com/kaifcodec/ytconverter.git
   ```
4. Give storage permission:
   ```bash
   termux-setup-storage
   ```
5. Navigate to the project directory:
   ```bash
   cd ytconverter
   ```
6. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### For Linux (Ubuntu/Debian/Fedora/Arch):
1. Install Python:
   ```bash
   sudo apt update && sudo apt install python3 python3-pip -y  # For Debian/Ubuntu
  
   sudo dnf install python3 python3-pip  # For Fedora
  
   sudo pacman -S python python-pip  # For Arch
   ```
2. Install Git and Curl:
   ```bash
   sudo apt install git curl -y  # Debian/Ubuntu
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/kaifcodec/ytconverter.git
   cd ytconverter
   ```
4. Install required Python libraries:
   ```bash
   pip3 install -r requirements.txt
   ```

## Usage
1. Run the main script to start the conversion process:
   ```bash
   python ytconverter.py
   ```
2. Follow the on-screen instructions to input the YouTube URL and choose the desired output format.

## Tested on
- Linux
- Termux
- Ubuntu
- MacOs

---
 <p align="left">
<img src= "https://github.com/user-attachments/assets/8e9d00ce-b698-4b1f-8870-badd5d274442" width="600" height="600"/>
</p>

---

<p align="center">
  <b>Click on the image below to watch the demo and installation on YouTube</b>
  <a href="https://youtu.be/W2Evqs3fqHs" target="_blank">
    <img src="https://img.youtube.com/vi/W2Evqs3fqHs/hqdefault.jpg" alt="Watch the demo" style="max-width: 100%;">
  </a>
</p>

<p align="center">
  
</p>

---

## Contact for any error or issue:
- kaifcodec@gmail.com

## Features
- **Video Downloading**: Fetch videos directly from YouTube.
- **Multiple video download**: Now you can download multiple videos using the tool, just paste the urls one by one
- **Format Conversion**: Convert downloaded videos into different formats such as MP3, MP4, etc.
- **Metadata Handling**: Extract and manage metadata associated with YouTube videos.

---



## Contributing

Contributions, issues, and feature requests are welcome!

Please take a moment to read our [CONTRIBUTING.md](CONTRIBUTING.md) guide for details on how to help make **YTConverter™** better.

Feel free to open a pull request or submit an issue.

## Disclaimer ⚠⚠
 - **We do ask you for your Name and Contact information at the beginning of the tool for update-related notices, but if you don't want to disclose those creds, you can leave those fields blank**
 - **We also collect some basic information about the usage statistics and the user's Public IP, but we assure you that this data is not kept more than 48 hours**
 - **We respect your privacy. Any basic info this tool collects (like usage data) is handled securely and never shared. No creepy tracking—just good software.**
 - _Thank you 🌹🌹_ _Keep supporting ❤❤_

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please open an issue or contact [kaifcodec](https://github.com/kaifcodec).


---
