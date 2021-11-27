from flask import render_template, make_response
from flask_restful import Resource


class Index(Resource):
    @staticmethod
    def get():
        return make_response(render_template('index.html'), 200, {'Content-Type': 'text/html'})
