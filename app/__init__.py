from flask import Flask
from flask_bootstrap import Bootstrap

from .config import DevConfig


# Intializing appliction
app = Flask(__name__)


# Initializing Flask Extensions
bootstrap = Bootstrap(app)

# Setting up configuration
app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

from app import views
