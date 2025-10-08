import pyautogui
import time
pyautogui.PAUSE = 0.3


#while(True):
   # print(pyautogui.position())
time.sleep(3)
pyautogui.moveTo(1708, 152 , duration=2)

pyautogui.click(x=1761 , y=154)
time.sleep(2)
pyautogui.click(x=1053, y=495)
time.sleep(2)
pyautogui.click(x=1030, y=540)
time.sleep(2)
pyautogui.write("123654pollkk")
pyautogui.click(x=1398, y=691)
