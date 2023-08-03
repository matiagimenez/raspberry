# sudo pip3 install adafruit-circuitpython-ssd1306

from board import SCL, SDA
import busio
import time
import adafruit_ssd1306 as adafruit
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(SCL, SDA)
time.sleep(1)
# sets the height & width of the screen
display = adafruit.SSD1306_I2C(128, 64, i2c)

def printData(data):
    # clears the screen
    display.fill(0)
    display.show()

    # defines the text to paint
    image = Image.new('1', (128, 64))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((0, 0), str(data["time"]), font=font, fill=255)
    draw.text((2, 16), "T: " + str(data["temperature"]), font=font, fill=255)
    draw.text((2, 32), "H: " + str(data["humidity"]), font=font, fill=255)
    draw.text((2, 48), "P: " + str(data["pressure"]), font=font, fill=255)
    
    # paints the screen
    display.image(image)
    display.show()

