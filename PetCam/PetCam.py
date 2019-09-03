from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()

action = 'start'
length = 0

camera.resolution = (1640,922)
camera.framerate = 30

camera.start_preview()
camera.preview.fullscreen = False
camera.preview.window = (10,10,500,500)
camera.annotate_text = "Bailey Cam"

while action != 'stop':
    os.system('clear')
    print('Commands: image, video, stop\n')
    print('Command ->')
    action = input()

    if action == 'image':
        camera.capture('/home/pi/Desktop/image.jpg')

    elif action == 'video':
        print('How long would you like to record for (seconds):')
        length = input()

        camera.start_recording('/home/pi/Desktop/video.h264')
        sleep(int(length))
        camera.stop_recording()

camera.stop_preview()

