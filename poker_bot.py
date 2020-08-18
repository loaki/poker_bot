import pyautogui
import pytesseract
import os
import sys
import shutil
import time
import msvcrt

from decision_making import algo
from remote import discord, dc_result
from PIL import Image, ImageEnhance, ImageFilter

secure = 1

def screenshot(max):
    pic = pyautogui.screenshot()
    pic.save('images/screenshot.png')
    if (max == 8):
        pic = pyautogui.screenshot(region=(410, 78, 24, 35))
        pic.save('images/card1.png')
        pic = pyautogui.screenshot(region=(435, 78, 25, 35))
        pic.save('images/card2.png')
    if (max == 6):
        pic = pyautogui.screenshot(region=(410, 79, 24, 35))
        pic.save('images/card1.png')
        pic = pyautogui.screenshot(region=(434, 79, 26, 35))
        pic.save('images/card2.png')
    pic = pyautogui.screenshot(region=(259, 271, 28, 35))
    pic.save('images/board1.png')
    pic = pyautogui.screenshot(region=(339, 271, 28, 35))
    pic.save('images/board2.png')
    pic = pyautogui.screenshot(region=(419, 271, 28, 35))
    pic.save('images/board3.png')
    pic = pyautogui.screenshot(region=(499, 271, 28, 35))
    pic.save('images/board4.png')
    pic = pyautogui.screenshot(region=(579, 271, 28, 35))
    pic.save('images/board5.png')
    pic = pyautogui.screenshot(region=(470, 380, 80, 25))
    pic.save('images/pot.png')
    pic = pyautogui.screenshot(region=(418, 402, 150, 21))
    pic.save('images/totalpot.png')
    pic = pyautogui.screenshot(region=(400, 620, 85, 17))
    pic.save('images/tocall.png')
    pic = pyautogui.screenshot(region=(409, 153, 80, 25))
    pic.save('images/stack.png')

def set_position(max):
    im = Image.open('images/screenshot.png')
    pix = im.load()
    if max == 8:
        r,g,b=pix[457,127+5]
    if max == 6:
        r,g,b=pix[457,127+5]
    #print (r,g,b)
    #pyautogui.click(457,127+5)
    if r < 95 and pyautogui.locateOnScreen('images/button/seat.png') != None:
        pyautogui.click('images/button/seat.png')
        #print(r)
        if max == 8:
            pyautogui.click(457,132)
        if max == 6:
            pyautogui.click(457,127+5)

def new_table(max):
    if pyautogui.locateOnScreen('images/button/newtable.png') != None:
        pyautogui.click('images/button/newtable.png')
        set_position(max)

def sit_back():
    if pyautogui.locateOnScreen('images/button/smiley.png') == None:
        pyautogui.click(511,19)
    if pyautogui.locateOnScreen('images/button/sitback.png') != None:
        pyautogui.click('images/button/sitback.png')

def log_in(psw):
    if pyautogui.locateOnScreen('images/button/disconnect.png') != None:
        pyautogui.click('images/button/disconnect.png')
    if pyautogui.locateOnScreen('images/button/login.png') != None:
        pyautogui.click(115, 732)
        if pyautogui.locateOnScreen('images/button/psw.png') != None:
            pyautogui.click('images/button/psw.png')
            pyautogui.write(psw, interval=0.25)
            pyautogui.press('enter')
        if pyautogui.locateOnScreen('images/button/ok.png') != None:
            pyautogui.click('images/button/ok.png')

def get_nplayermax(max):
    nplayer = 0
    im = Image.open('images/screenshot.png')
    pix = im.load()
    if (max == 8):
        pos = [[191,127],[453,127],[720,127],[812,330],[715,534],[453,534],[195,534],[94,331]]
    if (max == 6):
        pos = [[134,177],[452,127],[768,177],[767,484],[453,534],[134,484]]
    for i in range (0,max):
        r,g,b=pix[pos[i][0],pos[i][1]]
        if (r+10>b and r-10<b and b+10>g and b-10<g and r > 150):
            nplayer += 1
        #else:
        #    print('player not found : '+str(i),r)
    return(nplayer)

def get_max():
    #print((get_nplayermax(8)/8),(get_nplayermax(6)/6))
    if get_nplayermax(8)/8 > get_nplayermax(6)/6:
        return (8)
    else:
        return (6)

def get_stack():
    if pyautogui.locateOnScreen('images/button/allin.png') != None:
        pyautogui.click('images/button/allin.png')
    pic = pyautogui.screenshot(region=(534, 619, 120, 18))
    pic.save('images/stack.png')
    return get_number('images/stack.png', 0.5)

def get_nplayer(max):
    nplayer = 0
    im = Image.open('images/screenshot.png')
    pix = im.load()
    if (max == 8):
        #pos = [[197,128],[453,127],[720,127],[807,331],[715,534],[453,534],[195,534],[94,331]]
        pos = [[191,127],[720,127],[812,330],[715,534],[453,534],[195,534],[94,331]]
    if (max == 6):
        #pos = [[134,177],[452,127],[768,177],[767,484],[453,534],[134,484]]
        pos = [[134,177],[768,177],[767,484],[453,534],[134,484]]
    for i in range (0,max - 1):
        r,g,b=pix[pos[i][0],pos[i][1]-50]
        if (r+5>b and r-10<b and b+10>g and b-10<g and r > 200):
            nplayer += 1
        #else:
        #    print('player not found : '+str(i),r,g,b)
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

