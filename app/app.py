from flask import Flask
from app.controllers.HelloWorldController import helloWorldController
from app.controllers.MoviesController import MoviesController
from . import DevelopmentConfig

def build_app():
    
    app = Flask(__name__)
    config = DevelopmentConfig()
    
    app.config['DEBUG'] = config.DEBUG
    app.config['ENV'] = config.ENV
    
    app.register_blueprint(helloWorldController,url_prefix=config.URL_PREFIX)
    app.register_blueprint(MoviesController,url_prefix=config.URL_PREFIX)
    
    return app

