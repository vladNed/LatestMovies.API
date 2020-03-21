import os

class DevelopmentConfig(object):
    
    def __init__(self):
        self.DEBUG = True
        self.API_KEY = os.environ.get('API_KEY')
        self.ENV = 'Development'
        self.URL_PREFIX = '/api/v1'
        self.BASE_URL = 'https://api.themoviedb.org'
        