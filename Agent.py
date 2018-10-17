

class Agent:

    def __init__(self, keypad, led_board, passcode_buffer, pathname, Lid, Ldur):
        self.keypad = keypad #a pointer to the keypad
        self.led_board = led_board #pointer to the LED Board
        self.passcode_buffer = passcode_buffer
        self.pathname = pathname  #pathname to the file holding the KPC’s password
        self.override_signal = None
        self.led_id = Lid  #slots for holding the LED id
        self.led_time = Ldur


    def init_passcode_entry(self):
        self.passcode_buffer = []
        self.led_board.light_led()


    def get_next_signal(self):
        if self.override_signal != None:
            return self.override_signal
        self.keypad.get_next_signal()



    def verify_login(self): #lese filen og sjekke om passordet stemmer
        file = open("pathname", "r")
        password = file.read()  #leser inn filen og oppretter en streng med ordene
        file.close()
        if password == self.passcode_buffer: #sjekker om passordet lagret i filen er lik passordet tastet inn
            self.override_signal = "Y"
            return True
        self.override_signal = "N"
        return False
    #Also, this should call the LED Board to initiate the
    # appropriate lighting pattern for login success or failure.


    def validate_passcode_change(self, password):
        if password.isdigit() and len(password) > 3:
            return True
        return False

    #def reset_password


    #def check_password


    def light_one_led(self):
        self.led_board.light_led(self.led_id, self.led_time)


    def flash_leds(self):
        self.led_board.flash_all_leds(self.led_time)

    def twinkle_leds(self):
        self.led_board.twinkle_all_leds(self.led_time)


    def exit_action(self):
        return



# • light one led - Using values stored in the Lid and Ldur slots, call the LED Board and request that
    # LED # Lid be turned on for Ldur seconds.
    # • flash leds - Call the LED Board and request the flashing of all LEDs.
    # • twinkle leds - Call the LED Board and request the twinkling of all LEDs.
    # • exit action - Call the LED Board to initiate the ”power down” lighting sequence




#• init passcode entry - Clear the passcode-buffer and initiate a ”power up” lighting sequence on the LED
#Board. This should be done when the user first presses the keypad.
#• get next signal - Return the override-signal, if it is non-blank; otherwise query the keypad for the next
#pressed key.
#• verify login - Check that the password just entered via the keypad matches that in the password file.
#Store the result (Y or N) in the override-signal. Also, this should call the LED Board to initiate the
#appropriate lighting pattern for login success or failure.
#• validate passcode change - Check that the new password is legal. If so, write the new password in the
#password file. A legal password should be at least 4 digits long and should contain no symbols other
#than the digits 0-9. As in verify login, this should use the LED Board to signal success or failure in
#changing the password.2
#• light one led - Using values stored in the Lid and Ldur slots, call the LED Board and request that
#LED # Lid be turned on for Ldur seconds.
#• flash leds - Call the LED Board and request the flashing of all LEDs.
#• twinkle leds - Call the LED Board and request the twinkling of all LEDs.
#• exit action - Call the LED Board to initiate the ”power down” lighting sequence





#• init passcode entry - Clear the passcode-buffer and initiate a ”power up” lighting sequence on the LED
#Board. This should be done when the user first presses the keypad.

#• get next signal - Return the override-signal, if it is non-blank; otherwise query the keypad for the next
#pressed key.

#• verify login - Check that the password just entered via the keypad matches that in the password file.
#Store the result (Y or N) in the override-signal. Also, this should call the LED Board to initiate the
#appropriate lighting pattern for login success or failure.

#• validate passcode change - Check that the new password is legal. If so, write the new password in the
#password file. A legal password should be at least 4 digits long and should contain no symbols other
#than the digits 0-9. As in verify login, this should use the LED Board to signal success or failure in
#changing the password.2

#• light one led - Using values stored in the Lid and Ldur slots, call the LED Board and request that
#LED # Lid be turned on for Ldur seconds.

#• flash leds - Call the LED Board and request the flashing of all LEDs.
#• twinkle leds - Call the LED Board and request the twinkling of all LEDs.
#• exit action - Call the LED Board to initiate the ”power down” lighting sequence