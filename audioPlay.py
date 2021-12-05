from gpiozero import Button
import os
import time

button = Button(5)
running = False

while True:
    if button.is_pressed and not running:
        running = True
        print("preset")
        song = audioFiles[random.randrange(0,len(audioFiles))]
        audioFiles.remove(song)
        if (song.startswith("COC")):
            os.system("amixer -c 2 -- sset Speaker playback 6.00dB")
            os.system("sudo aplay -D hw:2 ./AudioFiles/\"" + song + "\"")
        else:
            os.system("sudo aplay -D hw:2 ./AudioFiles/\"" + song + "\" &")

    elif button.is_pressed and running:
        running = False
        print("killed")
        os.system("sudo killall aplay")
        os.system("sudo killall arecord")
        time.sleep(0.5)
