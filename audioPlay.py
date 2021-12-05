from gpiozero import Button
import os
import time
import random
import psutil

volumes = ["-114.00", "-25.00", "-12.00", "-1.00", "6.00"]
iterator = 0

button = Button(5)
presetAudioButton = Button(6)
cycleVolumeButton = Button(13)
cycleAudioButton = Button(19)
recordAudioButton = Button(26)
buttonSelected = "presetAudioButton"
toggle1 = Button(21) #toggle between recording and playing
toggle2 = Button(20)
toggle3 = Button(16)

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

def runButton():
    global running
    global iterator
    global audioFiles
    global recordedFiles
    global recorded_iterator
    global iterator
    global volumes
    global buttonSelected

    if button.is_pressed and not running:
        running = True
        if buttonSelected == "presetAudioButton":
            os.system("sudo aplay -D hw:2 ChugJug.wav &")

        elif buttonSelected == "cycleAudioButton":
            song = audioFiles[random.randrange(0,len(audioFiles))]
            audioFiles.remove(song)
            if (song.startswith("COC")):
                os.system("amixer -c 2 -- sset Speaker playback 6.00dB")
            os.system("sudo aplay -D hw:2 ./AudioFiles/\"" + song + "\" &")

        elif buttonSelected == "recordAudioButton":
            if toggle1.is_pressed:
                os.system("sudo arecord -D hw:2 -f S32_LE -r 16000 -c 2 customRecordedAudio.wav &")
            else:
                os.system("sudo aplay -D hw:2 customRecordedAudio.wav &")
        time.sleep(0.4)

    elif cycleVolumeButton.is_pressed:
        if (iterator == 4):
            iterator = 0
        else:
            iterator += 1
        os.system("amixer -c 2 -- sset Speaker playback " + volumes[iterator] + "dB &")
        # print("amixer -c 1 -- sset Master playback " + volumes[iterator] +"dB")

        time.sleep(0.4)

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

while True:

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

    runButton()

    if button.is_pressed and running:
        running = False
        if checkIfProcessRunning("aplay") or checkIfProcessRunning("arecord"):
            os.system("sudo killall aplay")
            os.system("sudo killall arecord")
            time.sleep(0.5)
        else:
            print("else statement")
            runButton()
