import pyautogui
import pytesseract
import os
import sys
import shutil

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

def read_card(file_name, en):
    img = Image.open(file_name).convert('L')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(float(en))
    img = img.filter(ImageFilter.GaussianBlur(radius = 0.6))
    img.save('images/errors/greyscalecard.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    customconf = r'-c tessedit_char_whitelist=B.0123456789 --oem 3 --psm 6'
    string = pytesseract.image_to_string('images/errors/greyscalecard.png', config=customconf)
    return (string)
    if not string:
        print('read error')
        return ''
    if (len(string) >= 2 and string[0] == '1' and string[1] == '0'):
        return ('T')
    return (string[0])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv[1])
        file = sys.argv[1]
    else :
        print('no file specified')
    #print(get_symbol(file))
    print(read_card(file, sys.argv[2]))