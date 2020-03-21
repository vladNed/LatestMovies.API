# LatestMovies.API

This project is an API with 3 functional endpoints:
- Hello World
- Latest Movies
- Movies for a set of actors

## How to run ?
There are two main requirements for this project ro run:
- install python >= 3.6
- install flask 

> There is a `requirement.txt` file within the project but will not install `python` and `pip`

After installing python and pip you can go inside a `cmd` or `bash` and run the following commands inside the repo:

```console
$ pip install requirements.txt
$ python startup.py
```
## Endpoints

There are 3 endpoints for this API:
- GET `/api/v1/hello-world` will only display a message hello world 
- GET `/api/v1/movies/latest` will return a json with the latest movies from the current year
- POST `/api/v1/movies/actors-movies` requires a JSON body with a string list. For example:

```yaml
{
  "actors_list": ["adam driver","tom ford","vlad nedelcu"]
}
```

This will return a JSON with 10 movies for each actor sorted from the latest to the earliest.

## Configuration
There is a development config for now class inside the app's init:
```python
class DevelopmentConfig(object):
    
    def __init__(self):
        self.DEBUG = True
        self.API_KEY = os.environ.get('API_KEY')
        self.ENV = 'Development'
        self.URL_PREFIX = '/api/v1'
        self.BASE_URL = 'https://api.themoviedb.org'
        
```
