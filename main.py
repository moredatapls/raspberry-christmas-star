from flask import Flask
from flask_restful import Api

from controllers.Index import Index
from controllers.SingleColor import SingleColor
from dependencies.Container import Container
from star.MockStar import MockStar
from star.Star import Star

app = Flask(__name__, template_folder='static')
api = Api(app)

if app.env == "production":
    container = Container(Star())
    port = 80
elif app.env == "development":
    container = Container(MockStar())
    port = 8080
else:
    raise ValueError("Unsupported environment: " + str(app.env))

api.add_resource(SingleColor, '/single-color', resource_class_kwargs={'container': container})
api.add_resource(Index, '/')

if __name__ == '__main__':
    # set some color on startup
    container.get_star().set_color(117, 54, 255)

    app.run("0.0.0.0", port, debug=True)
