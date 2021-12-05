from gpiozero import Button
import os
import time

button = Button(5)

while True:
    if button.is_pressed:
        os.system("sudo aplay -D hw:2 ChugJug.wav &")
        time.sleep(0.5)
    else:
        print("Button is not pressed")