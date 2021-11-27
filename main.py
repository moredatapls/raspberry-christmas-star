import sys

from flask import Flask
from flask_restful import Api
from controllers.Index import Index
from controllers.SingleColor import SingleColor

app = Flask(__name__, template_folder='static')
api = Api(app)
port = 8080

if sys.argv.__len__() > 1:
    port = sys.argv[1]

print("API running on port : {}".format(port))

api.add_resource(SingleColor, '/single-color')
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run("0.0.0.0", port, debug=True)
