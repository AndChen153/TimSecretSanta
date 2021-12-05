import os
import random
from gpiozero import Button
import time

# playingLED = LED(insert)
playButton = Button(5)

presetAudioButton = Button(6)
cycleVolumeButton = Button(13)
cycleAudioButton = Button(19)
recordAudioButton = Button(26)
buttonSelected = "presetAudioButton"
running = False # if any function is running. used to kill audio processes

volumes = ["-114.00", "-25.00", "-12.00", "-1.00", "6.00"]
iterator = 0
recorded_iterator = 0
# os.system("amixer -c 2 -- sset Speaker playback -5.00dB")

audioFiles = []
for file in os.listdir("./AudioFiles/"):
    if file.endswith(".wav"):
        audioFiles.append(file)

recordedFiles = []
for file in os.listdir("./RecordedFiles/"):
    if file.endswith(".wav"):
        recordedFiles.append(file)

def setButton(buttonName):
    buttonSelected = buttonName
    print(buttonSelected)

while True:
    # if presetAudioButton.is_pressed:
    #     setButton("presetAudioButton")
    # elif cycleVolumeButton.is_pressed:
    #     setButton("cycleVolumeButton")
    # elif cycleAudioButton.is_pressed:
    #     setButton("cycleAudioButton")
    # elif recordAudioButton.is_pressed:
    #     setButton("recordAudioButton")
    # print(running)


    if not running and playButton.is_pressed :
        # if buttonSelected == "presetAudioButton": # preset audio, can cycle through two
        os.system("sudo aplay -D hw:2 ChugJug.wav &")
        time.sleep(0.5)
        running = False



    elif running and playButton.is_pressed:
        print("killed")
        os.system("sudo killall aplay")
        os.system("sudo killall arecord")
        time.sleep(0.5)
        running = False