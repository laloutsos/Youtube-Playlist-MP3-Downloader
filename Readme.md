# 🎵 YouTube Playlist MP3 Downloader

This is a simple Python GUI application that allows you to download the **best audio tracks** (in MP3 format) from a **YouTube playlist**. The program uses `yt-dlp` for downloading and `tkinter` for the graphical interface.

## ✨ Features

* 🎙️ Downloads high-quality MP3 audio from any YouTube playlist.
* 📁 Lets you choose your preferred download folder.
* 🚀 Easy-to-use graphical interface.
* ✅ Skips errors and continues downloading the rest of the playlist.
* 🌟 Automatically names the files based on playlist order and video title.

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

* Python 3.x
* `yt-dlp`
* `ffmpeg`

To install the required Python package:

```bash
pip install yt-dlp
```

Make sure `ffmpeg` is installed and added to your system PATH. You can download it from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

## 📚 How to Use

1. Run the script:

   ```bash
   python your_script_name.py
   ```

2. Enter a valid YouTube **playlist** URL.

3. Click on **"Choose Download Folder"** and select your target directory.

4. Click **"Download MP3s"**.

5. Sit back and let it fetch the best quality audio from the playlist!

## 👍 Example Output

Downloaded files will be named like this:

```
1 - First Song Title.mp3
2 - Second Song Title.mp3
...
```

## 🌐 Technologies Used

* Python
* tkinter
* yt-dlp
* ffmpeg

