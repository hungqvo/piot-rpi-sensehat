from sense_hat import SenseHat
import json
import time
from senseHatCalibration import Calibration
class Display:
    s = SenseHat()
  
    cali = Calibration()
# color in RGB format
    green = (0, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
#get accurate temperature
    temperature = cali.get_accurate_temp()
    OFFSET_LEFT = 1
    OFFSET_TOP = 2

    NUMS =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
           0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
           1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
           1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
           1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
           1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
           1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
           1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
           1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
           1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9

# Displays a single digit (0-9)
    def show_digit(self,val, xd, yd, r, g, b):
        offset = val * 15
        for p in range(offset, offset + 15):
            xt = p % 3
            yt = (p-offset) // 3
            self.s.set_pixel(xt+xd, yt+yd, r*self.NUMS[p], g*self.NUMS[p], b*self.NUMS[p])

# Displays a two-digits positive number (0-99)
    def show_number(self,val, r, g, b):
        abs_val = abs(val)
        tens = abs_val // 10
        units = abs_val % 10
        if (abs_val > 9): 
            self.show_digit(tens, self.OFFSET_LEFT, self.OFFSET_TOP, r, g, b)
            self.show_digit(units, self.OFFSET_LEFT+4, self.OFFSET_TOP, r, g, b)
    # temperature < comfortable min => blue
    #             in            range => green
    #             >             max => red
    def startDisplay(self):
        with open('config.json') as configFile:
            data = json.load(configFile)
        if int(self.temperature ) < data['cold_max']:
            self.show_number(int(self.temperature),0,0,255)
        elif int(self.temperature)>= data['cold_max'] and int(self.temperature)<= data['hot_min']:
            self.show_number(int(self.temperature),0,255,0)
        else:
            self.show_number(int(self.temperature),255,0,0)
display = Display()
display.startDisplay()
