from flask import Flask

from .routes import index_blueprient

app = Flask(__name__)


def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(index_blueprient,url_prefix='/api')
    return app
