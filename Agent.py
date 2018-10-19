class Agent:
    def __init__(self, keypad, led_board, passcode_buffer, pathname, Lid, Ldur):
        self.keypad = keypad #a pointer to the keypad
        self.led_board = led_board #pointer to the LED Board
        self.passcode_buffer = passcode_buffer
        self.pathname = pathname  #pathname to the file holding the KPC’s password
        self.override_signal = None
        self.led_id = Lid  #slots for holding the LED id
        self.led_time = Ldur
        self.temp_password = ""

    def activate_agent(self):
        return

    def null_action(self): #Resetter agenten (?) og passord(?)
        pass

    def get_next_signal(self):
        if self.override_signal != None:
            return self.override_signal
        self.keypad.get_next_signal()

    def verify_login(self): #lese filen og sjekke om passordet stemmer
        file = open("self.pathname.txt", "r")
        password = file.read()  #leser inn filen og oppretter en streng med ordene
        file.close()
        if password == self.passcode_buffer: #sjekker om passordet lagret i filen er lik passordet tastet inn
            self.override_signal = "Y"
            return True
        self.override_signal = "N"
        return False

    def validate_passcode_change(self, password):
        if password.isdigit() and len(password) > 3:
            return True
        return False

    def startup(self): #Få lys til å blinke og reset password
        self.reset_password()
        self.flash_leds()

    def login(self): #Twinkle lights og verify login
        self.verify_login()
        self.twinkle_leds()

    # PASSORD
    def init_passcode_entry(self):
        self.passcode_buffer = []
        self.led_board.light_led()

    def add_symbol_password(self):
        self.temp_password.append(keypad)  # Legg til det vi skriver inn i keypaden

    def reset_password(self):
        self.cach_password()

    def clear_password(self):
        #for i in range(len(self.temp_password)):
           # self.temp_password.pop()
        self.temp_password = ""

    def validate_password(self):

    # Sjekker om elementene i temp_password er lik tallene i tekstfilen med passord
    def cach_password(self, password):  # SAVE NEW PASSWORD
        #  Lagre filen med nytt passord som ny tekstfil med passord
        f = open("self.pathname.txt", "w")
        f.write(password)
        f.close()

    #LYS
    def set_led_id(self):
        self.led_id = keypad #Setter id til det vi har trykket på keypaden

    def set_led_time(self):
        self.led_time += Int(keypad) #Legger til taller vi har skrevet inn i ledd helt til vi trykker *

    def reset_led(self):
        self.led_time = 0

    def light_one_led(self):
        self.led_board.light_led(self.led_id, self.led_time)

    def flash_leds(self):
        self.led_board.flash_all_leds(self.led_time)

    def twinkle_leds(self):
        self.led_board.twinkle_all_leds(self.led_time)

    def exit_action(self):
        self.led_board.twinkle_all_leds(2) #Blinker i 2 sek
        self.led_board.flash_all_leds(3) #Flash i 3 sek
        self.led_board.twinkle_all_leds(2) #Blinker i 2 sek


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