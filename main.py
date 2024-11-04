import machine
import time

print("Ejecutando main.py...")  # Mensaje de depuración para verificar

led = machine.Pin(2, machine.Pin.OUT)  # Cambia 2 por el pin correcto si es necesario

while True:
    led.value(1)  # Enciende el LED
    time.sleep(5)  # Espera 1 segundo
    led.value(0)  # Apaga el LED
    time.sleep(5)  # Espera otro segundo
