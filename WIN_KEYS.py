import pywinauto
from pywinauto.keyboard import send_keys, KeySequenceError
import time

while True:
    time.sleep(20)
    send_keys("{VK_LWIN}") # cmd kb.
