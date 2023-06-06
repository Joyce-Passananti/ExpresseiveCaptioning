from os import environ as env

from dotenv import load_dotenv
load_dotenv()

# Put your deepgram key here
DEEPGRAM_KEY = "4a5c16bb21321af4afe4733859e0a404b5978702"

# This is for Windows users
IMAGEMAGIK_LOCATION= r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

CONFIG = {
    "OUTPUT_FPS": 24,
    "AUDIO" : True,
    "VIDEO_CODEC": "libx264",
    "OUTPUT_FILE": "testbrightness.mp4"
}