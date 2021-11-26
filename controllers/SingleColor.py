import board
import neopixel
from flask import request
from flask_restful import Resource


class SingleColor(Resource):
    @staticmethod
    def post():
        r = int(request.args.get("r"))
        g = int(request.args.get("g"))
        b = int(request.args.get("b"))

        pixels = neopixel.NeoPixel(board.D12, 11)

        pixels.fill((r, g, b))

        return {'op': 'single-color', 'params': {'r': r, 'g': g, 'b': b}}
