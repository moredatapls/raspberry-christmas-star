import board
import neopixel
from flask import request
from flask_restful import Resource
from werkzeug.utils import redirect


class SingleColor(Resource):
    @staticmethod
    def post():
        color = request.form.get("color")

        print(color)

        if len(color) == 7:
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)

            print(r)
            print(g)
            print(b)

            pixels = neopixel.NeoPixel(board.D12, 11)

            pixels.fill((r, g, b))

        return redirect('/')
