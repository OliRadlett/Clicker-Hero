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

while (True):
    cmd = input()
    if (cmd[0:4] == "loop"):
        MainLoop(int(cmd[5:]))
    elif (cmd[0:7] == "analyse"):
        if (cmd[8:] == "money"):
            Screenshot_Money()
            OCR("money")
        else:
            print("Value not recognised")
    else:
        print ("Command not recognised")