import yt_dlp


def download_best_audio(playlist_url):
    # Define options for yt_dlp
    ydl_opts = {
        # Download the best available audio quality
        'format': 'bestaudio',

        # Set the output file template: folder will be named after the playlist
        # Files will be named as "<index> - <title>.<ext>"
        'outtmpl': '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',

        # Use FFmpeg to convert the audio to MP3 with 192kbps quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],

        # Additional argument to remove video stream (just in case)
        'postprocessor_args': [
            '-vn'
        ],

        # Show output messages (set to False to suppress output)
        'quiet': False,

        # Enable playlist downloading (not just a single video)
        'noplaylist': False,

        # Skip videos that produce errors instead of stopping the whole process
        'ignoreerrors': True,

        # Do not overwrite existing files
        'nooverwrites': True,
    }

    # Create a YoutubeDL object with the specified options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Start downloading the playlist
        ydl.download([playlist_url])


if __name__ == "__main__":
    # Ask the user to input a YouTube playlist URL in Greek
    url = input("Type YouTube playlist URL: ")
    download_best_audio(url)
