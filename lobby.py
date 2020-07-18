import pyautogui
import pytesseract
import os

from PIL import Image, ImageEnhance, ImageFilter     

def read_t(file_name):
    img = Image.open(file_name).convert('LA')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img.save('images/greyscaledc.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    customconf = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz --oem 3 --psm 6'
    return (pytesseract.image_to_string('images/greyscaledc.png', config=customconf))

def t_screenshot():
    if pyautogui.locateOnScreen('images/lobby/info.png') != None:
        iloc = pyautogui.locateOnScreen('images/lobby/info.png')
        if iloc != None:
            pic = pyautogui.screenshot(region=(iloc[0], iloc[1], 1365, 165))
            pic.save('images/tinfo.png')
        if pyautogui.locateOnScreen('images/discord/shortcut.png') != None:
            pyautogui.click('images/discord/shortcut.png')
        if pyautogui.locateOnScreen('images/discord/shortcut2.png') != None:
            pyautogui.click('images/discord/shortcut2.png')
        if pyautogui.locateOnScreen('images/discord/+.png') != None:
            pyautogui.click('images/discord/+.png', interval = 0.25)
            pyautogui.write('tinfo.png', interval = 0.1)
            pyautogui.press('enter', interval = 0.3)
            pyautogui.press('enter', interval = 0.25)

def t_info():
    if pyautogui.locateOnScreen('images/lobby/mainchat.png') != None:
        pyautogui.click('images/lobby/mainchat.png')
    else:
        pyautogui.click(115, 732)
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
                else:
                    t_screenshot()
        if pyautogui.locateOnScreen('images/lobby/lobby.png') != None:
            pyautogui.click('images/lobby/lobby.png')

def t_check():
    if pyautogui.locateOnScreen('images/lobby/info.png') != None:
        iloc = pyautogui.locateOnScreen('images/lobby/info.png')
        if iloc != None:
            pic = pyautogui.screenshot(region=(iloc[0], iloc[1]+20, 300, 80))
            pic.save('images/tinfo.png')
            if (read_t('images/tinfo.png') == 'Freeroll'):
                return (1)
    return (0)

def t_register():
    if pyautogui.locateOnScreen('images/lobby/mainchat.png') != None:
        pyautogui.click('images/lobby/mainchat.png')
    else:
        pyautogui.click(115, 732)
    if pyautogui.locateOnScreen('images/lobby/name.png') != None:
        nloc = pyautogui.locateOnScreen('images/lobby/name.png')
        for i in range(1,5):
            pyautogui.click(nloc[0], nloc[1]+5+i*22, clicks = 2)
            if pyautogui.locateOnScreen('images/lobby/registerfree.png') != None:
                pyautogui.click('images/lobby/registerfree.png')
                if pyautogui.locateOnScreen('images/lobby/register.png') != None:
                    pyautogui.click('images/lobby/register.png')
            if pyautogui.locateOnScreen('images/lobby/lobby.png') != None:
                pyautogui.click('images/lobby/lobby.png')

    