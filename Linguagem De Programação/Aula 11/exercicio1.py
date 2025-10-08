import pyautogui
import time

pyautogui.PAUSE = 0.3
print (pyautogui.KEYBOARD_KEYS)
pyautogui.press("win")
time.sleep(2)
pyautogui.write("bloco de notas")
time.sleep(2)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("Bruno" " Dias")
time.sleep(2)
pyautogui.press("alt" "F4")

