import pyautogui
import time

#pyAutogui.moveto(600, 500, duration=2)
#clicar

#pyAutogui.click()


#digitar

#pyAutogui.white("Olá mundo!" , interval= 0.1)


#pressionar tela
#pyAutogui.press()
pyautogui.PAUSE = 0.5
pyautogui.hotkey('win' , 'r')
time.sleep(1)


pyautogui.write("notepad")
pyautogui.press ("enter")

time.sleep(1)

pyautogui.write("Olá, este texto foi digitado automaticamente!", interval=0.07)