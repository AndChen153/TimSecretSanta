import os
os.system("amixer -c 0 -- sset Speaker playback -25.00dB")
os.system("sudo python3 /home/pi/TimSecretSanta/audioPlay.py")