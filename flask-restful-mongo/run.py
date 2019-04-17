import configparser
from flask import Flask
from mongoengine import connect
from api.api_controller import APIController


class Run:
    def __init__(self):
        self.CONFIG = configparser.RawConfigParser()
        self.CONFIG.read('config.cfg')

        # Get Config info
        self.HOST = self.CONFIG.get('flask', 'host')
        self.PORT = int(self.CONFIG.get('flask', 'port'))

        # DB
        connect(
            self.CONFIG.get('db', 'name'),
            host=self.CONFIG.get('db', 'host'),
            port=self.CONFIG.getint('db', 'port')
        )

        # API
        self.APP = Flask(__name__)
        self.APP.secret_key = self.CONFIG.get('flask', 'secret')
        self.APP.config['DEBUG'] = self.CONFIG.getboolean('flask', 'debug')
        self.api = APIController(self.APP)
        self.api.add_resources()
        self.api.register_blueprint()

    def run_app(self):
        self.APP.run(host=self.HOST, port=self.PORT)


if __name__ == '__main__':
    Run().run_app()
