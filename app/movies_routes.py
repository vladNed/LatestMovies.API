from flask import Blueprint, jsonify, request
import requests
from datetime import datetime
from datetime import date
from app.components.tmdb_request import searchMovies, searchActor, searchCastMovies

movies_routes = Blueprint('movies_routes',__name__)


@movies_routes.route('/movies/latest',methods=['GET'])
def latest_movies():
      
    latest_movies = searchMovies(date.today().year,date.today().strftime('%Y-%m-%d')) 
    
    if latest_movies == 503:
        return jsonify({
            'error': 'Service Unavailable',
            'message': 'Could not query database'}), 503
    if latest_movies == 400:
        return jsonify({
            'error': 'NOT FOUND',
            'message': 'No results were found in the database'}), 50
     
    sorted_response = [(movie['title'],movie['release_date']) for movie in sorted(latest_movies,key=lambda x: datetime.strptime(x['release_date'],'%Y-%m-%d'),reverse=True)][:10]   
    return jsonify({'payload':'10 latest movies from current year',
                         'data': sorted_response})

@movies_routes.route('/movies/actors-movies',methods=['POST',])
def actors_latest_movies():
    
    if (request.json == None) or 'actors_list' not in request.json.keys() or len(request.json.keys())>1:
        return jsonify({
            'error': 'BAD REQUEST',
            'message': 'Invalid request body'}), 400    
    
    actors_names = request.json['actors_list']
    actors_movies = {}
    
    for actor_name in actors_names:
        actor_id = searchActor(actor_name)
        if actor_id == 503:
             return jsonify({
                'error': 'Service Unavailable',
                'message': 'Could not query database'}), 503
        if actor_id != 404:   
            actor_movies = searchCastMovies(actor_id['id'])
            actors_movies[actor_name] = [(movie['title'],movie['release_date']) for movie in sorted(actor_movies ,key=lambda x: datetime.strptime(x['release_date'],'%Y-%m-%d'),reverse=True)][:10]       
        else:
            actors_movies[actor_name] = "Could not find any matching ID for this actor"

    return jsonify({'data':actors_movies})