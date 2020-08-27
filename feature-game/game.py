from sense_hat import SenseHat
import time
from datetime import datetime
from electronicDie import eDie
from writeToCsv import csvHandler

class Game:
    # Symbolic initialization
    sense = SenseHat()
    continued = True
    instruction_show = True
    p1_turn_toggle = True
    p2_turn_toggle = True
    p1 = 0          # Player score
    p2 = 0
    counter_p1 = 0  # Player turn counter
    counter_p2 = 0
    winner = 0      # Winner variables
    winner_score = 0
    winner_turns = 0

    # Setup the color
    g = [0, 255, 0]         # Green
    b = [0, 0, 255]         # Blue
    p = [160, 32, 240]      # Purple
    
    # Introduce the game
    @classmethod
    def show_intro(cls):
        cls.sense.show_message("Welcome to Shake the Dice 30!",\
             text_colour=cls.p, scroll_speed=0.08)
        time.sleep(0.5)
        cls.sense.show_message("shake the Pi and get 30 first to win", \
            text_colour=cls.p, scroll_speed=0.08)
        
        time.sleep(0.5)
        cls.sense.show_message("< use joystick to select >", \
            text_colour=cls.p, scroll_speed=0.08)
        cls.sense.show_message("<< P1 <<", text_colour=cls.b, scroll_speed=0.08)        
        cls.sense.show_message(">> P2 >>", text_colour=cls.g, scroll_speed=0.08)

        time.sleep(0.5)
        cls.sense.show_message("Go!",text_colour=cls.p, scroll_speed=0.08)
        cls.sense.clear()
        
        # Start game
        cls.start_game()

    # When player 1 toggles left joystick
    @classmethod
    def left_pushed(cls,event):        
        # Player pressed and released the joystick      
        if event[2] == "released":            
            cls.sense.show_message("P1", text_colour=cls.b, scroll_speed = 0.04)                 
            time.sleep(0.01)
            result = eDie.check_movement(1)
            # If the player shakes the dice
            if result != None:
                cls.counter_p1 += 1
                cls.p1 += result               
            else:
                cls.right_pushed(event)
            # If the player reaches 30 first
            if cls.p1 > 30:
                cls.winner = 1
                cls.winner_score = cls.p1
                cls.winner_turns = cls.counter_p1
                cls.continued = False
        cls.sense.clear()

    # When player 2 toggles right joystick
    @classmethod
    def right_pushed(cls,event):                
        # Player pressed and released the joystick
        if event[2] == "released":
            # while cls.p1_turn_toggle:
            cls.sense.show_message("P2", text_colour=cls.g, scroll_speed = 0.04)           
            time.sleep(0.01)            
            result = eDie.check_movement(2)
            # If the player shakes the dice           
            if result != None:                                
                cls.counter_p2 += 1
                cls.p2 += result
            else:
                cls.right_pushed(event)

            # If the player reaches 30 first
            if cls.p2 > 30:
                cls.winner = 2
                cls.winner_score = cls.p2
                cls.winner_turns = cls.counter_p2
                cls.continued = False
        cls.sense.clear()

    @classmethod
    def start_game(cls):   
        cls.sense.stick.direction_left = cls.left_pushed
        cls.sense.stick.direction_right = cls.right_pushed

        # Continue the game till stop trigger
        while cls.continued:
            pass

        # Acknowledge the winner
        if cls.winner == 1:        
            cls.sense.show_message("P1 wins!", text_colour=cls.b,\
            scroll_speed=0.08)
        elif cls.winner == 2:                    
            cls.sense.show_message("P2 wins!", text_colour=cls.g,\
            scroll_speed=0.08)    

        time.sleep(0.5)

        # End the game with message
        cls.sense.show_message("Game over! That was fun!", \
            text_colour=cls.p, scroll_speed=0.08)

        result_message = "Player {} wins with {} points in {} turns"\
            .format(cls.winner, cls.winner_score, cls.winner_turns)
        
        # Write to csv file
        csvHandler.write_to_csv(result_message)
                
# Start the program
Game.show_intro()
