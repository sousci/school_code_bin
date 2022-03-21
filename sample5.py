# フルカラーLEDの制御2
from microbit import *

while True:
    pin0.write_digital(1)
    sleep(1000)
    pin0.write_digital(0)
    
    pin1.write_digital(1)
    sleep(1000)
    pin1.write_digital(0)

    pin2.write_digital(1)
    sleep(1000)
    pin2.write_digital(0)
    