from django.shortcuts import render

# faltan las rutas 
# from .../.../... import movie_recommmendations.py

#from  movie.models import Movie

def recomendacion(request):
    return render(request, 'recommendations.html')
