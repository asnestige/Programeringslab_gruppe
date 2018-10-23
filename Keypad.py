import RPi.GPIO as GPIO
import time

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
        prevkey = "start"
        key = None

        while count < 20: #må sjekke flere ganger for å være sikker på at det er et "ordentlig" trykk
            key = self.do_polling()
            if key != "No key": #har funnet en nøkkel

                if prevkey == "base":
                    prevkey = key
                    count += 1

                elif key == prevkey:
                    count += 1

                else: #key != prevkey
                    prevkey = "base"
                    count = 0

            time.sleep(0.010)
        print("keypad key =", key)
        return key
