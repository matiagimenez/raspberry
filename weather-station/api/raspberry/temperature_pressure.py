# sudo pip3 install adafruit-circuitpython-bmp3xx

import board
import adafruit_bmp3xx
import time

# I2C setup
i2c = board.I2C()
time.sleep(1)
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
bmp.pressure_oversampling = 8
bmp.temperature_oversampling = 2

def getPressure():
    pressure = bmp.pressure
    if(pressure is not None):
        return "{:6.2f}".format(pressure) + " hPa"
    else:
        return False

def getTemperature():
    temperature = bmp.temperature
    if(temperature is not None):
        return "{:5.2f}".format(temperature) + " °C"
    else:
        return False
