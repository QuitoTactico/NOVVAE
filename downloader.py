import os
import yt_dlp

# Ruta de descarga
output_dir = r'C:\Users\Esteban\Downloads\Música\-Novo 12-'

# Función para descargar y convertir a MP3
def download_mp3(video_url):
    # Opciones de configuración para yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Descargar solo el mejor audio disponible
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Guardar con el título del video
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convertir a mp3
            'preferredquality': '320',  # Mejor calidad posible (320 kbps)
        }],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])  # Descargar el video
        return True  # Si todo salió bien, retornar True
    except Exception as e:
        print(f"Error: {e}")  # En caso de error, mostrar el error
        return False  # Retornar False si ocurrió un problema

# Solicitar el link del video por consola
video_url = input("Introduce el link del video de YouTube: ")

# Llamar a la función de descarga y mostrar si tuvo éxito
if download_mp3(video_url):
    print("Descarga y conversión completadas correctamente.")
else:
    print("Error durante la descarga o conversión.")
