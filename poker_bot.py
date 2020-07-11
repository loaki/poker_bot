import pyautogui
import pytesseract
import os

from decision_making import algo
from PIL import Image, ImageEnhance, ImageFilter

max = 8

def screenshot():
    pic = pyautogui.screenshot()
    pic.save('images/screenshot.png')
    if (max == 8):
        pic = pyautogui.screenshot(region=(148, 78, 21, 36))
        pic.save('images/card1.png')
        pic = pyautogui.screenshot(region=(170, 78, 25, 36))
        pic.save('images/card2.png')
    if (max == 6):
        pic = pyautogui.screenshot(region=(94, 130, 21, 36))
        pic.save('images/card1.png')
        pic = pyautogui.screenshot(region=(117, 130, 23, 36))
        pic.save('images/card2.png')
    pic = pyautogui.screenshot(region=(259, 270, 24, 36))
    pic.save('images/board1.png')
    pic = pyautogui.screenshot(region=(339, 270, 24, 36))
    pic.save('images/board2.png')
    pic = pyautogui.screenshot(region=(419, 270, 24, 36))
    pic.save('images/board3.png')
    pic = pyautogui.screenshot(region=(499, 270, 24, 36))
    pic.save('images/board4.png')
    pic = pyautogui.screenshot(region=(579, 270, 24, 36))
    pic.save('images/board5.png')
    pic = pyautogui.screenshot(region=(420, 380, 135, 25))
    pic.save('images/pot.png')
    pic = pyautogui.screenshot(region=(420, 400, 135, 25))
    pic.save('images/totalpot.png')
    pic = pyautogui.screenshot(region=(420, 380, 135, 45))
    pic.save('images/potlarge.png')
    pic = pyautogui.screenshot(region=(415, 618, 70, 20))
    pic.save('images/tocall.png')

def set_position():
    if pyautogui.locateOnScreen('images/button/seat.png') != None:
        pyautogui.click('images/button/seat.png')
    if max == 8:
        pyautogui.click(136,175)
    if max == 6:
        pyautogui.click(136,180)

def new_table():
    if pyautogui.locateOnScreen('images/button/newtable.png') != None:
        pyautogui.click('images/button/newtable.png')
        set_position()

def get_nplayer(max):
    nplayer = 0
    im = Image.open('images/screenshot.png')
    pix = im.load()
    if (max == 8):
        pos = [[197,128],[453,127],[720,127],[807,331],[715,534],[453,534],[195,534],[94,331]]
    if (max == 6):
        pos = [[134,177],[452,127],[768,177],[767,484],[453,534],[134,484]]
    for i in range (1,max):
        r,g,b=pix[pos[i][0],pos[i][1]-50]
        if (r+2>b and r-2<b and b+2>g and b-2<g and r > 200):
            nplayer += 1
        #else:
        #    print('player not found : '+str(i))
    return(nplayer)

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

def get_number(string):
    index_list = []
    del index_list[:]
    for i, x in enumerate(string):
        if x.isdigit() == True:
            index_list.append(i)
    if not index_list:
        return 0
    start = index_list[0]
    end = index_list[-1] + 1
    number = string[start:end]
    return number

def get_symbol(file_name):
    im = Image.open(file_name)
    pix = im.load()
    r,g,b=pix[11,35]
    if (r >= 225):
        return('d')
    if (r >= 160):
        return('h')
    if (r >= 64):
        return('c')
    if (r == 0):
        return('a')
    return('N')

