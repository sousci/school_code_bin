# ボタンを押したら無線通信
from microbit import *
import radio

radio.on()

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("AB")
        radio.send('2')
        break
    elif button_a.is_pressed():
        display.scroll("A")
        radio.send('0')
    elif button_b.is_pressed():
        display.scroll("B")
        radio.send('1')
        
    sleep(100)
