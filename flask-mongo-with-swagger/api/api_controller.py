import configparser
from flask_swagger_ui import get_swaggerui_blueprint
from api.blueprints.bp1 import bp1
from api.blueprints.bp2 import bp2



class APIController:

    def __init__(self, app):
        self.app = app
        self.CONFIG = configparser.RawConfigParser()
        self.CONFIG.read('config.cfg')
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
        self.app.register_blueprint(bp1, url_prefix="/bp1")
        self.app.register_blueprint(bp2, url_prefix="/bp2")
        self.app.register_blueprint(self.bp_swagger, url_prefix=self._SWAGGER_URL)
