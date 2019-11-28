from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config_options

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)

    bootstrap.init_app(app)

    return app
    
