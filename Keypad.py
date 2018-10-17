

#CLASS keypad

class Keypad:


    def setup(self):
        return


    def do_polling(self):
        return


    def get_next_signal(self):
        return

# get next signal - This is the main interface between the agent and the keypad. It should initiate
# repeated calls to do polling until a key press is detected.




# setup - Set the proper mode via: GPIO.setmode(GPIO.BCM). Also, use GPIO functions to set the
#row pins as outputs and the column pins as inputs.
# do polling - Use nested loops (discussed above) to determine the key currently being pressed on the keypad.

