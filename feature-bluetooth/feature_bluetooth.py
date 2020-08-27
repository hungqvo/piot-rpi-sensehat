import bluetooth
import time
import json
import os
from read_json import jsonHandler
from get_temperature_humidity import senseHatDataRetriever
from bluetooth_client import bluetoothClient

# Call the delegated functions from import

# Wait for system to boot up
time.sleep(20)

# Get rounded values of temperature and humidity from SenseHAT
current_temp = round(senseHatDataRetriever.get_regular_temp())    
current_humidity = round(senseHatDataRetriever.get_current_humidity())

# Check temperature and humidity whether they're in range
msg = jsonHandler.check_range(current_temp,current_humidity)

# Scan nearby devices and send a message through bluetooth
bluetoothClient.find_devices(msg)
