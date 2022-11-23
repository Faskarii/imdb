from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, HttpResponse
from .models import Movie
from .forms import MovieForm


def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        limit = int(request.GET.get('limit', 8))
        offset = int(request.GET.get('offset', 0))
        return render(request, 'movies/movie_list.html', context={'movies': movies})

    elif request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
        
        return movies_add(request, form)


def movies_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'GET':
        return render(request, 'movies/movie_detail.html')

    elif request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if not form.is_valid():
            return movie_edit(request, pk, movie_form=form)

        form.save()
        return redirect ('movie_detail', pk=pk) 

def movies_add(request, movie_form=None):
    if not movie_form:
        movie_form = MovieForm()
    return render(request, 'movies/movie_add.html', {'form':movie_form})


def movie_edit(request, pk, movie_form=None):
    movie = get_object_or_404(Movie, pk=pk)

    if not movie_form:
        form = MovieForm(instance=movie)

    context = {
        'form':form,
        'movie':movie
    }
    return render(request, 'movies/movie_edit.html', context=context)




def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk)
    movie.delete()
    return redirect(movies_list)
        