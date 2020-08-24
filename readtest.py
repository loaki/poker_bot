import pyautogui
import pytesseract
import os
import sys
import shutil
import random

from PIL import Image, ImageEnhance, ImageFilter

def get_symbol(file_name):
    im = Image.open(file_name)
    pix = im.load()
    r,g,b=pix[11,33]
    if (r >= 225):
        return('d')
    if (r >= 160):
        return('h')
    if (r >= 64):
        return('c')
    if (r == 0):
        return('s')
    if file_name == 'images/card1.png' or file_name == 'images/card2.png':
        shutil.copy(file_name, 'images/errors/s'+file_name[7:12]+'.png')
        print('read error')
    return(r)

def pixelProcRed(intensity):

    return intensity

def pixelProcBlue(intensity):

    return intensity

def pixelProcGreen(intensity):

    return intensity

def read_card(file_name, en, th, gb):
    
    img = Image.open(file_name).convert('L')
    img = img.point(lambda p: p > th and 255)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(float(en))
    #img = sharp.enhance(1)
    img = img.filter(ImageFilter.GaussianBlur(radius = gb))

    img.save('images/errors/greyscalecard.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    customconf = r'-c tessedit_char_whitelist="AKQJ0123456789" --psm 10'
    string = pytesseract.image_to_string('images/errors/greyscalecard.png', config=customconf)
    print(en, th, gb,' = ',string)
    return (string)

    '''
    if not string and float(en) < 6:
        print('read error')
        return read_card(file_name, float(en) + 0.1)
    print(en, string)
    return read_card(file_name, float(en) + 0.1)
    return string
    if (len(string) >= 2 and string[0] == '1' and string[1] == '0'):
        return ('T')
    return (string[0])
    '''
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv[1])
        file = sys.argv[1]
    else :
        print('no file specified')

    print(read_card(file, int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[3])))
    '''
    en = random.randint(0, 200)
    en -= 100
    th = random.randint(30, 160)
    gb = random.randint(0, 20)
    gb /= 10
    while (read_card(file, en, th, gb) != sys.argv[2]):
        en = random.randint(0, 200)
        en -= 100
        th = random.randint(80, 160)
        gb = random.randint(0, 20)
        gb /= 10

    print(read_card(file, sys.argv[2]))'
   '''