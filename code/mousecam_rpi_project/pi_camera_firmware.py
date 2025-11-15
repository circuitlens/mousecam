from machine import Pin, ADC
import time

# written for PAW3256, using register map from a datasheet for PAW3335, seems to be compatible thankfully

# chip pins:
# 1 - LED
# 2 - VDDREG
# 3 - VDD (expects 1.8-2.1V)
# ! 4 - SCLK - serial clock input
# 5 - MOTION
# 6 - GND
# ! 7 - SDIO - serial i/o
# ! 8 - NCS - chip select (active low)


# the PAW3256 runs on a lower voltage than my pi, thus I'm trying to send serial input from a digital pin via a voltage divider
# serial output is being read by an analog pin and interpreted in-program
SDIO_send = Pin(2, Pin.OUT, Pin.PULL_UP)
SDIO_receive = ADC(26)



