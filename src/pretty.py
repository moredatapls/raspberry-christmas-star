import board
import neopixel

pixels = neopixel.NeoPixel(board.D12, 11)

pixels.fill((255,150,25))
