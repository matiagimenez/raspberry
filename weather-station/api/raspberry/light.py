# sudo pip3 install adafruit-circuitpython-tsl2591

import board
import busio
import adafruit_tsl2591
import time

# Initialize the I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)
time.sleep(1)
# Initialize the sensor.
sensor = adafruit_tsl2591.TSL2591(i2c)
 
# You can optionally change the gain and integration time:
# sensor.gain = adafruit_tsl2591.GAIN_LOW (1x gain)
# sensor.gain = adafruit_tsl2591.GAIN_MED (25x gain, the default)
# sensor.gain = adafruit_tsl2591.GAIN_HIGH (428x gain)
# sensor.gain = adafruit_tsl2591.GAIN_MAX (9876x gain)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS (100ms, default)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_200MS (200ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_300MS (300ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_400MS (400ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_500MS (500ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_600MS (600ms)
 
# Read the total lux, IR, and visible light levels and print it every second.
def getLightLevels():
    # Read and calculate the light level in lux.
    lux = sensor.lux
    lux_value = "{0}".format(lux)
    # You can also read the raw infrared and visible light levels.
    # These are unsigned, the higher the number the more light of that type.
    # There are no units like lux.
    # Infrared levels range from 0-65535 (16-bit)
    infrared = sensor.infrared
    infrared_value = "{0}".format(infrared)
    # Visible-only levels range from 0-2147483647 (32-bit)
    visible = sensor.visible
    visible_value = "{0}".format(visible)
    # Full spectrum (visible + IR) also range from 0-2147483647 (32-bit)
    full_spectrum = sensor.full_spectrum
    full_spectrum_value = "{0}".format(full_spectrum)
    return {
        "total_light": lux_value,
        "infrared_light": infrared_value,
        "visible_light": visible_value,
        "full_spectrum": full_spectrum_value
    }
