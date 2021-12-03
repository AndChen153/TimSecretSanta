import os
import random

volume = 50

audioFiles = []
for file in os.listdir("./AudioFiles/"):
    if file.endswith(".wav"):
        audioFiles.append(file)

print(audioFiles)

# while (True):
selection = input("1 - play random audio clip \n2 - play chug jug \n3 - record audio \n4 - play recorded audio \n5 - cycle volume \n")
if (selection == "1"):
    os.system("sudo aplay -D hw:2 ./AudioFiles/" + audioFiles[random.randrange(0,len(audioFiles))])
    # print("sudo aplay -D hw:2 ./AudioFiles/" + audioFiles[random.randrange(0,len(audioFiles))])
elif (selection == "2"):
    os.system("sudo aplay -D hw:2 ./AudioFiles/ChugJug.wav")
    # print("sudo aplay -D hw:2 ./AudioFiles/ChugJug.wav")
elif (selection == "3"):
    os.system("sudo arecord -D hw:2 -f S32_LE -r 16000 -c 2 recorded.wav")
    # print("sudo arecord -D hw:2 -f S32_LE -r 16000 -c 2 recorded.wav")
elif (selection == "4"):
    os.system("sudo aplay -D hw:2 recorded.wav")
    # print("sudo aplay -D hw:2 recorded.wav")
elif (selection == "5"):
    if (volume == 100):
        volume = 0
    else:
        volume += 25
    os.system("sudo amixer -c 2 set Master " + str(volume) + "%")
    # print("sudo amixer -c 2 set Master " + str(volume) + "%")