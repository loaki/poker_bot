import pyautogui
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

def screenshot():
    pic = pyautogui.screenshot()
    pic.save('images/screenshot.png')
    pic = pyautogui.screenshot(region=(94, 129, 23, 37))
    pic.save('images/card1.png')
    pic = pyautogui.screenshot(region=(117, 129, 23, 37))
    pic.save('images/card2.png')
    pic = pyautogui.screenshot(region=(259, 270, 23, 37))
    pic.save('images/board1.png')
    pic = pyautogui.screenshot(region=(339, 270, 23, 37))
    pic.save('images/board2.png')
    pic = pyautogui.screenshot(region=(419, 270, 23, 37))
    pic.save('images/board3.png')
    pic = pyautogui.screenshot(region=(499, 270, 23, 37))
    pic.save('images/board4.png')
    pic = pyautogui.screenshot(region=(579, 270, 23, 37))
    pic.save('images/board5.png')
    pic = pyautogui.screenshot(region=(420, 380, 130, 25))
    pic.save('images/pot.png')
    pic = pyautogui.screenshot(region=(420, 400, 130, 25))
    pic.save('images/totalpot.png')

#afer : check la position du joueur et son tapis

'''
#mouse pos and pixel color
while 1:
    im = Image.open('images/screenshot.png') # Can be many different formats.
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
    im = Image.open('images/screenshot.png')
    pix = im.load()
    if (max == 8):
        pos = [[380,241],[647,241],[906,241],[1001,444],[909,648],[647,648],[378,648],[290,444]]
    if (max == 6):
        pos = [[134,177],[452,127],[768,177],[767,484],[453,534],[134,484]]
    for i in range (max):
        r,g,b=pix[pos[i][0],pos[i][1]-50]
        if (r+2>b and r-2<b and b+2>g and b-2<g and r > 200):
            nplayer += 1
    return(nplayer)

'''
def get_pos(max):
    im = Image.open('images/screenshot.png')
    pix = im.load()
    #if (max == 8):
        #pos = [[,],[,],[,],[,],[,],[,],[,],[,]]
    #if (max == 6):
        #pos = [[,],[,],[,],[,],[,],[,]]
    for i in range (max):
        r,g,b=pix[pos[i][0],pos[i][1]]
        if (r > 100):
            return (i)
'''

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
pos button 8 | pos button 6
1
2
3
4
5
6
7
8
'''
def get_symbol(file_name):
    im = Image.open(file_name)
    pix = im.load()
    r,g,b=pix[11,35]
    if (r >= 225):
        return('T')
    if (r >= 160):
        return('H')
    if (r >= 64):
        return('C')
    if (r == 0):
        return('A')
    return('N')

def read_data(file_name):
    img = Image.open(file_name).convert('LA')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img.save('images/greyscale.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    customconf = r'--oem 3 --psm 6'
    return(pytesseract.image_to_string('images/greyscale.png', config=customconf))

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
    #set_position()
    screenshot()

    print(get_nplayer(6))
    print('hand\n')
    print(read_data('images/card1.png'))
    print(get_symbol('images/card1.png'))
    print(read_data('images/card2.png'))
    print(get_symbol('images/card2.png'))
    print('board1\n')
    print(read_data('images/board1.png'))
    print(get_symbol('images/board1.png'))
    print('board2\n')
    print(read_data('images/board2.png'))
    print(get_symbol('images/board2.png'))
    print('board3\n')
    print(read_data('images/board3.png'))
    print(get_symbol('images/board3.png'))
    print('board4\n')
    print(read_data('images/board4.png'))
    print(get_symbol('images/board4.png'))
    print('board5\n')
    print(read_data('images/board5.png'))
    print(get_symbol('images/board5.png'))
    print('pot\n')
    print(read_data('images/pot.png'))
    print(read_data('images/totalpot.png'))

