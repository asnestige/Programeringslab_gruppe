
import RPi.GPIO as GPIO
import time

#CLASS keypad

class Keypad:

    rows = [18, 23, 24, 25] #rowpins
    columns = [17, 27, 22] #columnpins
    symbols = {"nokey": "No key", "1817": 1, "1827": 2, "1822": 3, "2317": 4, "2327": 5, "2322": 6, "2417": 7, "2427": 8, "2422": 9, "2517": '*', "2527": 0, "2522": '#'}

    def __init__(self):  #setup the keypad with the correct rowpins and columnpins
        GPIO.setmode(GPIO.BCM)

        for row in self.rows:
            GPIO.setup(row, GPIO.OUT)

        for col in self.columns:
            GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


    def do_polling(self):

        match = False #variabel for å si ifra at vi har funnet en match
        keystring = "nokey"
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



    def get_next_signal(self):
        count = 0
        prevkey = self.do_polling()
        key = None

        while count < 20: #må sjekke flere ganger for å være sikker på at det er et "ordentlig" trykk
            key = self.do_polling()

            if key != "nokey": #har funnet en nøkkel

                if key == prevkey:
                    count += 1

                else: #key != prevkey
                    prevkey = key
                    count = 0

            time.sleep(0.010)

        return key

    #Finally, to avoid noisy inputs from the column pins, it helps to consider the column pin to be actually high
#only if repeated measurements (for example, 20 in a row with a 10 millisecond delay between each reading)
#all show a high value. You can use the time.sleep() command from Python’s time package to support this
#simple (but very important) measure-wait-measure loop.

#• get next signal - This is the main interface between the agent and the keypad. It should initiate
#repeated calls to do polling until a key press is detected.





#This is the main interface between the agent and the keypad. It should initiate
#repeated calls to do polling until a key press is detected.


#setup - Set the proper mode via: GPIO.setmode(GPIO.BCM). Also, use GPIO functions to set the
#row pins as outputs and the column pins as inputs.
#• do polling - Use nested loops (discussed above) to determine the key currently being pressed on the
#keypad.
#• get next signal - This is the main interface between the agent and the keypad. It should initiate
#repeated calls to do polling until a key press is detected.