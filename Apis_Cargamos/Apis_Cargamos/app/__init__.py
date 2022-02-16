from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_object(Config)
db=SQLAlchemy(app)

from app import routes,models