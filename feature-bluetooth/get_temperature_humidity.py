# Reference: https://raspberrypi.stackexchange.com/questions/61524/how-to-approximate-room-temperature-in-a-better-way
from sense_hat import SenseHat
import os
import time

class senseHatDataRetriever:
    # Get Temperature & Humidity
    sense = SenseHat()

    # Get CPU temperature.
    @classmethod
    def get_cpu_temp(cls):
        res = os.popen("vcgencmd measure_temp").readline()
        return float(res.replace("temp=","").replace("'C\n",""))

    # Calculate real temp compensating CPU temperature    
    @classmethod
    def get_true_temp(cls):
        t1 = cls.sense.get_temperature_from_humidity()
        t2 = cls.sense.get_temperature_from_pressure()
        t_cpu = senseHatDataRetriever.get_cpu_temp()
        # Calculates the real temperature compesating CPU heating.
        t = (t1 + t2) / 2
        t_corr = t - ((t_cpu - t) / 1.5)        
        return t_corr

    # The above real temperature algorithm creates 
    # too much of error margin.
    # Thus for this version, regular temp is used
    @classmethod
    def get_regular_temp(cls):
        return cls.sense.get_temperature()

    # Get humidity
    @classmethod
    def get_current_humidity(cls):        
        return cls.sense.get_humidity()

# use moving average to smooth readings
def get_smooth(x):
  if not hasattr(get_smooth, "t"):
    get_smooth.t = [x,x,x]
  get_smooth.t[2] = get_smooth.t[1]
  get_smooth.t[1] = get_smooth.t[0]
  get_smooth.t[0] = x
  xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
  return(xs)

        
