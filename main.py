#!/usr/bin/env python3
import glob

path = input("enter the path the playlists are in: ")


class Playlist:

    def __init__(self, file):
        self.file = file
        self.name = file.split('\\')[-1].strip(".m3u8").strip('m3u')
        self.weight = 0
        self.content = open(file, 'r').read().split('\n')
        self.content.pop(0)

    def set_weight(self):
        print(f"how weighted should {self.name} be?")
        self.weight = int(input(">> "))


playlistfiles = glob.glob(f"{path}/*.m3u*")
playlists = [Playlist(file) for file in playlistfiles]

print(f"{len(playlistfiles)} playlist(s) found")
for playlist in playlists:
    playlist.set_weight()

new_file = ['#EXTM3U']
for playlist in playlists:
    if playlist.weight:
        for i in range(playlist.weight):
            for line in playlist.content:
                new_file.append(line)

new_file_name = input("enter a playlist name\n>> ")
new_full_file_name = f"{path}\{new_file_name}.m3u8"

with open(new_full_file_name, 'w') as file:
    for line in new_file:
        file.write(f"{line}\n")
