from flask import Flask, jsonify   
import threading
import time
from datetime import datetime

from raspberry.humidity import getHumidity
from raspberry.light import getLightLevels
from raspberry.temperature_pressure import getTemperature, getPressure
from raspberry.screen import printData

app = Flask(__name__)

time.sleep(5)
data = {'light': getLightLevels(), 'pressure': getPressure(), 'humidity': getHumidity(), 'temperature': getTemperature(), 'time': datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

# Function with sensor logic
def collect_data_loop():
    global data
    
    while True:
        data["temperature"] = getTemperature()
        data["humidity"] = getHumidity()
        data["pressure"] = getPressure()
        data["light"] = getLightLevels()
        data["time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        printData(data)
        time.sleep(10)
        
# Thread for executing data recolection loop
data_thread = threading.Thread(target=collect_data_loop)
data_thread.daemon = True  # The threads stop with the main app
data_thread.start()

@app.route('/weather')
def get_sensor_data():
    global data
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#http://0.0.0.0:5000/weather
