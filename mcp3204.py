import spidev
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 30500

while True:
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(11,GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(11, GPIO.LOW)

    to_send = [0x60]
    spi.xfer(to_send)

    data = spi.readbytes(2)

    value = (data[0]*256 + data[1]>>3) / 4096
    print(value)

