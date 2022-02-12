from gpiozero import Button
import os
import random
import time
import subprocess
import tempfile


time.sleep(5)

button = Button(5)

cycleVolumeButton = Button(6)
cycleAudioTypeButton = Button(13)
recordButton = Button(12)
cursesButton = Button(16)
buttonNames = ["ChugJug", "Random Audio", "Recorded Audio", "Custom Audio"]


selection = 0
iterator = 0


volumes = ["-114.00", "-25.00", "-12.00", "-1.00", "6.00"]
os.system("amixer -c 0 -- sset Speaker playback -12.00dB")


go = False
recordGo = True


audioFiles = []
all_Audio = []
for file in os.listdir("/home/pi/TimSecretSanta/AudioFiles/"):
    if file.endswith(".wav"):
        audioFiles.append(file)
        all_Audio.append(file)

recordedFiles = []
all_Recorded = []
for file in os.listdir("/home/pi/TimSecretSanta/RecordedFiles/"):
    if file.endswith(".wav"):
        recordedFiles.append(file)
        all_Recorded.append(file)
recorded_iterator = len(recordedFiles)


curseFiles = []
all_Curse = []
for file in os.listdir("/home/pi/TimSecretSanta/CurseFiles/"):
    if file.endswith(".wav"):
        curseFiles.append(file)
        all_Curse.append(file)

# print(all_Audio, all_Recorded)


while True:
    print(len(curseFiles), len(all_Curse))
    if len(audioFiles) < 3:
        audioFiles = all_Audio
    if len(recordedFiles) < 3:
        recordedFiles = all_Recorded
    if len(curseFiles) < 3:
        curseFiles = all_Curse


    if cycleAudioTypeButton.is_pressed:
        if selection > 2:
            selection = 0
        else:
            selection += 1
        print(selection)
        print(buttonNames[selection])
        time.sleep(0.4)


    if cursesButton.is_pressed:
        selection = 10
        print("Curses Audio")
        time.sleep(0.4)


    if cycleVolumeButton.is_pressed:
        if (iterator == 4):
            iterator = 0
        else:
            iterator += 1
        os.system("amixer -c 0 -- sset Speaker playback " + volumes[iterator] +"dB &")
        time.sleep(0.4)


    if recordButton.is_pressed and recordGo:
        os.system("sudo arecord -D hw:0 -f S24_LE -r 16000 -c 2 /home/pi/TimSecretSanta/customRecordedAudio.wav &")
        recorded_iterator += 1
        # os.system("sudo python3 /home/pi/TimSecretSanta/recordwav.py /home/pi/TimSecretSanta/RecordedFiles/recorded" + str(len(recordedFiles)) + ".wav &")
        recordGo = False
        print("recording")
        time.sleep(0.4)
    elif recordButton.is_pressed and not recordGo:
        print("killrecord")
        os.system("sudo killall arecord")
        time.sleep(0.4)
        recordGo = True



    if selection == 0 and go:
        # wavFile = input("Enter a wav filename: ")
        # Play the wav file
        os.system("sudo python3 /home/pi/TimSecretSanta/playwav.py /home/pi/TimSecretSanta/ChugJug.wav &")
        # print("sudo python3 /home/pi/TimSecretSanta/playwav.py /home/pi/TimSecretSanta/ChugJug.wav &")
        time.sleep(0.4)
        go = False
    elif selection == 1 and go:
        song = audioFiles[random.randrange(0,len(audioFiles))]
        audioFiles.remove(song)
        if (song.startswith("COC")):
            os.system("amixer -c 0 -- sset Speaker playback 6.00dB &")
        os.system("sudo python3 /home/pi/TimSecretSanta/playwav.py /home/pi/TimSecretSanta/AudioFiles/\"" + song + "\" &")
        # print("sudo python3 /home/pi/TimSecretSanta/playwav.py /home/pi/TimSecretSanta/AudioFiles/\"" + song + "\" &")
        if (song.startswith("COC")):
            os.system("amixer -c 0 -- sset Speaker playback " + volumes[iterator] +"dB &")
        time.sleep(0.4)
        go = False
    elif selection == 2 and go:
        song = recordedFiles[random.randrange(0,len(recordedFiles))]
        recordedFiles.remove(song)
        os.system("sudo python3 /home/pi/TimSecretSanta/playwav.py /home/pi/TimSecretSanta/RecordedFiles/\"" + song + "\" &")
        # print("sudo python3 /home/pi/TimSecretSanta/playwav.py /home/pi/TimSecretSanta/RecordedFiles/\"" + song + "\" &")
        time.sleep(0.4)
        go = False
    elif selection == 3 and go:
        os.system("sudo aplay -D hw:0 /home/pi/TimSecretSanta/customRecordedAudio.wav &")
        # print("sudo aplay -D hw:0 /home/pi/TimSecretSanta/customRecordedAudio.wav &")
        time.sleep(0.4)
        go = False
    elif selection == 10 and go:
        song = curseFiles[random.randrange(0,len(curseFiles))]
        curseFiles.remove(song)
        os.system("sudo python3 /home/pi/TimSecretSanta/playwav.py /home/pi/TimSecretSanta/CurseFiles/\"" + song + "\" &")
        # print("sudo python3 /home/pi/TimSecretSanta/playwav.py /home/pi/TimSecretSanta/CurseFiles/\"" + song + "\" &")
        time.sleep(0.4)
        go = False
    elif button.is_pressed and not go:
        # os.system("sudo pkill -f playwav.py")
        # ['sudo', 'pkill', '-f','playwav.py']
        p = subprocess.Popen("pgrep -af python", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = str(output, 'UTF-8')
        if "playwav" in output:
            os.system("sudo pkill -f playwav.py")
        else:
            go = True

    # if button.is_pressed:
    #     go = True
    #     time.sleep(0.4)



