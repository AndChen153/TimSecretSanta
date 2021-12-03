import os
import random
from gpiozero import Button

# playingLED = LED(insert)
playButton = Button(5)

presetAudioButton = Button(6)
cycleVolumeButton = Button(13)
cycleAudioButton = Button(19)
recordAudioButton = Button(26)
buttonSelected = "presetAudioButton"
running = False # if any function is running. used to kill audio processes

toggle1 = Button(21) #toggle between recording and playing
toggle2 = Button(20)
toggle3 = Button(16)



volumes = ["-114.00", "-25.00", "-12.00", "-1.00", "6.00"]
iterator = 0
recorded_iterator = 0
os.system("amixer -c 2 -- sset Speaker playback -5.00dB")

audioFiles = []
for file in os.listdir("./AudioFiles/"):
    if file.endswith(".wav"):
        audioFiles.append(file)

recordedFiles = []
for file in os.listdir("./RecordedFiles/"):
    if file.endswith(".wav"):
        recordedFiles.append(file)



# print(recordedFiles)
# print(audioFiles)


all_Audio = audioFiles
all_Recorded = recordedFiles
all_Curses = curseWordFiles
# print(all_Audio, all_Recorded)

while (True):
    if len(audioFiles) < 3:
        audioFiles = all_Audio
    if len(recordedFiles) < 3:
        recordedFiles = all_Recorded

    if presetAudioButton.is_pressed:
        buttonSelected = "presetAudioButton"
    elif cycleVolumeButton.is_pressed:
        buttonSelected = "cycleVolumeButton"
    elif cycleAudioButton.is_pressed:
        buttonSelected = "cycleAudioButton"
    elif recordAudioButton.is_pressed:
        buttonSelected = "recordAudioButton"

    if playButton.is_pressed and not running:
        running = True
        if buttonSelected == "cycleAudioButton": # random soundboard
            print(buttonSelected)
            if toggle2.is_pressed:
                print("preset")
                song = audioFiles[random.randrange(0,len(audioFiles))]
                audioFiles.remove(song)
                if (song.startswith("COC")):
                    os.system("amixer -c 2 -- sset Speaker playback 6.00dB")
                    os.system("sudo aplay -D hw:2 ./AudioFiles/\"" + song + "\"")
                else:
                    os.system("sudo aplay -D hw:2 ./AudioFiles/\"" + song + "\" &")
            else:
                if toggle3.is_pressed:
                    print("recorded")
                    song = recordedFiles[random.randrange(0,len(recordedFiles))]
                    recordedFiles.remove(song)
                    os.system("sudo aplay -D hw:2 ./RecordedFiles/\"" + song + "\" &")
                    # print("sudo aplay -D hw:2 recorded.wav")
                else:
                    print("custom")
                    os.system("sudo aplay -D hw:2 customRecordedAudio.wav &")
        elif buttonSelected == "presetAudioButton": # preset audio, can cycle through two
            if toggle2.is_pressed:
                print("ChugJug")
                os.system("sudo aplay -D hw:2 ChugJug.wav &")
            # print("sudo aplay -D hw:2 ChugJug.wav")

        elif buttonSelected == "cycleVolumeButton":
            print("volume cycle")
            if (iterator == 4):
                iterator = 0
            else:
                iterator += 1
            os.system("amixer -c 2 -- sset Speaker playback " + volumes[iterator] +"dB &")
            # print("amixer -c 1 -- sset Master playback " + volumes[iterator] +"dB")

        # elif (selection == "3"):
        #     os.system("sudo arecord -D hw:2 -f S32_LE -r 16000 -c 2 recorded" + str(recorded_iterator) + ".wav &")
        #     recorded_iterator += 1
        #     # print("sudo arecord -D hw:2 -f S32_LE -r 16000 -c 2 recorded.wav")



    if playButton.is_pressed and running:
        running = False
        print("killed")
        os.system("sudo killall aplay")
        os.system("sudo killall arecord")
