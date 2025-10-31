import pyautogui
import time
time.sleep(3)
                                               # 0 0    300    400
im1= pyautogui.screenshot(region=(0,0,300,400))# x y largura altura

im1.save('imagem2.png')

