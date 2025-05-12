import os
import yt_dlp
import utils


def download_mp3(output_dir, video_url, start_time=None, end_time=None):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            },
            {"key": "EmbedThumbnail"},
            {"key": "FFmpegMetadata"},
        ],
        "addmetadata": True,
        "writethumbnail": True,
        "embedthumbnail": True,
        "quiet": False,
    }

    if start_time and end_time:
        ydl_opts["download_sections"] = [f"*{start_time}-{end_time}"]

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    output_dir = utils.folder_selector("OUTPUT")
    video_url = input("Introduce el link del video de YouTube: ").strip()
    start_time = input("Hora de inicio (formato hh:mm:ss, opcional): ").strip() or None
    end_time = input("Hora de fin (formato hh:mm:ss, opcional): ").strip() or None

    if download_mp3(output_dir, video_url, start_time, end_time):
        print("Descarga y conversión completadas correctamente.")
    else:
        print("Error durante la descarga o conversión.")
