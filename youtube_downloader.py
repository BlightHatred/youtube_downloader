#!usr/bin/env python

import pytube
import pytube.request
from pytube.cli import on_progress
import configparser
import os 

pytube.request.default_range_size = 262144 

links = []

config = configparser.ConfigParser()
config.read('config.ini')
savepath = config['SAVEPATH']['savepath']


while True:
    link = input('Paste video link, or type "stop" to begin downloading: ')
    if link == 'stop':
        break
    links.append(link)
        


succ = 0
fail = 0
for link in links:
    try:
        ytdata = pytube.YouTube(link, on_progress_callback=on_progress)
        stream = ytdata.streams.get_audio_only()
        stream.download(output_path=savepath)
        filename = stream.default_filename
        filepath = f'{savepath}/{filename}'
        os.rename(filepath, f'{savepath}/{stream.default_filename}.mp3')
        succ += 1
        print(f' {stream.default_filename} download complete.')
    except:
        print('Invalid link, skipping.')
        fail += 1
        continue
print(f'{succ} successful downloads to mp3, {fail} failed.')


        


