from flask import Flask
from flask_bootstrap import Bootstrap

from .config import config_options

from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()


def create_app(config_name):

    # Intializing appliction
    app = Flask(__name__)

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)

    # Setting up configuration
    app.config.from_object(config_options[config_name])

    # app.config.from_pyfile('config.py')

    # intiating database
    db = SQLAlchemy()

    # Initializing db
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
