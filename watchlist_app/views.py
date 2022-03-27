from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# Complex QuerySet -> Python Dictionary -> JsonReponse
def movie_list(request):
    movies = Movie.objects.all() # QuerySet
    data = {
      'movies' : list(movies.values())  # Convert to PythonDict
    }
    
    return JsonResponse(data)
