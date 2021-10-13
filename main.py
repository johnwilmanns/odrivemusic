# This is a sample Python script.
import ODrive_Ease_Lib
import time
import serial
import solenoid
import odrive
import usb.core
from odrive.enums import *
from pynput import keyboard


ax, od = ODrive_Ease_Lib.generic_startup()
ax.scuffed_home()

def hit(number):
    # print("hit " + number)
    pos = 5.5 + (number -1)
    ax.set_pos(pos)
    solenoid.on()
    time.sleep(.01)
    solenoid.off()
def on_press(key):
    print(type(key))
    hit(int(key.char))



    #plz forgive me i know this is scuffed
    # if key == "a":
    #     hit(0)
    # elif key == "s":
    #     hit(1)
    # elif key == "d":
    #     hit(2)



with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#sadads