import RPi.GPIO as GPIO
import spidev
from time import sleep

spi = spidev.SpiDev()  #enable spi
CS = 0 #pin for chip select cs is active low
spi.open(0, CS)#open and initialize the SPI communication with a specific SPI device connected to the SPI bus.
# bus port 0 and cs pin to establish spi
spi.max_speed_hz = 4300000# MAX6675(ADC) is of 4.3MHz 
spi.mode = 0
data= 0x23
spi.xfer2(data)
sleep(2)
print("i finished transmitting")

