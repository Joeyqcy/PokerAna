from flask import Flask
from app.model import db


def create_app(config):
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object(config)
    db.init_app(app)
    return app