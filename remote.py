import pyautogui
import pytesseract
import os

from lobby import t_info, t_register
from PIL import Image, ImageEnhance, ImageFilter

def read_cmd(file_name):
    img = Image.open(file_name).convert('L')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img = img.filter(ImageFilter.GaussianBlur(radius = 0.1))
    img.save('images/greyscaledc.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    customconf = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --oem 3 --psm 6'
    return (pytesseract.image_to_string('images/greyscaledc.png', config=customconf))

def dc_write(string):
    if pyautogui.locateOnScreen('images/discord/cmd.png') != None:
        pyautogui.click('images/discord/cmd.png')
    if pyautogui.locateOnScreen('images/discord/write.png') != None:
        pyautogui.click('images/discord/write.png')
        pyautogui.write(string)
        pyautogui.press('enter')

def dc_screenshot():
    if pyautogui.locateOnScreen('images/discord/screenshot.png') != None:
        pyautogui.click('images/discord/screenshot.png')
        if pyautogui.locateOnScreen('images/discord/+.png') != None:
            pyautogui.click('images/discord/+.png', interval = 0.25)
            pyautogui.write('screenshot.png')
            pyautogui.press('enter', interval = 0.25)
            pyautogui.press('enter', interval = 0.25)

def dc_result():
    if pyautogui.locateOnScreen('images/discord/results.png') != None:
        pyautogui.click('images/discord/results.png')
        if pyautogui.locateOnScreen('images/discord/+.png') != None:
            pyautogui.click('images/discord/+.png', interval = 0.25)
            pyautogui.write('result.png')
            pyautogui.press('enter', interval = 0.25)
            pyautogui.press('enter')
    if pyautogui.locateOnScreen('images/lobby/mainchat.png') != None:
        pyautogui.click('images/lobby/mainchat.png')
    else:
        pyautogui.click(115, 732)
    if pyautogui.locateOnScreen('images/lobby/lobby.png') != None:
        pyautogui.click('images/lobby/lobby.png')
    pic = pyautogui.screenshot()
    pic.save('images/lobby.png')
    im = Image.open('images/lobby.png')
    pix = im.load()
    if pyautogui.locateOnScreen('images/lobby/lobbys.png') != None:
        lloc = pyautogui.locateOnScreen('images/lobby/lobbys.png')
        for i in range(1,5):
            r,g,b=pix[int(lloc[0]+i*177),int(lloc[1])]
            if (r > 60):
                pyautogui.click(lloc[0]+i*177, lloc[1])
                if pyautogui.locateOnScreen('images/lobby/finalpos.png') != None or t_check() == 0:
                    pyautogui.doubleClick(lloc[0]+i*177+147, lloc[1]+8, interval = 0.25)
        if pyautogui.locateOnScreen('images/lobby/lobby.png') != None:
            pyautogui.click('images/lobby/lobby.png')

def discord(d):
    if pyautogui.locateOnScreen('images/discord/cancel.png') != None:
        pyautogui.click('images/discord/cancel.png')
    if pyautogui.locateOnScreen('images/discord/shortcut.png') != None:
        pyautogui.click('images/discord/shortcut.png')
    if pyautogui.locateOnScreen('images/discord/shortcut2.png') != None:
        pyautogui.click('images/discord/shortcut2.png')
    if pyautogui.locateOnScreen('images/discord/server.png') != None:
        pyautogui.click('images/discord/server.png')
    if pyautogui.locateOnScreen('images/discord/cmd.png') != None:
        pyautogui.click('images/discord/cmd.png')
    if pyautogui.locateOnScreen('images/discord/write.png') != None:
        wloc = pyautogui.locateOnScreen('images/discord/write.png')
        if wloc != None:
            pic = pyautogui.screenshot(region=(wloc[0]-10, wloc[1]-70, 120, 25))
            pic.save('images/cmd.png')
            cmd = read_cmd('images/cmd.png')
            #print(cmd)
            if cmd == 'screenshot':
                dc_write('ok')
                dc_screenshot()
            if cmd == 'info':
                dc_write('ok')
                t_info()
            if cmd == 'autoregister':
                d.auto_register ^= 1
                if d.auto_register == 1:
                    dc_write('on')
                if d.auto_register == 0:
                    dc_write('off')
            if d.auto_register == 1:
                t_register()
            if cmd == 'register':
                dc_write('ok')
                t_register()
            if (cmd == 'stop' or cmd == 'Stop'):
                dc_write('ok')
                return (1, d.auto_register)
    return (0, d.auto_register)