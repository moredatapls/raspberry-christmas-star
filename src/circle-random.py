import board
import neopixel
import time
import random

gpioPin = board.D12 # has to be PWM compatible
numPixels = 11

sleepDurationSecs = 0.2

pixels = neopixel.NeoPixel(gpioPin, numPixels, brightness=0.5)

pixels.fill((0, 0, 0))

pLast = 0

while True:
	for p in range(numPixels):
		color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

		pixels[p] = color

		pixels.show()

		print("p=" + str(p) + ",color=" + str(color))

		pLast = p

		time.sleep(sleepDurationSecs)
