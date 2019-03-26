import configparser
from flask import Flask
from mongoengine import connect
from api.api_controller import APIController


from models.model1 import Model1, ModelReferenced1;


class Run:
    def __init__(self):
        self.CONFIG = configparser.RawConfigParser()
        self.CONFIG.read('config.cfg')

        # Get Config info
        self.HOST = self.CONFIG.get('flask', 'host')
        self.PORT = int(self.CONFIG.get('flask', 'port'))

        # DB
        connect('template_db')

        # API
        self.APP = Flask(__name__)
        self.APP.secret_key = self.CONFIG.get('flask', 'secret')
        self.APP.config['DEBUG'] = (self.CONFIG.get('flask', 'debug') == "True")
        APIController(self.APP).register_blueprints()

    def run_app(self):
        self.APP.run(host=self.HOST, port=self.PORT)


if __name__ == '__main__':
    Run().run_app()
