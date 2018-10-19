
import RPi.GPIO as GPIO
import time

#CLASS keypad

class Keypad:

    rows = [18, 23, 24, 25] #rowpins
    columns = [17, 27, 22] #columnpins
    symbols = { "1817": 1}

    def __init__(self):  #setup the keypad with the correct rowpins and columnpins
        GPIO.setmode(GPIO.BCM)

        for row in self.rows:
            GPIO.setup(row, GPIO.OUT)

        for col in self.columns:
            GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


    def do_polling(self):

        match = False #variabel for å si ifra at vi har funnet en match

        for r in self.rows:
            GPIO.output(r, GPIO.HIGH)

            for c in self.columns:
                if GPIO.input(c) == GPIO.HIGH:
                    x = True
                    keystring = str(r) + str(c)

            if match:
                break

            GPIO.output(r, GPIO.LOW) #må sette den low før vi går til neste rad-element

        return self.symbols[keystring]



#Use nested loops (discussed above) to determine the key currently being pressed on the
#keypad.

    def get_next_signal(self):
        
        return



#setup - Set the proper mode via: GPIO.setmode(GPIO.BCM). Also, use GPIO functions to set the
#row pins as outputs and the column pins as inputs.
#• do polling - Use nested loops (discussed above) to determine the key currently being pressed on the
#keypad.
#• get next signal - This is the main interface between the agent and the keypad. It should initiate
#repeated calls to do polling until a key press is detected.