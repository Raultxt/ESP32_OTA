from machine import Pin
from time import sleep

# Definir el pin donde está conectado el LED
led = Pin(2, Pin.OUT)  # GPIO 2 como salida

while True:
    led.on()  # Encender el LED
    sleep(1)  # Esperar 1 segundo
    led.off()  # Apagar el LED
    sleep(1)  # Esperar 1 segundo
