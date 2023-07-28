from flask import Flask, jsonify   
import threading
import time
from datetime import datetime

app = Flask(__name__)

# Example data (temporary)
sensor_data = {'time': datetime.now().isoformat() ,'temperature': 25.5, 'humidity': 60.0}

# Function with sensor logic
def collect_data_loop():
    # Acces to example data variable (temporary)
    global sensor_data
    
    while True:
        # TODO - This updates on values are temporary for tests
        sensor_data["temperature"] += 1
        sensor_data["humidity"] += 1
        sensor_data["time"] = datetime.now().isoformat()
        time.sleep(2)
        
# Thread for executing data recolection loop
data_thread = threading.Thread(target=collect_data_loop)
data_thread.daemon = True  # The threads stop with the main app
data_thread.start()

@app.route('/data')
def get_sensor_data():
    global sensor_data
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)