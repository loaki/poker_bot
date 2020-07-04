#pip install pyautogui
import pyautogui
pyautogui.FAILSAFE = True
# Take screenshot
pic = pyautogui.screenshot()
# Save the image
pic.save('screenshot.png')
#pyautogui.alert('This displays some text with an OK button.')
card = 'images/cards/6a.png'
if pyautogui.locateOnScreen(card):
    pyautogui.click(card)

bet = '5'
action = 3
if pyautogui.locateOnScreen('images/check.png') != None and action == 0:
    pyautogui.click('images/check.png')
if pyautogui.locateOnScreen('images/fold.png') != None and action == 1:
    pyautogui.click('images/fold.png')
if pyautogui.locateOnScreen('images/bet.png') != None and action == 2:
    pyautogui.click('images/bet.png')
    pyautogui.write(bet, interval=0.25)
    pyautogui.press('enter')

#pyautogui.click(50,50)