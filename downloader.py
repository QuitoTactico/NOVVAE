import os
import yt_dlp
import ffmpeg
import utils


def sanitize_filename(filename):
    """
    Reemplaza los caracteres no permitidos en Windows por guion bajo.
    Caracteres prohibidos en Windows: < > : " / \\ | ? *
    Son exactamente 9 caracteres.
    """
    forbidden_chars = '<>:"/\\|?*'
    for char in forbidden_chars:
        filename = filename.replace(char, '_')
    return filename


def download_audio_webm(output_dir, video_url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "writethumbnail": True,
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        original_filename = ydl.prepare_filename(info).rsplit(".", 1)[0]
        
        # yt-dlp puede sanitizar el nombre automáticamente
        # Verificar qué archivo se descargó realmente
        possible_exts = ['.webm', '.m4a', '.opus', '.mp4']
        actual_audio_file = None
        
        for ext in possible_exts:
            if os.path.exists(original_filename + ext):
                actual_audio_file = original_filename + ext
                break
        
        if not actual_audio_file:
            # Si no se encuentra, buscar con nombre sanitizado
            original_dir = os.path.dirname(original_filename)
            original_basename = os.path.basename(original_filename)
            sanitized_basename = sanitize_filename(original_basename)
            sanitized_filename = os.path.join(original_dir, sanitized_basename)
            
            for ext in possible_exts:
                if os.path.exists(sanitized_filename + ext):
                    actual_audio_file = sanitized_filename + ext
                    original_filename = sanitized_filename
                    break
        
        if not actual_audio_file:
            raise FileNotFoundError(f"No se pudo encontrar el archivo descargado. Buscado: {original_filename}")
        
        # El nombre base sin extensión
        base_name = actual_audio_file.rsplit(".", 1)[0]
        return base_name, info


def cut_audio(input_path, output_path, start_time, end_time):
    """
    Corta un archivo de audio usando ffmpeg-python.
    """
    """
    command = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-ss", start_time,
        "-to", end_time,
        "-c", "copy",
        output_path,
    ]
    subprocess.run(command, check=True)
    """

    try:
        (
            ffmpeg
            .input(input_path, ss=start_time, to=end_time)
            .output(output_path, c='copy')
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        print(f"Error al cortar audio: {e.stderr.decode()}")
        raise


def convert_to_mp3(input_path, output_path, thumbnail_path, metadata):
    """
    Convierte audio a MP3 con thumbnail embebida usando ffmpeg-python.
    Replica: ffmpeg -y -i audio -i thumb -map 0:a -map 1:v -c:a libmp3lame -b:a 320k ...
    """
    """
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
    """

    try:
        # Crear los inputs
        audio_input = ffmpeg.input(input_path)
        thumb_input = ffmpeg.input(thumbnail_path)
        
        # Crear streams de salida
        audio_stream = audio_input.audio
        video_stream = thumb_input.video
        
        # Construir opciones de salida base
        output_options = {
            'c:a': 'libmp3lame',
            'b:a': '320k',
            'id3v2_version': '3',
        }
        
        # Crear el output combinando ambos streams
        stream = ffmpeg.output(
            audio_stream,
            video_stream,
            output_path,
            **output_options
        )
        
        # Agregar metadatos usando global_args (la forma correcta para múltiples metadata)
        for key, value in metadata.items():
            stream = stream.global_args('-metadata', f'{key}={value}')
        
        # Agregar metadata del stream de video
        stream = stream.global_args('-metadata:s:v', 'title=Thumbnail')
        stream = stream.global_args('-metadata:s:v', 'comment=Cover (front)')
        
        # Ejecutar
        ffmpeg.run(stream, overwrite_output=True, capture_stdout=True, capture_stderr=True)
        
    except ffmpeg.Error as e:
        print(f"Error al convertir a MP3: {e.stderr.decode()}")
        raise


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
    start_time = input("Hora de inicio (hh:mm:ss, opcional): ").strip() or 0
    end_time = input("Hora de fin (hh:mm:ss, opcional): ").strip() or None

    try:
        base_path, info = download_audio_webm(output_dir, video_url)
        print(f"📁 Archivo base: {base_path}")
        
        webm_path = base_path + ".webm"
        thumb_path = base_path + ".webp"
        mp3_path = base_path + ".mp3"
        
        print(f"🎵 Audio esperado: {webm_path}")
        print(f"🖼️  Thumbnail esperado: {thumb_path}")
        print(f"🎵 MP3 de salida: {mp3_path}")
        
        # Verificar que los archivos existen
        if not os.path.exists(webm_path):
            print(f"⚠️  Archivo de audio no encontrado: {webm_path}")
            # Buscar archivos en el directorio
            directory = os.path.dirname(base_path)
            basename = os.path.basename(base_path)
            print(f"📂 Archivos en {directory} que contienen '{basename[:20]}':")
            for file in os.listdir(directory):
                if basename[:20] in file:
                    print(f"   - {file}")
            raise FileNotFoundError(f"No se encontró el archivo de audio")
        
        if not os.path.exists(thumb_path):
            print(f"⚠️  Thumbnail no encontrado: {thumb_path}")
            # Intentar con .jpg
            thumb_path_jpg = base_path + ".jpg"
            if os.path.exists(thumb_path_jpg):
                thumb_path = thumb_path_jpg
                print(f"✅ Usando thumbnail .jpg en su lugar")
            else:
                print(f"⚠️  Continuando sin thumbnail")

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
        import traceback
        traceback.print_exc()
