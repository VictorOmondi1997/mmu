
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()

def create_app(config_state):
    app = Flask(__name__)
    app.config.from_object(config_options[config_state])


    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
