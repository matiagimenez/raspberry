# sudo pip3 install adafruit-circuitpython-bmp3xx

import time
import board
import adafruit_bmp3xx

# I2C setup
i2c = board.I2C()
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

bmp.pressure_oversampling = 8
bmp.temperature_oversampling = 2

while True:
    print(
        "Pressure: {:6.2f}  Temperature: {:5.2f}".format(bmp.pressure, bmp.temperature)
    )
    time.sleep(1)