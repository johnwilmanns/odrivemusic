from pidev.Cyprus_Commands import Cyprus_Commands_RPi as cyprus
from time import *


cyprus.open_spi()


def off():
    cyprus.set_pwm_values(1, period_value=100000, compare_value=0,
                          compare_mode=cyprus.LESS_THAN_OR_EQUAL)
def idle():
    cyprus.set_pwm_values(1, period_value=100000, compare_value=50000,
                          compare_mode=cyprus.LESS_THAN_OR_EQUAL)

def on():
    cyprus.set_pwm_values(1, period_value=100000, compare_value=100000,
                                  compare_mode=cyprus.LESS_THAN_OR_EQUAL)


if __name__ == "__main__":
    for i in range(10):
        off()
        sleep(1)
        on()
        sleep(.01)

    off()
