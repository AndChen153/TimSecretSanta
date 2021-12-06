from gpiozero import Button
import os
import random
import time

button = Button(5)
selection = 2

go = True

audioFiles = []
for file in os.listdir("./AudioFiles/"):
    if file.endswith(".wav"):
        audioFiles.append(file)

recordedFiles = []
for file in os.listdir("./RecordedFiles/"):
    if file.endswith(".wav"):
        recordedFiles.append(file)

while True:


    if selection == 1 and button.is_pressed and go:
        # wavFile = input("Enter a wav filename: ")
        # Play the wav file
        os.system("sudo python3 ./playwav.py ./ChugJug.wav &")
        time.sleep(0.5)
        go = False
    elif selection == 2 and button.is_pressed and go:
        song = audioFiles[random.randrange(0,len(audioFiles))]
        audioFiles.remove(song)
        os.system("sudo python3 ./playwav.py ./AudioFiles/\"" + song + "\" &")
        time.sleep(0.5)
        go = False
    elif selection == 3 and button.is_pressed and go:
        song = recordedFiles[random.randrange(0,len(recordedFiles))]
        recordedFiles.remove(song)
        os.system("sudo python3 ./playwav.py ./RecordedFiles/\"" + song + "\" &")
    elif button.is_pressed and not go:
        os.system("sudo killall python3")
        time.sleep(0.5)
        go = True
        # print("Button is not pressed")