import os
import random

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
print(all_Audio, all_Recorded)

while (True):
    if len(audioFiles) < 3:
        audioFiles = all_Audio
    if len(recordedFiles) < 3:
        recordedFiles = all_Recorded

    selection = str(input("1 - play random audio clip \n2 - play chug jug \n3 - record audio \n4 - play recorded audio \n5 - cycle volume \n6 - kill song playing \n"))
    if (selection == "1"):
        song = audioFiles[random.randrange(0,len(audioFiles))]
        audioFiles.remove(song)
        if (song.startswith("COC")):
            os.system("amixer -c 2 -- sset Speaker playback 6.00dB")
        os.system("sudo aplay -D hw:0 ./AudioFiles/\"" + song + "\" &")
        # print("sudo aplay -D hw:0 ./AudioFiles/" + audioFiles[random.randrange(0,len(audioFiles))])

    elif (selection == "2"):
        os.system("sudo aplay -D hw:0 ChugJug.wav &")
        # print("sudo aplay -D hw:0 ChugJug.wav")

    elif (selection == "3"):
        os.system("sudo arecord -D hw:0 -f S32_LE -r 16000 -c 2 recorded" + str(recorded_iterator) + ".wav &")
        recorded_iterator += 1
        # print("sudo arecord -D hw:0 -f S32_LE -r 16000 -c 2 recorded.wav")

    elif (selection == "4"):
        song = recordedFiles[random.randrange(0,len(recordedFiles))]
        recordedFiles.remove(song)
        os.system("sudo aplay -D hw:0 ./RecordedFiles/\"" + song + "\" &")
        # print("sudo aplay -D hw:0 recorded.wav")

    elif (selection == "5"):
        if (iterator == 4):
            iterator = 0
        else:
            iterator += 1
        os.system("amixer -c 0 -- sset Speaker playback " + volumes[iterator] +"dB &")
        # print("amixer -c 0 -- sset Master playback " + volumes[iterator] +"dB")

    elif (selection == "6"):
        print("killed")
        os.system("sudo killall aplay")
        os.system("sudo killall arecord")