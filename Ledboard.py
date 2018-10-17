#CLASS ledboard

import RPi.GPIO as GPIO

class Ledboard:

    def setup(self):
        pins = [18, 23, 24]  # Set the proper mode via: GPIO.setmode(GPIO.BCM).
        pin_led_states = [
            [1, 0, -1],  # A
            [0, 1, -1],  # B
            [-1, 1, 0],  # C
            [-1, 0, 1],  # D
            [1, -1, 0],  # E
            [0, -1, 1]  # F
        ]
        GPIO.setmode(GPIO.BCM)

    def light_led(led_number):  # Turn on one of the 6 LEDs by making the appropriate combination of input and output declarations, and then making the appropriate HIGH / LOW settings on the output pins.
        for pin_index, pin_state in enumerate(pin_led_states[led_number]):
            set_pin(pin_index, pin_state)

    def flash_all_leds(self,k):
        return

    def twinkle_all_leds(self,k):
        return

    def set_pin(pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(pins[pin_index], GPIO.OUT)
            GPIO.output(pins[pin_index], pin_state)

    def light_led(self):
      return

    def flash_all_leds(self):  # Flash all 6 LEDs on and o↵ for k seconds, where k is an argument of the method.
        return

    def twinkle_all_leds(self):  # Turn all LEDs on and o↵ in sequence for k seconds, where k is an argument of the method
        return

    def lightshow(self):


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