from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.dentists import bp as dentists_bp
app.register_blueprint(dentists_bp, url_prefix='/dentists')

from app import models
