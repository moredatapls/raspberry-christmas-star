from flask import request
from flask_restful import Resource

from dependencies.Container import Container


class SingleColor(Resource):
    def __init__(self, container: Container):
        self.star = container.get_star()

    def post(self):
        color = request.form.get("color")

        # should be valid hex: #123456
        if color is not None and len(color) == 7:
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)

            self.star.set_color(r, g, b)

        return {'color': color}
