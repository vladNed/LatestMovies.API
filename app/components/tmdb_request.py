import requests
from .. import DevelopmentConfig

config = DevelopmentConfig()

api_key = config.API_KEY
base_url = config.BASE_URL

def searchMovies(primary_year, latest_release_date):
    tmdb_response = requests.get(f"{base_url}/3/discover/movie?api_key={api_key}&primary_release_year={primary_year}&primary_release_date.lte={latest_release_date}")
    
    if tmdb_response.status_code != 200:
        return 503
    
    if tmdb_response.json()['total_results'] != 0:
        return tmdb_response.json()['results']
    else:
        return 404

def searchActor(actor_name):
    actor_id = requests.get(f'{base_url}/3/search/person?api_key={api_key}&query={actor_name.replace(" ","%20")}')
    
    if actor_id.status_code != 200:
        return 503

    if actor_id.json()['total_results'] != 0:
        return actor_id.json()['results'][0]
    else:
        return 404

def searchCastMovies(actor_id):
    
    actor_movies = requests.get(f"{base_url}/3/discover/movie?api_key={api_key}&language=en-US&with_cast={actor_id}")
    
    if actor_movies.status_code != 200:
        return "Error: Could not query database."
    
    if actor_movies.json()['total_results'] != 0:
        return actor_movies.json()['results']
    else:
        return -1