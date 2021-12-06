from gpiozero import Button
import os
import time

button = Button(5)
go = True
while True:
    if button.is_pressed and go:
        # wavFile = input("Enter a wav filename: ")
        # Play the wav file
        os.system("sudo python3 ./playwav.py ./ChugJug.wav &")
        time.sleep(0.5)
        go = False
    elif button.is_pressed and not go:
        os.system("sudo killall python3")
        # print("Button is not pressed")