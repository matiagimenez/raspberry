# git clone https://github.com/adafruit/DHT-sensor-library.git
# cd Adafruit_Python_DHT
# sudo apt install build-essential python-dev
# sudo python3 setup.py install

import Adafruit_DHT as Adafruit
sensor_GPIO_pin = 4

def getHumidity():
    humidity, temperature = Adafruit.read_retry(Adafruit.AM2302, sensor_GPIO_pin)
    if (humidity is not None):
        return "{:%}".format(humidity/100)
    else:
        return False