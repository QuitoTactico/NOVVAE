import os
import yt_dlp

output_dir = r"C:\Users\Esteban\Downloads\Música\-Novo 12-"


def download_mp3(video_url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


video_url = input("Introduce el link del video de YouTube: ")

if download_mp3(video_url):
    print("Descarga y conversión completadas correctamente.")
else:
    print("Error durante la descarga o conversión.")
