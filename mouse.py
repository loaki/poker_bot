import pyautogui
import msvcrt

while 1:
    if msvcrt.kbhit():
        exit


    x, y = pyautogui.position()
    pix = pyautogui.screenshot(region=(x, y, 1, 1))
    color = pix.getpixel((0,0))
    print("%d, %d : %s"%(x, y, color))
    #if color[1] == 151:
    #    pyautogui.click()