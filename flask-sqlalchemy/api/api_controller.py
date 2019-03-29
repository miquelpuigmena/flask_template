from api.blueprints.bp1 import bp1
from api.blueprints.bp2 import bp2


class APIController:

    def __init__(self, app):
        self.app = app

    def register_blueprints(self):
        self.app.register_blueprint(bp1, url_prefix="/bp1")
        self.app.register_blueprint(bp2, url_prefix="/bp2")
