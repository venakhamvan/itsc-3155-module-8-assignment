from flask import Flask, redirect, render_template, request, abort
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)

rated_movies = {}

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    movie = request.form.get('movie_title')
    director = request.form.get('director')
    rating = request.form.get('rating')
    if not movie:
        abort(400)
    if not director:
        abort(400)
    rated_movies[movie] = [director, rating]
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
