import wiringpi
import time
from wiringpi import GPIO

class GpiosManager():
    def __init__(self):
        super().__init__()
        wiringpi.wiringPiSetup()
        #pines de salidas
        self.relay_1 = 8
        self.relay_2 = 11
        # declaracion de salidas
        wiringpi.pinMode(self.relay_1, GPIO.OUTPUT)
        wiringpi.pinMode(self.relay_2, GPIO.OUTPUT)

        def turnstileOpen(self):
            wiringpi.digitalWrite(self.relay_1, GPIO.LOW)
            wiringpi.digitalWrite(self.relay_1, GPIO.LOW)
            time.sleep(1)
            wiringpi.digitalWrite(self.relay_1, GPIO.HIGH)
            wiringpi.digitalWrite(self.relay_1, GPIO.HIGH)
            return "puerta general abierta"