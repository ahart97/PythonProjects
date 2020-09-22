rom picamera import PiCamera
from time import sleep
import os

camera = PiCamera()

action = 'start'
length = 0

camera.resolution = (1280,720)
camera.framerate = 30

camera.start_preview(fullscreen = False, window = (0,0,1280,720))
camera.annotate_text = "Type anything and hit enter to exit"


action = input()


camera.stop_preview()
