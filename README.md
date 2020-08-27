# SenseHAT PIOT Project
###### Project Repository URL:
https://github.com/Lycheeeeeee/piot/tree/master 
----
## TASK A + B:
crontab -e
save to the database and push notification every minute
* * * * * python3 /home/pi/piot/monitorAndDisplay.py
read temperature and display every minute
* * * * * python3 /home/pi/piot/readAndDisplay.py
run the apiRESTful server whenever the pi is booted
@reboot python3 /home/pi/piot/apiRESTful.py

1. command request to test the API
GET the newest records:
  curl --location --request GET 'localhost:5000/get' \
  --header 'Content-Type: application/json' \
  --data-raw '
  '
2. POST upload the new record:
  curl --location --request POST 'localhost:5000/upload' \
  --header 'Content-Type: application/json' \
  --data-raw '{	
  "temperature":20,
	"comfortable":false,
	"date":"07/10/2020",
	"humidity":45
  }'
  
3. PUT update the newest record:
  curl --location --request PUT 'localhost:5000/update' \
  --header 'Content-Type: application/json' \
  --data-raw '{	
	"temperature":22,
	"comfortable":true,
	"humidity":55
  }
  '
----
## FEATURE-BLUETOOTH (TASK C):
###### Setup: 
1. Run script at startup by using crontab by typing the following command (in terminal): 'EDITOR=nano crontab -e'
2. On the client side, append the script to crontab including the path to feature_bluetooth.py: '@reboot python3 path_to_file/feature_bluetooth.py >> path_to_output/cron_log.txt 2>1&'
3. On the server side, run bluetooth_server.py using crontab by typing the command:'@reboot python3 path_to_file/feature_bluetooth.py >> path_to_output/cron_log.txt 2>1&'

###### Function:
1. The scripts run at startup, and the client_side script will find the nearby devices, then send to the devices which are running the server_side script.
2. Once connected, the client_side sends the message containing the temperature and humidity to the server_side.
3. The real temperature algorithm (temperature compensating CPU temp) provided in the lecture produces high margin of error (sometimes it shows -4 degrees), thus this program will use regular temperature obtained directly from senseHat sensor. 
4. The program is scalable to implement immediately new temperature algorithm in the near future versions.
----
## FEATURE-GAME (TASK D):
###### Setup: 
1. Run the game.py script on the Pi

###### Function:
1. The game shows instructions to the players.
2. The players take turn, and toggle SenseHat joystick (Left for Player 1, Right for Player 2) to shake the dice.
3. First player to get 30 wins the game.
4. The program write into .csv file the winner score and time stamp of the game.
----
## REFERENCES: 
1. PEP8 naming conventions
https://softwareengineering.stackexchange.com/questions/308972/python-file-naming-convention

2. SenseHAT LED matrix
https://pythonhosted.org/sense-hat/api/#led-matrix

3. Python @staticmethod and @classmethod
https://stackoverflow.com/questions/1859959/static-methods-how-to-call-a-method-from-another-method

4. Class method and static method
https://realpython.com/instance-class-and-static-methods-demystified/

5. Python and Bluetooth
http://pages.iu.edu/~rwisman/c490/html/pythonandbluetooth.htm

6. Python time.sleep()
https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/

7. Python joy stick
https://pythonhosted.org/sense-hat/api/#joystick

8. Unix Bluetooth Turn On and Off
https://askubuntu.com/questions/450698/how-to-turn-on-and-off-bluetooth-visibility-mode

9. Unix Bluetooth Discoverable Mode
https://askubuntu.com/questions/450698/how-to-turn-on-and-off-bluetooth-visibility-mode

10. Unix subprocess.call (running Unix cmd commans using Python)
https://queirozf.com/entries/python-3-subprocess-examples

11. Handling errors and exception
https://docs.python.org/3/tutorial/errors.html

12. Getting correct file path
https://stackoverflow.com/questions/22282760/filenotfounderror-errno-2-no-such-file-or-directory

13. Getting Time stamp
https://www.programiz.com/python-programming/datetime/current-datetime

14. Scheduling tasks with Cron
https://www.raspberrypi.org/documentation/linux/usage/cron.md

15. Writing README.md
https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax