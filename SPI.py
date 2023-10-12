import RPi.GPIO as GPIO
import spidev
from time import sleep

spi = spidev.SpiDev()  #enable spi
CS_Pin = 23
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CS_Pin,GPIO.out)
result = 0x0000
spi.open(0)#open and initialize the SPI communication with a specific SPI device connected to the SPI bus.
# bus port 0 to establish spi
spi.max_speed_hz = 1000# MAX6675(ADC) is of 4.3MHz 
spi.mode = 0
GPIO.output(CS_Pin,GPIO.LOW)
spi.writebytes(0)
spi.writebytes (0)
GPIO.output(CS_Pin,GPIO.HIGH)
print("i finished transmitting")

