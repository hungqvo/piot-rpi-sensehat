from sense_hat import SenseHat
from time import sleep
class Emoji:
    sense = SenseHat()
    def __init__(self, e, m, f):
        self.eyes = e
        self.mouth = m
        self.face = f
    
    def display(self):
        e = self.eyes
        m = self.mouth
        f = self.face
        smilef_face = [
            (0,0,0), f, f, f, f, f, f, (0,0,0),
            f, f, f, f, f, f, f, f,
            f, e, e, f, f, e, e, f,
            f, e, e, f, f, e, e, f,
            f, f, f, f, f, f, f, f,
            f, m, m, f, f, m, m, f,
            f, f, f, m, m, f, f, f,
            (0,0,0), f, f, f, f, f, f,(0,0,0) 
            ]
    
        frowning_face =  [
            (0,0,0), f, f, f, f, f, f, (0,0,0),
            f, f, f, f, f, f, f, f,
            f, e, e, f, f, e, e, f,
            f, e, e, f, f, e, e, f,
            f, f, f, f, f, f, f, f,
            f, f, f, m, m, f, f, f,
            f, f, m, f, f, m, f, f,
            (0,0,0), m, f, f, f, f, m,(0,0,0) 
            ]

        freak_out = [
            (0,0,0), f, f, f, f, f, f, (0,0,0),
            f, f, f, f, f, f, f, f,
            f, e, e, f, f, e, e, f,
            f, e, e, f, f, e, e, f,
            f, f, f, f, f, f, f, f,
            f, m, f, m, f, m, f, f,
            f, f, m, f, m, f, m, f,
            (0,0,0), f, f, f, f, f, f,(0,0,0) 
            ]
        while True:
            self.sense.set_pixels(smilef_face)
            sleep(3)
            self.sense.set_pixels(frowning_face)
            sleep(3)
            self.sense.set_pixels(freak_out)
            sleep(3)

y = (255,255,0)
b = (0,0,255)
r = (255,0,0)
emoji = Emoji(y,r,b)
emoji.display()