def read_data(file_name):
    img = Image.open(file_name).convert('LA')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img.save('images/greyscale.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    customconf = r'-c tessedit_char_whitelist=.01234567859BB --oem 3 --psm 6'
    return (pytesseract.image_to_string('images/greyscale.png', config=customconf))

def read_card(file_name):
    img = Image.open(file_name).convert('LA')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img.save('images/greyscale.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    customconf = r'-c tessedit_char_whitelist=AKQJ0123456789 --oem 3 --psm 6'
    string = pytesseract.image_to_string('images/greyscale.png', config=customconf)
    if not string:
        return ''
    if (string[0] == '1' and string[1] == '0'):
        return ('T')
    return (string[0])

def action(bet, act):
    #allin = 0, check = 1, call = 2, fold = 3, bet = 4 
    if pyautogui.locateOnScreen('images/button/allin.png') != None and act == 0:
        pyautogui.click('images/button/allin.png')
        pyautogui.press('enter')
    if pyautogui.locateOnScreen('images/button/check.png') != None and (act == 1 or act ==3):
        pyautogui.click('images/button/check.png')
    if pyautogui.locateOnScreen('images/button/call.png') != None and act == 2:
        pyautogui.click('images/button/call.png')
    if pyautogui.locateOnScreen('images/button/fold.png') != None and act == 3:
        pyautogui.click('images/button/fold.png')
    if pyautogui.locateOnScreen('images/button/bet.png') != None and act == 4:
        pyautogui.click('images/button/bet.png')
        pyautogui.write(bet, interval=0.25)
        pyautogui.press('enter')

def init_card(file_name):
    card = Card(file_name)
    if get_symbol(file_name) != 'N':
        card.v = read_card(file_name)
        card.s = get_symbol(file_name)
    return card

def init_data(d):
    d.max = max
    d.nplayer = get_nplayer(max)
    d.card1 = init_card('images/card1.png')
    d.card2 = init_card('images/card2.png')
    d.board1 = init_card('images/board1.png')
    d.board2 = init_card('images/board2.png')
    d.board3 = init_card('images/board3.png')
    d.board4 = init_card('images/board4.png')
    d.board5 = init_card('images/board5.png')
    d.pot = get_number(read_data('images/pot.png'))
    d.tpot = get_number(read_data('images/totalpot.png'))
    d.tocall = get_number(read_data('images/tocall.png'))
    d.stack = 0

def print_data(d):
    print('hand  |     board')
    print(d.card1.v+d.card1.s, d.card2.v+d.card2.s,'|', \
        d.board1.v+d.board1.s, d.board2.v+d.board2.s, \
        d.board3.v+d.board3.s, d.board4.v+d.board4.s, \
        d.board5.v+d.board5.s)
    print('pot      : '+str(d.pot))
    print('tpot     : '+str(d.tpot))
    print('to call  : '+str(d.tocall))
    print('stack    : '+str(d.stack))

class Card():
    v = ''
    s = ''
    def __init__(self, file_name):
        if get_symbol(file_name) != 'N':
            self.v = read_card(file_name)
            self.s = get_symbol(file_name)

class Data():
    def __init__(self, max):
        self.max = max
        self.nplayer = get_nplayer(max)
    card1 = Card('images/card1.png')
    card2 = Card('images/card2.png')
    board1 = Card('images/board1.png')
    board2 = Card('images/board2.png')
    board3 = Card('images/board3.png')
    board4 = Card('images/board4.png')
    board5 = Card('images/board5.png')
    pot = get_number(read_data('images/pot.png'))
    tpot = get_number(read_data('images/totalpot.png'))
    tocall = get_number(read_data('images/tocall.png'))
    stack = 0

if __name__ == "__main__":
    set_position()
    screenshot()
    while pyautogui.locateOnScreen('images/button/finish.png') == None:
        new_table()
        screenshot()
        #d = Data(max)
        #init_data(d)
        #print_data(d)
        #print('\n')
        if pyautogui.locateOnScreen('images/button/bet.png') != None or pyautogui.locateOnScreen('images/button/fold.png') != None:
            screenshot()
            d = Data(max)
            init_data(d)
            print_data(d)
            bet, act = algo(d)
            print(bet, act)
            print('\n')
            action(bet , act)
            
    
#afer : check la position du joueur et son stack
