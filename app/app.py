from flask import Flask
from app.hello_routes import hello_routes
from app.movies_routes import movies_routes
from . import DevelopmentConfig

def build_app():
    
    app = Flask(__name__)
    config = DevelopmentConfig()
    
    app.config['DEBUG'] = config.DEBUG
    app.config['ENV'] = config.ENV
    
    app.register_blueprint(hello_routes,url_prefix=config.URL_PREFIX)
    app.register_blueprint(movies_routes,url_prefix=config.URL_PREFIX)
    
    return app

