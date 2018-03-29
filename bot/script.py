import pytesseract
import mss
import mss.tools
import time
import cv2
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def Screenshot():

    with mss.mss() as sct:
        # The screen part to capture
        monitor = {'top': 255, 'left': 295, 'width': 606, 'height': 71}
        output = 'screenshots/screenshot_money.png'.format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print("Screenshot saved to: " + output)

def Analyse():

    img = Image.open("screenshots/screenshot_money.png")
    img = img.convert('L')
    img.save('screenshots/screenshot_money.png')
    text = pytesseract.image_to_string(Image.open("screenshots/screenshot_money.png"))
    print ("Money: " + text)

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
Screenshot()
Analyse()
