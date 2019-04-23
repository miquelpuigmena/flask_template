import configparser
from flask import Blueprint
from flask_restful import Api
from flasgger import Swagger
from api.routes.route1 import Route1
from api.routes.route2 import Route2


class APIController:

    def __init__(self, app):
        self.app = app
        config = configparser.RawConfigParser()
        config.read('config.cfg')
        self.bp_api = Blueprint("bp-" + __name__, __name__)
        self.api = Api(self.bp_api)
        ### SWAGGER ###
        self.app.config['SWAGGER'] = {
            "swagger_version": "2.0",
            "title": "Flasgger",
            "specs": [
                {
                    "version": "0.0.1",
                    "title": "Flask-restful-mongo-with-Flasgger",
                    "endpoint": "flasgger",
                    "description": "Miquel's template",
                    "route": '/flasgger',
                }
            ]
        }
        self.swagger = Swagger(self.app)

    def register_blueprints(self):
        self.app.register_blueprint(self.bp_api)

    def add_resources(self):
        self.api.add_resource(Route1, '/route1', '/route1/<string:id>')
        self.api.add_resource(Route2, '/route2', '/route2/<string:id>')
