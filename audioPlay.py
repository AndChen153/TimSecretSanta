from gpiozero import Button
import os
import time
import random

button = Button(5)
running = False

audioFiles = []
for file in os.listdir("./AudioFiles/"):
    if file.endswith(".wav"):
        audioFiles.append(file)

recordedFiles = []
for file in os.listdir("./RecordedFiles/"):
    if file.endswith(".wav"):
        recordedFiles.append(file)

all_Audio = audioFiles
all_Recorded = recordedFiles
print(all_Audio, all_Recorded)

while True:
    if button.is_pressed and not running:
        running = True
        song = audioFiles[random.randrange(0,len(audioFiles))]
        audioFiles.remove(song)
        if (song.startswith("COC")):
            os.system("amixer -c 2 -- sset Speaker playback 6.00dB")
        os.system("sudo aplay -D hw:2 ./AudioFiles/\"" + song + "\" &")

        time.sleep(0.5)

    elif button.is_pressed and running:
        running = False
        print("killed")
        os.system("sudo killall aplay")
        os.system("sudo killall arecord")
        time.sleep(0.5)
