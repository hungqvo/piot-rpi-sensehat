import bluetooth
import time
import subprocess
from sense_hat import SenseHat

# Create a class
class bluetoothClient:
    # Color initialization
    w = [255, 255, 255]     # White
    r = [255, 0, 0]         # Red
    b = [0, 0, 255]         # Blue

    # Bluetooth icon pixel matrix
    bluetooth_icon = [
    b,b,b,w,b,b,b,b,
    b,w,b,w,w,b,b,b,
    b,b,w,w,b,w,b,b,
    b,b,b,w,w,b,b,b,
    b,b,b,w,w,b,b,b,
    b,b,w,w,b,w,b,b,
    b,w,b,w,w,b,b,b,
    b,b,b,w,b,b,b,b,
    ]

    # Tick icon pixel matrix
    tick_icon = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,w,
        b,b,b,b,b,b,w,b,
        b,b,b,b,b,w,b,b,
        w,b,b,b,w,b,b,b,
        b,w,b,w,b,b,b,b,
        b,b,w,b,b,b,b,b,
    ]

    sense = SenseHat()
    
    @classmethod
    def send_message_to(cls,targetBluetoothMacAddress, msg):
        # Setup RFCOMM Bluetooth connection
        port = 1
        client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        client_socket.connect((targetBluetoothMacAddress, port))
        
        # Send message through the bluetooth socket
        client_socket.send(msg)

        # Close the socket
        client_socket.close()

        # Display sent success status
        cls.sense.set_pixels(cls.tick_icon)
        time.sleep(3)
        cls.sense.clear()

    @classmethod
    def find_devices(cls,msg):        
        # Turn on Bluetooth
        subprocess.run("sudo rfkill unblock bluetooth", shell = True)
        time.sleep(1)

        # Start scaning and sending message
        while True:
            # Display Bluetooth icon
            cls.sense.clear()
            cls.sense.set_pixels(cls.bluetooth_icon)

            # Discover devices
            nearbyDevices = bluetooth.discover_devices()

            if len(nearbyDevices) > 0:
                # Found all nearby devices
                for macAddress in nearbyDevices:                    
                    try:
                        bluetoothClient.send_message_to(macAddress, msg)
                    except Exception:
                        # Keep sending to other bluetooth devices
                        continue      
                
                break # Quit searching for devices to send
            