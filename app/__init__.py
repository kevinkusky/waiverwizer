"""init.py"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# pylint: disable=wrong-import-position
from app.models import *
from app import routes
