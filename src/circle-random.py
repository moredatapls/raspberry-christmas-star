import board
import neopixel
import time
import random

gpioPin = board.D12 # has to be PWM compatible
numPixels = 11

sleepDurationSecs = 0.1

pixels = neopixel.NeoPixel(gpioPin, numPixels, brightness=1.0)

pixels.fill((0, 0, 0))

pLast = 0

def allRandom():
	color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
	return color

def shadesOfGreen():
	color = (random.randrange(0, 127), 255, random.randrange(0, 127))
	return color

while True:
	color = shadesOfGreen() #allRandom()

	for p in range(numPixels):
		pixels[p] = color

		pixels.show()

		print("p=" + str(p) + ",color=" + str(color))

		pLast = p

		time.sleep(sleepDurationSecs)
