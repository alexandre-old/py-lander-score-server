from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'pylander')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(DB_PATH)
db = SQLAlchemy(app)

from . import views
