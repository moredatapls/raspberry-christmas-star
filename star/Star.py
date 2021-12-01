from star.AbstractStar import AbstractStar


class Star(AbstractStar):
    # pin 10 == GPIO 12 on the board
    def __init__(self, pin: int = 10, num_leds: int = 11):
        # lazy-load the dependencies here so that it doesn't break non-Raspberry Pi environments
        import neopixel
        from microcontroller import Pin

        self.pixels = neopixel.NeoPixel(Pin(pin), num_leds)

    def set_color(self, r: int, g: int, b: int):
        self.pixels.fill((r, g, b))
        self.pixels.show()
