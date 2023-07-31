from flask import Flask, jsonify   
import threading
import time
from datetime import datetime

# from src.IWeather import IWeather
# from src.RaspberryStation import RaspberryStation
from raspberry.humidity import getHumidity
from raspberry.light import getLightLevels
from raspberry.temperature_pressure import getTemperature, getPressure

app = Flask(__name__)

# weatherStation: IWeather = RaspberryWeather()
# data = {'light': weatherStation.getLightLevels(), 'pressure': weatherStation.getPressure(), 'humidity': weatherStation.getHumidity(), 'temperature': weatherStation.getTemperature(), 'time': datetime.now().isoformat()}

data = {'light': getLightLevels(), 'pressure': getPressure(), 'humidity': getHumidity(), 'temperature': getTemperature(), 'time': datetime.now().isoformat()}

# Function with sensor logic
def collect_data_loop():
    global data
    # global weatherStation
    # pressure, temperature, humidity, light = weatherStation.read_data()
    
    while True:
        # data["temperature"] = weatherStation.getTemperature()
        # data["humidity"] = weatherStation.getHumidity()
        # data["pressure"] = weatherStation.getPressure()
        # data["light"] = weatherStation.getLightLevels()
        data["temperature"] = getTemperature()
        data["humidity"] = getHumidity()
        data["pressure"] = getPressure()
        data["light"] = getLightLevels()
        data["time"] = datetime.now().isoformat()
        time.sleep(5)
        
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