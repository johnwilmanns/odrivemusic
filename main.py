# This is a sample Python script.
import ODrive_Ease_Lib
import time
import serial
import solenoid
import math
import odrive
import usb.core
from odrive.enums import *
from pynput import keyboard

solenoid.off()

ax, od = ODrive_Ease_Lib.generic_startup()
ax.scuffed_home()
ax.set_pos(5.5)


def hit(number):
    # print("hit " + number)
    pos = 5.5 + (number -1)
    ax.set_pos(pos)
    while abs(pos - ax.get_pos()) > .1:
        print(ax.get_vel())
        time.sleep(.02)
    solenoid.on()
    time.sleep(.05)
    solenoid.off()
def on_press(key):
    print(type(key))
    hit(int(key.char))


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#sadads