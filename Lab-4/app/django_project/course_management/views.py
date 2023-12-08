from django.shortcuts import render
from .models import Course, Student
import requests

def index(request):
    # Obtener la lista de cursos (suponiendo que tengas un modelo 'Course')
    courses = Course.objects.all()

    # Renderizar la plantilla con los cursos
    return render(request, 'index.html', {'courses': courses})

def get_now_playing_movies(request):
    # URL de la API de TheMovieDB
    url = "https://api.themoviedb.org/3/movie/now_playing"

    # Parámetros de la solicitud, incluyendo la clave de la API
    params = {
        "api_key": "6a06f7f8888c8d73b42b2a9a99b2a8d5"  # Reemplaza con tu propia API Key
    }

    try:
        # Realizar la solicitud GET a la API
        response = requests.get(url, params=params)

        # Verificar si la solicitud fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            # Parsear la respuesta JSON
            data = response.json()
            movies = data['results']
            return render(request, 'get_now_playing_movies.html', {'movies': movies})
        else:
            # Manejo de errores si la solicitud no fue exitosa
            return render(request, 'error.html', {'error_message': 'No se pudo obtener la información de las películas'})
    except Exception as e:
        # Manejo de excepciones
        return render(request, 'error.html', {'error_message': str(e)})
