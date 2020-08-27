from sense_hat import SenseHat
import random
import time

class eDie:
    # Symbolic initialization
    sense = SenseHat()
    
    # Setup the color
    d = [0, 0, 0]           # Default: Black
    g = [0, 255, 0]         # Green
    b = [0, 0, 255]         # Blue

    # Configure the dice on LED matrix
    # Player 1 dice pixel matrix
    one_p1 = [
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    ]

    two_p1 = [
    d,d,d,d,d,d,d,d,
    d,b,b,d,d,d,d,d,
    d,b,b,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,b,b,d,
    d,d,d,d,d,b,b,d,
    d,d,d,d,d,d,d,d,
    ]

    three_p1 = [
    b,b,d,d,d,d,d,d,
    b,b,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,b,b,
    d,d,d,d,d,d,b,b,
    ]

    four_p1 = [
    d,d,d,d,d,d,d,d,
    d,b,b,d,d,b,b,d,
    d,b,b,d,d,b,b,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,b,b,d,d,b,b,d,
    d,b,b,d,d,b,b,d,
    d,d,d,d,d,d,d,d,
    ]

    five_p1 = [
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    d,d,d,d,d,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,d,d,d,d,d,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    ]

    six_p1 = [
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    d,d,d,d,d,d,d,d,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    d,d,d,d,d,d,d,d,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    ]

    # Player 2 dice pixel matrix
    one_p2 = [
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    ]

    two_p2 = [
    d,d,d,d,d,d,d,d,
    d,g,g,d,d,d,d,d,
    d,g,g,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,g,g,d,
    d,d,d,d,d,g,g,d,
    d,d,d,d,d,d,d,d,
    ]

    three_p2 = [
    g,g,d,d,d,d,d,d,
    g,g,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,g,g,
    d,d,d,d,d,d,g,g,
    ]

    four_p2 = [
    d,d,d,d,d,d,d,d,
    d,g,g,d,d,g,g,d,
    d,g,g,d,d,g,g,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,g,g,d,d,g,g,d,
    d,g,g,d,d,g,g,d,
    d,d,d,d,d,d,d,d,
    ]

    five_p2 = [
    g,g,d,d,d,d,g,g,
    g,g,d,d,d,d,g,g,
    d,d,d,d,d,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,d,d,d,d,d,
    g,g,d,d,d,d,g,g,
    g,g,d,d,d,d,g,g,
    ]

    six_p2 = [
    g,g,d,d,d,d,g,g,
    g,g,d,d,d,d,g,g,
    d,d,d,d,d,d,d,d,
    g,g,d,d,d,d,g,g,
    g,g,d,d,d,d,g,g,
    d,d,d,d,d,d,d,d,
    g,g,d,d,d,d,g,g,
    g,g,d,d,d,d,g,g,
    ]

    @classmethod
    def die_roll(cls,player):        
        # Generate random number from 1 to 6
        randomNumber = random.randint(1,6)
        
        # Set the dice on LED Matrix
        if randomNumber == 1:
            if player == 1:
                cls.sense.set_pixels(cls.one_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.one_p2)

        elif randomNumber == 2:
            if player == 1:
                cls.sense.set_pixels(cls.two_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.two_p2)

        elif randomNumber == 3:
            if player == 1:
                cls.sense.set_pixels(cls.three_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.three_p2)

        elif randomNumber == 4:
            if player == 1:
                cls.sense.set_pixels(cls.four_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.four_p2)

        elif randomNumber == 5:
            if player == 1:
                cls.sense.set_pixels(cls.five_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.five_p2)

        elif randomNumber == 6:
            if player == 1:
                cls.sense.set_pixels(cls.six_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.six_p2)
                
        time.sleep(1)
        cls.sense.clear()        
        return(randomNumber)        

    @classmethod
    def check_movement(cls,player):
        # Get accelerometer from SenseHat    
        acceleration = cls.sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = abs(x)
        y = abs(y)
        z = abs(z)
        
        # Sensitivity to filter out accidental shakes
        if x > 1.2 or y > 1.2 or z > 1.2:            
            if player == 1:                
                result = eDie.die_roll(1)                 
                return result
            
            elif player == 2:                
                result = eDie.die_roll(2)                 
                return result          
        
        else:
            return eDie.check_movement(player)            

    

