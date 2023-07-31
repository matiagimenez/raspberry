# sudo pip3 install adafruit-circuitpython-bmp3xx
# sudo pip3 install adafruit-circuitpython-tsl2591
# sudo pip3 install Adafruit_DHT

import board
import busio
import Adafruit_DHT as dht
import adafruit_bmp3xx as bmp3xx
import adafruit_tsl2591

class RaspberryStation(IWeather):
    def __init__(self):
        i2c = board.I2C()
        self.bmp = bmp3xx.BMP3XX_I2C(i2c)
        self.bmp.pressure_oversampling = 8
        self.bmp.temperature_oversampling = 2
        i2c = busio.I2C(board.SCL, board.SDA)
        self.tsl = adafruit_tsl2591.TSL2591(i2c)
        
        
    def getHumidity(self):
        sensor_GPIO_pin = 4
        humidity, temperature = dht.read_retry(dht.AM2302, sensor_GPIO_pin)
        if (humidity is not None):
            return "{:%}".format(humidity/100)
        else:
            return False
        
    def getTemperature(self):
        temperature = self.bmp.temperature
        if(temperature is not None):
            return "{:5.2f}".format(temperature)
        else:
            return False
        
    def getPressure(self):
        pressure = self.bmp.pressure
        if(pressure is not None):
            return "{:6.2f}".format(pressure)
        else:
            return False
        
    def getLightLevels(self):
        lux = self.tsl.lux
        lux_value = "{0}".format(lux)
        # Infrared levels range from 0-65535 (16-bit)
        infrared = self.tsl.infrared
        infrared_value = "{0}".format(infrared)
        # Visible-only levels range from 0-2147483647 (32-bit)
        visible = self.tsl.visible
        visible_value = "{0}".format(visible)
        # Full spectrum (visible + IR) also range from 0-2147483647 (32-bit)
        full_spectrum = self.tsl.full_spectrum
        full_spectrum_value = "{0}".format(full_spectrum)
        
        return {
            "total_light": lux_value,
            "infrared_light": infrared_value,
            "visible_light": visible_value,
            "full_espectrum": full_spectrum_value
        }
    