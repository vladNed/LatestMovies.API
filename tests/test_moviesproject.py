import os
import tempfile
import pytest
from main import app
from app import DevelopmentConfig
config = DevelopmentConfig()

@pytest.fixture
def client():
    
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client
        
def test_hello_positive(client):  
    response = client.get('/api/v1/hello')
    assert response.status_code == 200
    assert response.get_data() == b'Hello, World!'

def test_hello_negative(client):
    response = client.post('/api/v1/hello')
    assert response.status_code == 405   
    
def test_latest_movies_positive(client):
    response = client.get('/api/v1/movies/latest')
    assert response.status_code == 200
    assert len(response.json['data']) == 10

def test_latest_movies_negative(client):
    response = client.post('/api/v1/movies/latest')
    assert response.status_code == 405
    
def test_actors_movies(client):
    response = client.post('/api/v1/movies/actors-movies',json={
        'actors_list': ['brad pitt']
    })
    data = response.get_json()
    
    assert response.status_code == 200
    assert len(data['data']) == 1

def test_actors_movies_negative1(client):
    response = client.post('/api/v1/movies/actors-movies',json={
        'actors_list': ['vlad nedelcu']
    })
    data = response.get_json()
    
    assert response.status_code == 200
    assert data['data']['vlad nedelcu'] == "Could not find any matching ID for this actor"

def test_actors_movies_negative2(client):
    response = client.post('/api/v1/movies/actors-movies',json={
        'different_key': 'Test'
    })
    data = response.get_json()
    
    assert response.status_code == 400
    assert data['error'] == 'BAD REQUEST'