import pyautogui
import pytesseract
import os
import sys

from decision_making import algo
from remote import discord, dc_result
from PIL import Image, ImageEnhance, ImageFilter

def screenshot(max):
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
    pic = pyautogui.screenshot(region=(415, 618, 70, 20))
    pic.save('images/tocall.png')

def set_position(max):
    im = Image.open('images/screenshot.png')
    pix = im.load()
    if max == 8:
        r,g,b=pix[193,128+5]
    if max == 6:
        r,g,b=pix[140,177+5]
    if r < 75 and pyautogui.locateOnScreen('images/button/seat.png') != None:
        pyautogui.click('images/button/seat.png')
        print(r)
        if max == 8:
            pyautogui.click(136,175)
        if max == 6:
            pyautogui.click(136,180)

def new_table(max):
    if pyautogui.locateOnScreen('images/button/newtable.png') != None:
        pyautogui.click('images/button/newtable.png')
        set_position(max)

def sit_back():
    if pyautogui.locateOnScreen('images/button/smiley.png') == None:
        pyautogui.click(511,19)
    if pyautogui.locateOnScreen('images/button/sitback.png') != None:
        pyautogui.click('images/button/sitback.png')

def get_max():
    #if (float(get_nplayer(8))/8 > float(get_nplayer(6))/6):
    return (8)
    #else:
    #    return (6)

def get_stack():
    if pyautogui.locateOnScreen('images/button/allin.png') != None:
        pyautogui.click('images/button/allin.png')
    pic = pyautogui.screenshot(region=(534, 619, 120, 18))
    pic.save('images/stack.png')
    return(get_number(read_data('images/stack.png')))

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
    return(nplayer+1)

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
        return('s')
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
    img.save('images/greyscalecard.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    customconf = r'-c tessedit_char_whitelist=AKQJ0123456789 --oem 3 --psm 6'
    string = pytesseract.image_to_string('images/greyscalecard.png', config=customconf)
    if not string:
        return ''
    if (len(string) >= 2 and string[0] == '1' and string[1] == '0'):
        return ('T')
    return (string[0])

def action(bet, act):
    #allin = 0, check = 1, call = 2, fold = 3, bet = 4 
    if pyautogui.locateOnScreen('images/button/allin.png') != None and act == 0:
        pyautogui.click('images/button/allin.png')
        pyautogui.press('enter')
    if pyautogui.locateOnScreen('images/button/raise.png') != None and act == 0:
        pyautogui.click('images/button/raise.png')
    if pyautogui.locateOnScreen('images/button/check.png') != None and (act == 1 or act ==3):
        pyautogui.click('images/button/check.png')
    if pyautogui.locateOnScreen('images/button/fold.png') != None and act == 3:
        pyautogui.click('images/button/fold.png')
    if pyautogui.locateOnScreen('images/button/bet.png') != None and act == 4:
        pyautogui.click('images/button/bet.png')
        pyautogui.write(str(bet), interval=0.25)
        pyautogui.press('enter')
    if pyautogui.locateOnScreen('images/button/call.png') != None and (act == 2 or act == 0 or act == 4):
        pyautogui.click('images/button/call.png')

def init_card(file_name):
    card = Card(file_name)
    if get_symbol(file_name) != 'N':
        card.v = read_card(file_name)
        card.s = get_symbol(file_name)
    return card

def init_data(d, max):
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
    d.stack = get_stack()

def print_data(d):
    print('--------------------')
    print('hand  |     board')
    print(d.card1.v+d.card1.s, d.card2.v+d.card2.s,'|', \
        d.board1.v+d.board1.s, d.board2.v+d.board2.s, \
        d.board3.v+d.board3.s, d.board4.v+d.board4.s, \
        d.board5.v+d.board5.s)
    print('max      : '+str(d.max))
    print('nplayer  : '+str(d.nplayer))
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
    stack = get_stack()

if __name__ == "__main__":
    exit = 0
    if len(sys.argv) > 1 and sys.argv[1] == '-dc':
        dc = 1
    else:
        dc = 0
    pic = pyautogui.screenshot()
    pic.save('images/screenshot.png')
    while exit == 0:
        sit_back()
        max = get_max()
        new_table(max)
        set_position(max)
        screenshot(max)
        if pyautogui.locateOnScreen('images/button/bet.png') != None or pyautogui.locateOnScreen('images/button/fold.png') != None:
            screenshot(max)
            d = Data(max)
            init_data(d, max)
            print_data(d)
            bet, act = algo(d)
            action(bet , act)
        if dc == 1:
            exit = discord()
        if pyautogui.locateOnScreen('images/button/finish.png') != None:
            pic = pyautogui.screenshot(region=(159, 156, 589, 432))
            pic.save('images/result.png')
            if dc == 1:
                dc_result()
            pyautogui.click(509, 482)
            
'''
afer : 
get_max
cmd register
'''
