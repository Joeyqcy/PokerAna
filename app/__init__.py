from flask import Flask
from app.model import db
from app.views import home_page
from app.views import theory, stats


def create_app(config):
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(stats, url_prefix='/stats')
    app.register_blueprint(theory, url_prefix='/theory')
    app.add_url_rule('/', 'home_page', home_page)

    return app
