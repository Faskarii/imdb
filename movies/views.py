from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, HttpResponse
from .models import Movie
from .forms import MovieForm

def movies_list(request):
    limit = int(request.GET.get('limit', 8))
    offset = int(request.GET.get('offset', 0))
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', context={'movies': movies})


def movies_detail(request, pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=pk, is_valid=True)
        content = {'movie': movie}
        return render(request, 'movies/movie_detail.html', context=content)


def movies_add(request):
    if request.method == 'GET':
        form = MovieForm()
        return render(request, 'movies/movie_add.html', {'form':form})

    elif request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            release_date = form.cleaned_data.get('release_date')
            avatar = form.cleaned_data.get(avatar)
            Movie.objects.create(
                title = title,
                description = description,
                release_date = release_date,
                avatar = avatar
            )
            return redirect('movies/movie_list.html')
        return HttpResponse(str(form.errors))