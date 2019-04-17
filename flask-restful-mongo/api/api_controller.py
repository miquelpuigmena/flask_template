import configparser
from flask import Blueprint
from flask_restful import Api
from api.routes.route1 import Route1
from api.routes.route2 import Route2


class APIController:

    def __init__(self, app):
        self.app = app
        config = configparser.RawConfigParser()
        config.read('config.cfg')
        self.bp_api = Blueprint("bp-"+__name__, __name__)
        self.api = Api(self.bp_api)

    def register_blueprint(self):
        self.app.register_blueprint(self.bp_api)

    def add_resources(self):
        self.api.add_resource(Route1, '/route1/<string:id>')
        self.api.add_resource(Route2, '/route2/<string:id>')
