import board
import neopixel
import time

gpioPin = board.D12 # has to be PWM compatible
numPixels = 11

sleepDurationSecs = 0.2

pixels = neopixel.NeoPixel(gpioPin, numPixels)

pixels.fill((0, 0, 0))

pLast = 0

while True:
	for p in range(numPixels):
		print("now=" + str(p))
		print("last=" + str(pLast))

		pixels[pLast] = (0, 0, 0)
		pixels[p] = (0, 255, 0)

		pixels.show()

		pLast = p

		time.sleep(sleepDurationSecs)
