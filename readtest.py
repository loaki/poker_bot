import pyautogui
import pytesseract
import os
import sys
import shutil

from PIL import Image, ImageEnhance, ImageFilter


def read_card(file_name):
    img = Image.open(file_name).convert('LA')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
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
    print(read_card(file))