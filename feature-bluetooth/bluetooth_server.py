import bluetooth
import subprocess
import time
from sense_hat import SenseHat

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

def receive_messages():
	# Wait for system to boot
	time.sleep(20) 

	# Turn on Bluetooth
	subprocess.run("sudo rfkill unblock bluetooth", shell = True)
	time.sleep(1)

	# Display Bluetooth icon on SenseHat
	sense = SenseHat()
	sense.set_pixels(bluetooth_icon)

	# Turn on Discoverable mode
	subprocess.run("sudo hciconfig hci0 piscan", shell = True)
	
	# Setup RFCOMM Bluetooth connection	
	server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	port = 1

	# Bind the server socket and starts listening 
	server_socket.bind(("",port))
	server_socket.listen(1)

	# Accept incoming connection
	client_socket, address = server_socket.accept()

	# Receive the message from bluetooth client socket
	data = str(client_socket.recv(1024).decode())

	# Format the message
	message_list = data.split("|")
	temp_message = message_list[0]
	humidity_message = message_list[1]

	# Display message on SenseHAT
	sense.clear()
	sense.show_message(temp_message, scroll_speed=0.08, text_colour=r)
	
	time.sleep(1)
	sense.show_message(humidity_message, scroll_speed=0.08, text_colour=b)
	sense.clear()
	
	# Close the bluetooth sockets
	client_socket.close()
	server_socket.close()

# Execute the program
receive_messages()
