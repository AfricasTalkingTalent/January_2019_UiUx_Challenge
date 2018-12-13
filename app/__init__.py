from flask import Flask
from flask_bootstrap import Bootstrap

from .config import config_options

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()

# intiating database
db = SQLAlchemy()


def create_app(config_name):

    # Intializing appliction
    app = Flask(__name__)

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Setting up configuration
    app.config.from_object(config_options[config_name])

    # app.config.from_pyfile('config.py')

    # Initializing db
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
