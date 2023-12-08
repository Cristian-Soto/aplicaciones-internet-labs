from django.shortcuts import render
from .models import Course, Student
import requests

def index(request):
    # Obtener la lista de cursos (suponiendo que tengas un modelo 'Course')
    courses = Course.objects.all()

    # Renderizar la plantilla con los cursos
    return render(request, 'index.html', {'courses': courses})

def get_now_playing_movies(request):
    # Configurar la solicitud a la API de TheMovieDB
    api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2YTA2ZjdmODg4OGM4ZDczYjQyYjJhOWE5OWIyYThkNSIsInN1YiI6IjY1NjY1M2IzZDk1NDIwMDBjNDFmNTZlNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LEJGUFOtTFrs2CdDhB0Sv9uKvQQ-WEKl0k1xoulpxVk'
    url = 'https://api.themoviedb.org/3/movie/now_playing'
    params = {'api_key': api_key}
    
    # Realizar la solicitud
    response = requests.get(url, params=params)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener la lista de películas
        data = response.json()
        movies = data.get('results', [])
    else:
        # Manejar el caso en que la solicitud no sea exitosa
        movies = []

    # Renderizar la plantilla con las películas
    return render(request, 'now_playing_movies.html', {'movies': movies})
