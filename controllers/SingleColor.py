from flask import request
from flask_restful import Resource


class SingleColor(Resource):
    @staticmethod
    def post():
        color = request.args.get("color")

        return {'color': color}
