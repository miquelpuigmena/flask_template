import configparser
from flask import Blueprint
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from api.routes.route1 import Route1
from api.routes.route2 import Route2


class APIController:

    def __init__(self, app):
        self.app = app
        config = configparser.RawConfigParser()
        config.read('config.cfg')
        self.bp_api = Blueprint("bp-"+__name__, __name__)
        self.api = Api(self.bp_api)
        ### SWAGGER ###
        self._SWAGGER_URL = '/swagger'
        self._API_URL = '/static/swagger.yaml'
        self.bp_swagger = get_swaggerui_blueprint(
            self._SWAGGER_URL,
            self._API_URL,
            config={
                'app_name': "flask-restful-mongo-with-Swagger"
            }
        )

    def register_blueprints(self):
        self.app.register_blueprint(self.bp_swagger, url_prefix=self._SWAGGER_URL)
        self.app.register_blueprint(self.bp_api)

    def add_resources(self):
        self.api.add_resource(Route1, '/route1', '/route1/<string:id>')
        self.api.add_resource(Route2, '/route2', '/route2/<string:id>')
