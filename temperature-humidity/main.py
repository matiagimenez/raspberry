# git clone https://github.com/adafruit/DHT-sensor-library.git
# cd Adafruit_Python_DHT
# sudo apt install build-essential python-dev
# sudo python3 setup.py install

import Adafruit_DHT as Adafruit
from time import sleep
from datetime import datetime

sensor = 4

while True:
    
    try:
        humidity, temperature = Adafruit.read_retry(Adafruit.AM2302, sensor)
        file = open('temperature-humidity.txt', 'a')
        if (humidity is not None and temperature is not None):
            data = '[' + str(datetime.now()) + '] Temperature: ' + str("%.2f"%temperature) + ' - Humidity: ' + str(int(humidity)) + '%'
            print(data)
            file.write(data + '\n')
            sleep(1)
        else:
            print('Failed to get reading')
            sleep(1)
    except:
        print('Something went wrong writing the file')
    finally:
        file.close()