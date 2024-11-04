import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # Pin 2 suele ser el LED en el ESP32

while True:
    led.value(1)  # Enciende el LED
    time.sleep(1)  # Espera 1 segundo
    led.value(0)  # Apaga el LED
    time.sleep(1)  # Espera otro segundo
