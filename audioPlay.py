from gpiozero import Button
import os
import time

button = Button(5)
running = False

while True:
    if button.is_pressed and not running:
        running = True
        os.system("sudo aplay -D hw:2 ChugJug.wav &")
        time.sleep(0.5)

    elif button.is_pressed and running:
        running = False
        print("killed")
        os.system("sudo killall aplay")
        os.system("sudo killall arecord")
        time.sleep(0.5)
