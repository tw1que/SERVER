from flask import Blueprint

bp = Blueprint('dentists', __name__)
from app.dentists import routes