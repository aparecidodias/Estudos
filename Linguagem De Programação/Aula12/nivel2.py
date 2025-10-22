import pyautogui
import time

pyautogui.PAUSE = 0.3
print (pyautogui.KEYBOARD_KEYS)

pyautogui.press("win")
time.sleep(2)


pyautogui.write("bloco de notas")
time.sleep(2)


pyautogui.press("enter")
time.sleep(2)


pyautogui.write("automatizando com PyAutogui e divertido ", interval=0.2)
time.sleep(5)

