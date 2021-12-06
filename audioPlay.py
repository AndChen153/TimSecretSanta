from gpiozero import Button
import os
import random
import time

button = Button(5)
cycleVolumeButton = Button(6)
cycleAudioTypeButton = Button(13)
recordButton = Button(12)

selection = 0
iterator = 0

volumes = ["-114.00", "-25.00", "-12.00", "-1.00", "6.00"]
os.system("amixer -c 0 -- sset Speaker playback -12.00dB")

go = True
recordGo = True

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
    if len(audioFiles) < 3:
        audioFiles = all_Audio
    if len(recordedFiles) < 3:
        recordedFiles = all_Recorded

    if cycleAudioTypeButton.is_pressed:
        if selection > 3:
            selection = 0
        else:
            selection += 1
        time.sleep(0.5)

    if cycleVolumeButton.is_pressed:
        if (iterator == 4):
            iterator = 0
        else:
            iterator += 1
        os.system("amixer -c 0 -- sset Speaker playback " + volumes[iterator] +"dB &")
        time.sleep(0.5)

    if recordButton.is_pressed and recordGo:
        recordedFiles = []
        for file in os.listdir("./RecordedFiles/"):
            if file.endswith(".wav"):
                recordedFiles.append(file)
        os.system("sudo arecord -D hw:0 -f S32_LE -r 16000 -c 0 ./RecordedFiles/recorded" + str(len(recordedFiles)) + ".wav &")
        recordGo = False
        time.sleep(0.5)
    elif recordButton.is_pressed and not recordGo:
        os.system("sudo killall arecord")
        time.sleep(0.5)
        recordGo = True

    if selection == 0 and button.is_pressed and go:
        # wavFile = input("Enter a wav filename: ")
        # Play the wav file
        os.system("sudo python3 ./playwav.py ./ChugJug.wav &")
        print("sudo python3 ./playwav.py ./ChugJug.wav &")
        time.sleep(0.5)
        go = False
    elif selection == 1 and button.is_pressed and go:
        song = audioFiles[random.randrange(0,len(audioFiles))]
        audioFiles.remove(song)
        os.system("sudo python3 ./playwav.py ./AudioFiles/\"" + song + "\" &")
        print("sudo python3 ./playwav.py ./AudioFiles/\"" + song + "\" &")
        time.sleep(0.5)
        go = False
    elif selection == 2 and button.is_pressed and go:
        song = recordedFiles[random.randrange(0,len(recordedFiles))]
        recordedFiles.remove(song)
        os.system("sudo python3 ./playwav.py ./RecordedFiles/\"" + song + "\" &")
        print("sudo python3 ./playwav.py ./RecordedFiles/\"" + song + "\" &")
        time.sleep(0.5)
        go = False
    elif selection == 3 and button.is_pressed and go:
        os.system("sudo aplay -D hw:0 customRecordedAudio.wav &")
        print("sudo aplay -D hw:0 customRecordedAudio.wav &")
        time.sleep(0.5)
        go = False
    elif button.is_pressed and not go:
        os.system("sudo killall python3")
        print("sudo killall python3")
        time.sleep(0.5)
        go = True
        # print("Button is not pressed")


