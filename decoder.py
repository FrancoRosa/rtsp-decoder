from time import sleep
from os import system
system('clear')
while True:
    sleep(5)
    system('omexplayer -o both rtsp//:192.168.1.10:8554/0')
    system('clear')
    print('>> Network error')
    sleep(5)
