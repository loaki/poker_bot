import pyautogui
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

def screenshot():
    pic = pyautogui.screenshot()
    pic.save('screenshot.png')
    pic = pyautogui.screenshot(region=(94, 129, 22, 37))
    pic.save('card1.png')
    pic = pyautogui.screenshot(region=(117, 129, 22, 37))
    pic.save('card2.png')

#afer : check le button dealer checker le nb de joueur dans le coup

'''
#mouse pos and pixel color
while 1:
    im = Image.open('screenshot.png') # Can be many different formats.
    pix = im.load()
    x,y = pyautogui.position()
    r,g,b=pix[x,y]
    print(x,y)
    print(r,g,b)
'''


def set_position():
    if pyautogui.locateOnScreen('images/button/seat.png') != None:
        pyautogui.click('images/button/seat.png')
    pyautogui.click(136,182)

def get_nplayer(max):
    nplayer = 0
    im = Image.open('screenshot.png')
    pix = im.load()
    if (max == 8):
        pos = [[380,241],[647,241],[906,241],[1001,444],[909,648],[647,648],[378,648],[290,444]]
    if (max == 6):
        pos = [[134,177],[452,127],[768,177],[767,484],[453,534],[134,484]]
    for i in range (max):
        r,g,b=pix[pos[i][0],pos[i][1]]
        if (r+5>b and r-5<b and b+5>g and b-5<g):
            nplayer += 1
    return(nplayer)


'''
pos 8players | pos 6players
1 380  241      134  177
2 647  241      452  127
3 906  241      768  177
4 1001 444      767  484
5 909  648      453  534
6 647  648      134  484
7 378  648
8 290  444
'''

def read_data(file_name):
    img = Image.open(file_name).convert('LA')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img.save('images/test/greyscale.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    customconf = r'--oem 3 --psm 6'
    return(pytesseract.image_to_string('images/test/greyscale.png', config=customconf))

def action(bet, act):
    #allin = 0, check = 1, call = 2, fold = 3, bet = 4 
    if pyautogui.locateOnScreen('images/button/allin.png') != None and act == 0:
        pyautogui.click('images/button/allin.png')
    if pyautogui.locateOnScreen('images/button/check.png') != None and act == 1:
        pyautogui.click('images/button/check.png')
    if pyautogui.locateOnScreen('images/button/call.png') != None and act == 2:
        pyautogui.click('images/button/call.png')
    if pyautogui.locateOnScreen('images/button/fold.png') != None and act == 3:
        pyautogui.click('images/button/fold.png')
    if pyautogui.locateOnScreen('images/button/bet.png') != None and act == 4:
        pyautogui.click('images/button/bet.png')
        pyautogui.write(bet, interval=0.25)
        pyautogui.press('enter')


if __name__ == "__main__":
    screenshot()
    #set_position()
    print(get_nplayer(6))
    print(read_data('card1.png'))
    print(read_data('card2.png'))