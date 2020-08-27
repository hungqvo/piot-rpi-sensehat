from sense_hat import SenseHat
import os
import time
 
class Calibration:

    sense = SenseHat()
# Get CPU temperature.
    def get_cpu_temp(self):
        res = os.popen("vcgencmd measure_temp").readline()
        return float(res.replace("temp=","").replace("'C\n",""))

    def get_accurate_temp(self):
        t1 = self.sense.get_temperature_from_humidity()
        t2 = self.sense.get_temperature_from_pressure()
        t_cpu = self.get_cpu_temp()
        h = self.sense.get_humidity()
        p = self.sense.get_pressure()
        t = (t1 + t2) / 2
        t_corr = t - ((t_cpu - t) / 1.5)
        return t_corr

    def getHumidity(self):
        return self.sense.get_humidity()
