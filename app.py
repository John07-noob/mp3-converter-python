# This project created by John07-noob
# Sep/14/2020

from moviepy.editor import *
from moviepy.editor import VideoFileClip

print("Welcome to mp3 converter")
path = input("Please put your mp4 path in here: ")
mp3_name = input("What the name of covert file be?: ")

# Put the path and name inside this vars
mp4_file = (path)
mp3_file = (mp3_name)

# Put the vars in the object for converting
videofile = VideoFileClip(mp4_file)
audiofile = videofile.audio
audiofile.write_audiofile(mp3_file)
audiofile.close()
videofile.close()