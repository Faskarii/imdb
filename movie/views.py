from django.shortcuts import render, get_object_or_404
from .models import Movie


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies_list.html', context={'media': movies})

def movies_detail(request, pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=pk, is_valid=True)
