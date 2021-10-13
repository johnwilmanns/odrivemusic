
import spidev
import os
from time import sleep
import RPi.GPIO as GPIO

from pidev.Cyprus_Commands import Cyprus_Commands_RPi as cyprus

try:
    cyprus.close_spi()

except:
    pass

spi = spidev.SpiDev()
cyprus.initialize()
def off():
    print("off")
    cyprus.set_pwm_values(1, period_value=100000, compare_value=0,
                          compare_mode=cyprus.LESS_THAN_OR_EQUAL)
def idle():
    print("idle")
    cyprus.set_pwm_values(1, period_value=100000, compare_value=50000,
                          compare_mode=cyprus.LESS_THAN_OR_EQUAL)

def on():
    print("on")
    cyprus.set_pwm_values(1, period_value=100000, compare_value=100000,
                                  compare_mode=cyprus.LESS_THAN_OR_EQUAL)


if __name__ == "__main__":

    for i in range(3):
        off()
        sleep(1)
        on()
        sleep(1)
        idle()
        sleep(1)

    off()
