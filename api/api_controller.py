import configparser
from api.blueprints.bp1 import bp1
from api.blueprints.bp2 import bp2

class APIController:

    def __init__(self, app):
        self.APP = app
        self.CONFIG = configparser.RawConfigParser()
        self.CONFIG.read('config.cfg')

    def register_blueprints(self):
        self.APP.register_blueprint(bp1, url_prefix="/bp1")
        self.APP.register_blueprint(bp2, url_prefix="/bp2")
