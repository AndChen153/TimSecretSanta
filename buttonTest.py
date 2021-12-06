from gpiozero import Button
import os
import time
from playsound import playsound


button = Button(5)

while True:
    if button.is_pressed:
        # wavFile = input("Enter a wav filename: ")
        # Play the wav file
        os.system("sudo python3 ./playwav.py ./ChugJug.wav &")
        time.sleep(0.5)
    else:
        pass
        # print("Button is not pressed")