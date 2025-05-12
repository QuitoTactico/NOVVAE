import os
import subprocess
import yt_dlp
import utils


def download_audio_webm(output_dir, video_url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "writethumbnail": True,
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        title = ydl.prepare_filename(info).rsplit(".", 1)[0]
        return title, info


def cut_audio(input_path, output_path, start_time, end_time):
    command = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-ss", start_time,
        "-to", end_time,
        "-c", "copy",
        output_path,
    ]
    subprocess.run(command, check=True)


def convert_to_mp3(input_path, output_path, thumbnail_path, metadata):
    command = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-i", thumbnail_path,
        "-map", "0:a", "-map", "1:v",
        "-c:a", "libmp3lame", "-b:a", "320k",
        "-id3v2_version", "3",
        "-metadata:s:v", "title=Thumbnail",
        "-metadata:s:v", "comment=Cover (front)",
    ]
    for key, value in metadata.items():
        command += ["-metadata", f"{key}={value}"]
    command.append(output_path)
    subprocess.run(command, check=True)


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)


def extract_metadata(info):
    return {
        "title": info.get("title", ""),
        "artist": info.get("uploader", ""),
        "album": info.get("channel", ""),
        "genre": "YouTube",
        "date": info.get("upload_date", ""),
        "comment": info.get("description", ""),
        "description": info.get("description", ""),
        "track": str(info.get("track", "")),
        "composer": info.get("artist", ""),
        "disc": str(info.get("disc_number", "")),
        "publisher": info.get("channel", ""),
    }


if __name__ == "__main__":
    output_dir = utils.folder_selector("OUTPUT")
    video_url = input("Introduce el link del video de YouTube: ").strip()
    start_time = input("Hora de inicio (hh:mm:ss, opcional): ").strip() or None
    end_time = input("Hora de fin (hh:mm:ss, opcional): ").strip() or None

    try:
        base_path, info = download_audio_webm(output_dir, video_url)
        webm_path = base_path + ".webm"
        thumb_path = base_path + ".webp"
        mp3_path = base_path + ".mp3"

        should_cut = bool(start_time and end_time)
        final_audio = webm_path

        if should_cut:
            cut_path = base_path + "_cut.webm"
            cut_audio(webm_path, cut_path, start_time, end_time)
            final_audio = cut_path

        metadata = extract_metadata(info)
        convert_to_mp3(final_audio, mp3_path, thumb_path, metadata)
        print(f"✅ MP3 guardado en: {mp3_path}")

        # Limpieza
        delete_file(webm_path)
        delete_file(thumb_path)
        if should_cut:
            delete_file(cut_path)

    except Exception as e:
        print(f"❌ Error: {e}")
