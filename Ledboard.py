import RPi.GPIO as GPIO
import time

class Ledboard():
    def __init__(self):
        self.pins = [18, 23, 24]  # Set the proper mode via: GPIO.setmode(GPIO.BCM).
        self.pin_led_states = [
            [1, 0, -1], # 1
            [0, 1, -1], # 2
            [1, -1, 0], # 3
            [0, -1, 1], # 4
            [-1, 1, 0], # 5
            [-1, 0, 1], # 6

        ]
        GPIO.setmode(GPIO.BCM)

    def set_pin(self, pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    def turn_on_led(self, Lid):  # Skru på lys
        for pin_index, pin_state in enumerate(self.pin_led_states[Lid-1]):
            self.set_pin(pin_index, pin_state)

    def shut_off_lights(self):  # Skru av lys
        for i in range (0,3):
            self.set_pin(i, 0)

    def light_led(self, Lid, Ldur):  # Lys opp ett lys
        # for pin_index, pin_state in enumerate(pin_led_states[led_number]):
        # set_pin(pin_index, pin_state)

        #TODO Light the led width the lednr from the input
        self.turn_on_led(Lid)
        print("Lights led",Lid,"for",Ldur,"sekunds")
        time.sleep(Ldur)
        self.shut_off_lights()

    def light_all(self,Ldur):  # Skru på alle lys
        timeout = time.time() + Ldur
        while time.time() <= timeout:
            for i in range(1,7):
                self.turn_on_led(i)
        self.shut_off_lights()

    def flash_all_leds(self, flashes = 5, dif = 0.25): # Flah alle lys
        print("All leds flashing")
        for i in range (0,flashes):
            self.light_all(dif)
            time.sleep(dif)

    def twinkle_all_leds(self, Ldur):  # Twinkle lys
        timeout = time.time() + Ldur
        print("All leds twinkle")
        while time.time() <= timeout:
            for i in range(1,7):
                self.light_led(i, 0.2)
        self.shut_off_lights()

    def power_up(self):  # Start opp
        for i in range (1,7):
            self.light_led(i,0.2)
        self.flash_all_leds(3,0.1)
        print("Power upp animation")

    def power_down(self):  # Slå av
        self.flash_all_leds(3,0.1)
        for i in range (1,7):
            self.light_led(i,0.2)
        print("Power down animation")
        #TODO a sequence og lighting signaling power down

# set_pin(0, -1)
# set_pin(1, -1)
# set_pin(2, -1)

# while True:
#   x = int(raw_input("Pin (0 to 5):"))
#   light_led(x)

#setup - Set the proper mode via: GPIO.setmode(GPIO.BCM).

#• light led - Turn on one of the 6 LEDs by making the appropriate combination of input and output
#declarations, and then making the appropriate HIGH / LOW settings on the output pins.

#• flash all leds - Flash all 6 LEDs on and off for k seconds, where k is an argument of the method.

#• twinkle all leds - Turn all LEDs on and off in sequence for k seconds, where k is an argument of the
#method.