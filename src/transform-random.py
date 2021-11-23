import board
import neopixel
import time
import random
import math

gpioPin = board.D12 # has to be PWM compatible
numPixels = 11

sleepDurationSecs = 0.01
numSteps = 50

pixels = neopixel.NeoPixel(gpioPin, numPixels, brightness=1.0)

pixels.fill((0, 0, 0))

pLast = 0

currentColor = (0, 0, 0)

def allRandom():
	color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
	return color

def shadesOfGreen():
	color = (random.randrange(0, 127), 255, random.randrange(0, 127))
	return color

while True:
	newColor = allRandom()

	deltaR = float(newColor[0] - currentColor[0]) / numSteps
	deltaG = float(newColor[1] - currentColor[1]) / numSteps
	deltaB = float(newColor[2] - currentColor[2]) / numSteps

	print("new=" + str(newColor))
	print("deltas=" + str(deltaR) + "," + str(deltaG) + "," + str(deltaB))

	for p in range(numSteps):
		currentColor = (math.floor(currentColor[0] + deltaR), math.floor(currentColor[1] + deltaG), math.floor(currentColor[2] + deltaB))

		currentColor = (max(0, min(currentColor[0], 255)), max(0, min(currentColor[1], 255)), max(0, min(currentColor[2], 255)))

		print("current(" + str(p) + ")=" + str(currentColor))

		pixels.fill(currentColor)

		time.sleep(sleepDurationSecs)
