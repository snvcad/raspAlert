from gpiozero import LED
from gpiozero import Buzzer
from gpiozero import DistanceSensor
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

try:
    distanceSensor = DistanceSensor(GPIO_Distance_Echo, GPIO_Distance_Trg, max_distance=1, threshold_distance=TRIG_DISTANCE)
    while True:
        print("Distance measured :", distanceSensor.distance)
        if distanceSensor.distance < TRIG_DISTANCE:
            bz.on()
            ledR.on()
            ledG.off()
        else:
            bz.off()
            ledR.off()
            ledG.on()
            sleep(1)

except KeyboardInterrupt:
    ledR.off()
    ledG.off()
    bz.off()
    print("Program stopped")



#LED GPIO Pin setting
ledR.on()
sleep(1)
ledR.off()
ledG.on()
sleep(1)
ledG.off()

