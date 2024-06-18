#Simple Music Player
from tkinter import *
from winsound import PlaySound
from pygame import mixer
import os

def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()

def pausesong():
    mixer.music.pause()

def stopsong():
    mixer.music.stop()

def resumesong():
    mixer.music.unpause()

root = Tk()
root.title("Music Player")

mixer.init()
playlist = Listbox(root, selectmode=SINGLE, bg = "blue")
playlist.grid(column=5)
os.chdir('song')
song=os.listdir()
for s in song:playlist.insert(END, s)
Button(root,text="play",command=playsong).grid(row=1,column=0)
Button(root,text="pause",command=pausesong).grid(row=1,column=1)
Button(root,text="stop",command=stopsong).grid(row=1,column=2)
Button(root,text="resume",command=resumesong).grid(row=1,column=3)
mainloop()
