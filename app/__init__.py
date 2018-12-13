from flask import Flask
from flask_bootstrap import Bootstrap


# Intializing appliction
app = Flask(__name__)

from app import views

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
