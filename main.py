from app.app import build_app
from app import DevelopmentConfig, ProductionConfig

config = ProductionConfig()
app = build_app(config)
app.run(host=config.HOST,port=config.PORT)
