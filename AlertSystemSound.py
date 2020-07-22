# Code sample for Buzzer, LED and DistanceSensor by Saji Varghese
from gpiozero import LED
from gpiozero import Buzzer
from gpiozero import DistanceSensor
import pygame
from time import sleep

# Other setting
TRIG_DISTANCE = 0.2

# GPIO Pin setting
GPIO_BZ = 23
GPIO_LedR = 5
GPIO_LedG = 6
GPIO_Distance_Echo = 19
GPIO_Distance_Trg = 26

bz = Buzzer(GPIO_BZ)
ledR = LED(GPIO_LedR)
ledG = LED(GPIO_LedG)

#/usr/share/scratch/Media/Sounds/Vocals/Sing-me-a-song.mp3
#/home/pi/Projects/example.mp3
pygame.init()
pygame.mixer.music.load('/usr/share/scratch/Media/Sounds/Vocals/Sing-me-a-song.mp3')

try:
    distanceSensor = DistanceSensor(GPIO_Distance_Echo, GPIO_Distance_Trg, max_distance=1, threshold_distance=TRIG_DISTANCE)
    while True:
        if distanceSensor.distance < TRIG_DISTANCE:
            print("Distance measured :", distanceSensor.distance)
            bz.on()
            ledR.on()
            ledG.off()
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.stop()
            bz.off()
            ledR.off()
            ledG.on()
            sleep(1)

except KeyboardInterrupt:
    ledR.off()
    ledG.off()
    bz.off()
    print("Program stopped")


