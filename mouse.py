import pyautogui
while 1:
    MOUSE_X, MOUSE_Y = pyautogui.position()
    PIXEL = pyautogui.screenshot(region=(MOUSE_X, MOUSE_Y, 1, 1))
    COLOR = PIXEL.getcolors()
    print("%d, %d : %s"%(MOUSE_X, MOUSE_Y, COLOR))