# <<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
# =======
from django.shortcuts import render, HttpResponse
# >>>>>>> 606b57c67d2d46cc0e0eefed91d33501079749a1
from .models import Movie


def movies_list(request):
# <<<<<<< HEAD
    limit = int(request.GET.get('limit', 8))
    offset = int(request.GET.get('offset', 0))
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', context={'movies': movies})


def movies_detail(request, pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=pk, is_valid=True)
        content = {'movie': movie}
        return render(request, 'movie_detail.html', context=content)
# =======
#     movies = Movie.objects.all()
#     return render(request, 'movie/movies_list.html', context={'movies': movies})


# def movie_detail(request, pk):
#     return HttpResponse(f'<h1>this is movie{pk}</h1>')
# >>>>>>> 606b57c67d2d46cc0e0eefed91d33501079749a1
