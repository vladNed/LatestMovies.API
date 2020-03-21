from flask import Flask
from app import DevelopmentConfig, ProductionConfig
from app.hello_routes import hello_routes
from app.movies_routes import movies_routes

config = ProductionConfig()
app = Flask(__name__)
    
app.config['DEBUG'] = config.DEBUG
app.config['ENV'] = config.ENV
    
app.register_blueprint(hello_routes,url_prefix=config.URL_PREFIX)
app.register_blueprint(movies_routes,url_prefix=config.URL_PREFIX)

if __name__ == '__main__':
    app.run()
