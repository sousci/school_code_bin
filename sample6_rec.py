# 無線を受信してフルカラーLEDを制御
from microbit import *
import radio

radio.on()

while True:
    incoming = radio.receive()

    if incoming == '0':
        pin0.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(0)
    elif incoming == '1':
        pin0.write_digital(0)
        pin1.write_digital(1)
        pin2.write_digital(0)
    elif incoming == '2':
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(1)
