from django.shortcuts import render
from .forms import GenreForm
import requests

def get_genres():
    url = "http://api.filmon.com/api/vod/genres"
    response = requests.get(url)
    
    try:
        genres = [(genre['id'], genre['name']) for genre in response.json()]
    except (KeyError, TypeError):
        genres = []
    
    return genres

def get_movies_by_genre(genre_id):
    url = f"http://api.filmon.com/api/vod/search?genre={genre_id}"
    response = requests.get(url)

    try:
        movies = response.json()['movies']
    except (KeyError, TypeError):
        movies = []

    print(f"API Response: {response.text}")  # Agrega esta línea para imprimir la respuesta

    return movies


def index(request):
    genres = get_genres()
    form = GenreForm()
    form.fields['genres'].choices = genres

    selected_genre = request.POST.get('genres', None)

    movies = []
    if selected_genre:
        movies = get_movies_by_genre(selected_genre)

    return render(request, 'index.html', {'form': form, 'movies': movies})

