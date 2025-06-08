# 🎵 YouTube Playlist MP3 Downloader

A Python script that downloads the **best quality audio** from a **YouTube playlist** and converts it to high-quality **MP3 (192kbps)** using `yt-dlp` and `ffmpeg`.

---

## 🚀 Features

* ✅ Downloads **entire playlists**
* 🎷 Extracts **only the best audio track**
* ♻️ Automatically converts audio to **MP3 (192kbps)**
* 📂 Organizes files in folders by **playlist name**
* 📌 Skips broken/unavailable videos (no interruptions)
* 🔒 Avoids overwriting existing files

---

## 💠 Requirements

* Python 3.7+
* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
* [`ffmpeg`](https://ffmpeg.org/)

### Install Requirements

```bash
pip install yt-dlp
```

Make sure `ffmpeg` is installed and accessible from your system's PATH.

---

## 📥 Usage

1. **Clone this repository:**

```bash
git clone https://github.com/yourusername/youtube-playlist-mp3-downloader.git
cd youtube-playlist-mp3-downloader
```

2. **Run the script:**

```bash
python downloader.py
```

3. **Paste your YouTube playlist URL when prompted:**

```
𝕓άλε το URL της YouTube playlist:
```

The downloaded MP3 files will be saved in a folder named after the playlist, with filenames formatted like this:

```
<Playlist Name>/<Index> - <Video Title>.mp3
```

---

## 📂 Output Example

```
My Favorite Songs/
├── 01 - Song One.mp3
├── 02 - Song Two.mp3
├── ...
```

---

## ❗ Notes

* If a video is geo-blocked or unavailable, the script will **skip it** automatically.
* The script does **not** download videos—**only audio** is saved.

---