def get_number(file_name, en):
    string = read_data(file_name, en)
    index_list = []
    del index_list[:]
    for i, x in enumerate(string):
        if x.isdigit() == True:
            index_list.append(i)
    if not index_list and en < 5:
        return get_number(file_name, en + 0.5)
    if not index_list:
        return 0
    start = index_list[0]
    end = index_list[-1] + 1
    number = string[start:end]
    return number

def get_symbol(file_name):
    im = Image.open(file_name)
    pix = im.load()
    r,g,b=pix[10,34]
    if (r >= 225):
        return('d')
    if (r >= 160):
        return('h')
    if (r >= 64):
        return('c')
    if (r <= 4):
        return('s')
    #if file_name == 'images/card1.png' or file_name == 'images/card2.png':
        #shutil.copy(file_name, 'images/errors/s'+file_name[7:12]+'.png')
        #print('read error')
    return('N')

def read_data(file_name, en):
    if secure == 0:
        img = Image.open(file_name).convert('LA')
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(en)
        img = img.filter(ImageFilter.GaussianBlur(radius = 0.34))
        img.save('images/greyscale.png')
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        #TESSDATA_PREFIX:'C:/Program Files/Tesseract-OCR/tessdata'
        customconf = r'-c tessedit_char_whitelist=B.01234567859 --oem 3 --psm 6'
        return (pytesseract.image_to_string('images/greyscale.png', config=customconf))
    return 'error'

def read_card(file_name, en):
    if secure == 0:
        img = Image.open(file_name).convert('LA')
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(en)
        img = img.filter(ImageFilter.GaussianBlur(radius = 0.5))
        img.save('images/greyscalecard.png')
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        #TESSDATA_PREFIX:'C:/Program Files/Tesseract-OCR/tessdata'
        customconf = r'-c tessedit_char_whitelist=AKQJ0123456789 --oem 3 --psm 6'
        string = pytesseract.image_to_string('images/greyscalecard.png', config=customconf)
        if not string and en < 4:
            return (read_card(file_name, en + 1))
        if not string:
            #error read for 8
            #shutil.copy(file_name, 'images/errors/v'+file_name[7:12]+'.png')
            #print('read error')
            return '8'
        if (len(string) >= 2 and string[0] == '1' and string[1] == '0'):
            return ('T')
        return (string[0])
    return 'error'

def action(bet, act):
    #allin = 0, check = 1, call = 2, fold = 3, bet = 4 
    if pyautogui.locateOnScreen('images/button/allin.png') != None and act == 0:
        pyautogui.click('images/button/allin.png')
        pyautogui.press('enter')
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
    if pyautogui.locateOnScreen('images/button/raise.png') != None and (act == 0 or act == 4):
        pyautogui.click('images/button/raise.png')

def init_card(file_name):
    card = Card(file_name)
    if get_symbol(file_name) != 'N':
        card.v = read_card(file_name, 0.5)
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
    d.pot = get_number('images/pot.png', 0.5)
    d.tpot = get_number('images/totalpot.png', 3)
    d.tocall = get_number('images/tocall.png', 0.5)
    d.stack = get_number('images/stack.png', 0.5)

def print_data(d):
    print('--------------------')
    print('hand  |     board')
    print(d.card1.v+d.card1.s, d.card2.v+d.card2.s,'|', \
        d.board1.v+d.board1.s, d.board2.v+d.board2.s, \
        d.board3.v+d.board3.s, d.board4.v+d.board4.s, \
        d.board5.v+d.board5.s)
    print('max      :',d.max)
    print('nplayer  :',d.nplayer)
    print('pot      :',d.pot)
    print('tpot     :',d.tpot)
    print('to call  :',d.tocall)
    print('stack    :',d.stack)

class Card():
    v = ''
    s = ''
    def __init__(self, file_name):
        if get_symbol(file_name) != 'N':
            self.v = read_card(file_name, 3)
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
    pot = get_number('images/pot.png', 0.5)
    tpot = get_number('images/totalpot.png', 0.5)
    tocall = get_number('images/tocall.png', 0.5)
    stack = get_number('images/stack.png', 0.5)
    auto_register = 0

if __name__ == "__main__":
    secure = 0
    sys.tracebacklimit = 0
    q = 0
    psw = input('enter your password : ')
    while q == 0:
        try:
            actions = ['allin','check','call','fold','bet']
            if len(sys.argv) > 1 and sys.argv[1] == '-dc':
                dc = 1
            else:
                dc = 0
            pic = pyautogui.screenshot()
            pic.save('images/screenshot.png')
            max = get_max()
            d = Data(max)
            while q == 0:
                if msvcrt.kbhit():
                    print('key pressed, exiting...')
                    q = 1
                    sys.exit()
                log_in(psw)
                sit_back()
                max = get_max()
                new_table(max)
                set_position(max)
                screenshot(max) 
                im = Image.open('images/screenshot.png')
                pix = im.load()
                r,g,b=pix[513,643]
                if g < 20:
                    start_time = time.time()
                    init_data(d, max)
                    print_data(d)
                    secure = 1
                    secure, bet, act = algo(d)
                    print('bet      :',bet)
                    print('action   :',actions[act])
                    print('time     :',round(time.time() - start_time,1),'s')
                    action(bet , act)
                if dc == 1:
                    q, d.auto_register = discord(d)
                r,g,b=pix[453,254]
                #print (r)
                if r >= 188 and r < 192:
                    print(r)
                    pic = pyautogui.screenshot(region=(164, 161, 579, 422))
                    pic.save('images/result.png')
                    if dc == 1:
                        dc_result()
                    pyautogui.click(528, 501)
        except:
            continue





'''
afer : 
call bug
get_pos
get 2 cursor
fix errors
'''
