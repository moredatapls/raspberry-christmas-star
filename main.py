import sys

from flask import Flask
from flask_restful import Api

from controllers.Index import Index
from controllers.SingleColor import SingleColor
from dependencies.Container import Container
from star.MockStar import MockStar
from star.Star import Star

app = Flask(__name__, template_folder='static')
api = Api(app)
port = 8080

if sys.argv.__len__() > 1:
    port = sys.argv[1]

print("API running on port : {}".format(port))

if app.env == "PRODUCTION":
    container = Container(Star())
elif app.env == "DEVELOPMENT":
    container = Container(MockStar())
else:
    raise ValueError("Unsupported environment: " + str(app.env))

api.add_resource(SingleColor, '/single-color', resource_class_kwargs={'container': container})
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run("0.0.0.0", port, debug=True)
