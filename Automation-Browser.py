from pynput.keyboard import Key, Controller # pip install pynput
import time 

from Jarvis import take_command

keyboard = Controller()

time.sleep(5)
keyboard.press(Key.ctrl)
keyboard.press('w')
keyboard.release(Key.ctrl)
keyboard.release('w')
