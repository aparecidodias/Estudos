import pyautogui
import time
pyautogui.PAUSE = 0.3


#while(True):
   # print(pyautogui.position())
time.sleep(3)
pyautogui.moveTo(994, 408 , duration=2)
pyautogui.click(x=876, y=414 , clicks=2)
pyautogui.write("Wikipedia" , interval=0.5)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=299 , y=295)
