import pyautogui
import pytesseract
import os

from lobby import t_info, t_register
from PIL import Image, ImageEnhance, ImageFilter

def read_cmd(file_name):
    img = Image.open(file_name).convert('LA')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img.save('images/greyscaledc.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    customconf = r'-c tessedit_char_whitelist=ABCDEFHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz --oem 3 --psm 6'
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
            pyautogui.press('enter')

def dc_result():
    if pyautogui.locateOnScreen('images/discord/results.png') != None:
        pyautogui.click('images/discord/results.png')
        if pyautogui.locateOnScreen('images/discord/+.png') != None:
            pyautogui.click('images/discord/+.png', interval = 0.25)
            pyautogui.write('result.png')
            pyautogui.press('enter', interval = 0.25)
            pyautogui.press('enter')

def discord():
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
            if (cmd == 'screenshot' or cmd == 'Screenshot'):
                dc_write('ok')
                dc_screenshot()
            if (cmd == 'info' or cmd == 'Info'):
                dc_write('ok')
                t_info()
            if (cmd == 'register' or cmd == 'Register'):
                dc_write('ok')
                t_register()
            if (cmd == 'stop' or cmd == 'Stop'):
                dc_write('ok')
                return (1)
    return (0)