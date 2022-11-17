from django.shortcuts import render, HttpResponse
from .models import Movie


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movies_list.html', context={'movies': movies})


def movie_detail(request, pk):
    return HttpResponse(f'<h1>this is movie{pk}</h1>')