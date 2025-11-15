from machine import Pin, ADC
import time

#program shows when output of serial pin changes

print("Started observing pin")

#code for digital pin - my chip operates on 1.8-2.1V, giving 0.45V as LOW and 1.35-1.75V as HIGH, which doesn't really cooperate with the Raspberry's digital input
"""
pin = Pin(2, Pin.IN, Pin.PULL_DOWN)
last_value = pin.value()
while True:
    current_value = pin.value()
    time.sleep(0.001) #wait a bit to make sure we're not seeing noise
    if current_value != last_value:
        print(f"Changed to: {current_value}")
        last_value = current_value
    time.sleep(0.0001)
"""


#code for analog pin:
adc = ADC(26)
last_voltage = 0.3
while True:
    raw_data = adc.read_u16()
    voltage = round((raw_data * 1.9 / 65535), 1)
    if voltage > 1:
        value = 1
    else:
        value = 0
    print(f"Raw: {raw_data}, Voltage: {voltage}, Value: {value}")
    time.sleep(0.01) #temporary