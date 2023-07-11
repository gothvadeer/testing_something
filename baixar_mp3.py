from pytube import YouTube
import moviepy.editor as me
import re
import os
from pathlib import Path

link = input('Cole o link do vídeo: ')
yt = YouTube(link)
downloads_path = Path.home() / 'Downloads'

print('Aguarde um momento...')
youtube = yt.streams.filter(only_audio=True).first().download(str(downloads_path))
print('Convertendo...')

for file in os.listdir(downloads_path):
    if re.search('mp4', file):
        mp4_caminho = os.path.join(downloads_path, file)
        mp3_caminho = os.path.join(downloads_path, os.path.splitext(file)[0]+'.mp3')
        new_file = me.AudioFileClip(mp4_caminho)
        new_file.write_audiofile(mp3_caminho)
        os.remove(mp4_caminho)
print('Processo finalizado')
