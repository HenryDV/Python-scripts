from pytube import YouTube
video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
yt = YouTube(video_url)
print('Título:', yt.title)
print('Duración:', yt.length, 'segundos')
# Descargar video en la resolución más alta disponible
# Descargar video en la resolución más alta disponible
video = yt.streams.get_highest_resolution()

# Descargar video en formato MP4
video = yt.streams.filter(file_extension='mp4').first()
video.download('/ruta/de/destino/')
