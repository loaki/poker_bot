#pip install pyautogui
import pyautogui
pyautogui.FAILSAFE = True
# Take screenshot
pic = pyautogui.screenshot()
# Save the image
pic.save('screenshot.png')
#pyautogui.alert('This displays some text with an OK button.')
card = 'images/cards/8h.png'
#if pyautogui.locateOnScreen(card) != None:
#    pyautogui.click(card)


#----read data----
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

img = Image.open('images/test6.png').convert('LA')
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2)
img.save('images/test/greyscale2.png')

print(pytesseract.image_to_string('images/test/greyscale2.png'))


#----nb players----
#nb = 0
#for pos in pyautogui.locateAllOnScreen('images/nplayer.png'):
#	nb += 1
#print(nb)


#----actions----
#bet = '5'
#action = 1
#if pyautogui.locateOnScreen('images/check.png') != None and action == 0:
#    pyautogui.click('images/check.png')
#if pyautogui.locateOnScreen('images/fold.png') != None and action == 1:
#    pyautogui.click('images/fold.png')
#if pyautogui.locateOnScreen('images/bet.png') != None and action == 2:
#    pyautogui.click('images/bet.png')
#    pyautogui.write(bet, interval=0.25)
#    pyautogui.press('enter')
