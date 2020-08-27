import json
import os
from sense_hat import SenseHat

class jsonHandler:
    # Symbolic initialization
    min_temp = 0
    max_temp = 0
    min_humidity = 0
    max_humidity = 0
    
    # Check temp and humidity with configured range
    @classmethod
    def check_range(cls, temp, humidity):
        try:
            # Get relative file path
            current_directory = (__file__).split("read_json.py")[0]
            file_name = current_directory + "config_min_max.json"
            
            # Load the json file into python
            with open(file_name) as data_file:
                data = data_file.read()
                config_range = json.loads(data)    
            
            # Setting the variables
            cls.min_temp = config_range["min_temperature"]
            cls.max_temp = config_range["max_temperature"]
            cls.min_humidity = config_range["min_humidity"]
            cls.max_humidity = config_range["max_humidity"]

            # Check if the values are in range
            temp_position = jsonHandler.check_temp(temp)
            temp_message = "Temperature is {} at {} degrees".\
                format(temp_position, temp)
            humidity_position = jsonHandler.check_humidity(humidity)
            humidity_message = "|Humidity is {} at {} percent".\
                format(humidity_position, humidity)

            # Return the message
            result = temp_message + " " + humidity_message
            return(result)

        except Exception as exception_message:
            print("Cannot load json due to exception {}".format(exception_message))

    # Separate function to check temperature
    @classmethod
    def check_temp(cls,temp):
        max = cls.max_temp
        min = cls.min_temp
        
        # Range checking algorithm
        if temp > max:
            above_max_value = temp - max
            return("{} degrees above max temperature"
            .format(str(above_max_value)))
        
        elif temp == max:
            return("at the max temperature")
        
        else:
            if temp > min:
                above_min_value = temp - min
                below_max_value = max - temp
                if (above_min_value) < (below_max_value):
                    return("{} degrees above min temperature"
                    .format(str(above_min_value)))
                else:
                    return("{} degrees below max temperature"
                    .format(str(below_max_value)))

            elif temp == min:
                return("at the min temperature")
            else:
                below_min_value = min - temp
                return("{} degrees below min temperature"
                .format(str(below_min_value)))

    # Separate function to check humidity
    @classmethod
    def check_humidity(cls, humidity):
        max = cls.max_humidity
        min = cls.min_humidity
        
        # Range checking algorithm
        if humidity > max:
            above_max_value = humidity - max
            return("{} percent above max humidity"
            .format(str(above_max_value)))
        
        elif humidity == max:
            return("at the max humidity")
        
        else:
            if humidity > min:
                above_min_value = humidity - min
                below_max_value = max - humidity
                if (above_min_value) < (below_max_value):
                    return("{} percent above min humidity"
                    .format(str(above_min_value)))
                else:
                    return("{} percent below max humidity"
                    .format(str(below_max_value)))

            elif humidity == min:
                return("at the min humidity")
            else:
                below_min_value = min - humidity
                return("{} percent below min humidity"
                .format(str(below_min_value)))


    





