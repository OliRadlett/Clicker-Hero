import pytesseract
import mss
import mss.tools
import time
import cv2
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def Screenshot(top, left, width, height, name):

    with mss.mss() as sct:
    
        monitor = {'top': top, 'left': left, 'width': width, 'height': height}
        output = 'screenshots/screenshot_' + name + '.png'.format(**monitor)
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output = output)
        print ("Screenshot saved to: " + output)

def Screenshot_Money():
    
    top = 255
    left = 295
    width = 606
    height = 71
    name = "money"
    Screenshot(top, left, width, height, name)

def OCR(filename):

    img = Image.open("screenshots/screenshot_" + filename + ".png")
    img = img.convert('L')
    img.save('screenshots/screenshot_' + filename + '.png')
    text = pytesseract.image_to_string(Image.open("screenshots/screenshot_" + filename + ".png"))
    print (filename + ": " + text)

def MainLoop(duration):

    while (True):

        print ("New cycle")
        time.sleep(duration)

        #Screenshot_Money()
        #OCR("money")

menu = True
print ("Welcome to Clicker-Hero")
print ("Options: ")
print ("[loop]['duration'] - Runs loop with specified duration (seconds)")
print ("[analyse]['value'] - Analyse a specific value e.g. money")
while (menu):
    cmd = input("->")
    if (cmd[0:4] == "loop"):
        menu = False
        MainLoop(int(cmd[5:]))
    elif (cmd[0:7] == "analyse"):
        menu = False
        print ("Taking screenshot in: 5")
        time.sleep(1)
        print ("Taking screenshot in: 4")
        time.sleep(1)
        print ("Taking screenshot in: 3")
        time.sleep(1)
        print ("Taking screenshot in: 2")
        time.sleep(1)
        print ("Taking screenshot in: 1")
        time.sleep(1)
        if (cmd[8:] == "money"):
            Screenshot_Money()
            OCR("money")
        else:
            print("Value not recognised")
    else:
        print ("Command not recognised")