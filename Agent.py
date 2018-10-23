from Keypad import Keypad as keypad
from Ledboard import Ledboard as led

class Agent:
    def __init__(self, keypad, led_board, pathname):
        self.keypad = keypad  # a pointer to the keypad
        self.led_board = led_board  # pointer to the LED Board
        self.temp_password = ""
        self.pathname = pathname # pathname to the file holding the KPC’s password
        self.override_signal = None
        self.led_id = ""  # slots for holding the LED id
        self.led_time = ""

    def activate_agent(self):
        return

    def null_action(self):  # Resetter agenten (?) og passord(?)
        pass

    def get_next_signal(self):  # Return the override-signal, if it is non-blank; otherwise query the keypad for the next pressed key.
        if self.override_signal != None:
            self.override_signal = None
            print("Inne i override")
            return 'False'
        return self.keypad.get_next_signal()

    def verify_login(self):  # lese filen og sjekke om passordet stemmer
        file = open(self.pathname, "r")
        password = file.read()  # leser inn filen og oppretter en streng med ordene
        print("Passord =", password)
        file.close()
        print("Temp_passord =", self.temp_password)
        if password == self.temp_password:  # sjekker om passordet lagret i filen er lik passordet tastet inn
            self.override_signal = None
            return True
        self.override_signal = 'False'
        return False

    def validate_passcode_change(self, password):
        if password.isdigit() and len(password) > 3:
            return True
        return False

    def startup(self):  # Få lys til å blinke og reset password
        self.clear_password()
        self.led_board.startup_leds()

    def login(self):  # Twinkle lights og verify login
        self.verify_login()
        self.led_board.rightPassword_leds()

    def exit_action(self):
        self.led_board.exit_leds()

    # PASSORD
    def init_passcode_entry(self):
        self.passcode_buffer = []
        self.led_board.light_led()

    def add_symbol_password(self): #FEIL!!!!!!!
        signal = self.get_next_signal()
        print("get", signal)
        if signal == '*' or signal == '#':
            print("* eller #")
            pass
        else:
            print("temp_password =", self.temp_password)
            self.temp_password += str(signal)  # Legg til det vi skriver inn i keypaden

    def clear_password(self):
        self.temp_password = ""

    def cach_password(self):
        if self.validate_passcode_change(self.temp_password):
            f = open(self.pathname, "w")
            f.write(self.temp_password)
            f.close()
            self.flash_leds()  # If password changed
        self.twinkle_leds()  # If fail

    #LYS
    def set_led_id(self):
        self.led_id = self.get_next_signal()  # Setter id til det vi har trykket på keypaden

    def set_led_time(self):
        self.led_time + "" + str(self.get_next_signal())  # Legger til taller vi har skrevet inn i ledd helt til vi trykker *

    def reset_led(self):
        self.led_time = ""

    def light_one_led(self):
        self.led_board.light_led(int(self.led_id), int(self.led_time))

    def flash_leds(self):
        self.led_board.flash_all_leds(int(self.led_time))

    def twinkle_leds(self):
        self.led_board.twinkle_all_leds(int(self.led_time))

