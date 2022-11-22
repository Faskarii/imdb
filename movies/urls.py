from django.urls import path
<<<<<<< HEAD
from .views import movies_list, movies_detail

urlpatterns = [
    path('movies_list/', movies_list, name='movie_list'),
    path('movies_detail/<int:pk>/', movies_detail, name='movie_detail'),
=======
from . import views

urlpatterns = [
    path('movies/', views.movies_list, name='movie_list'),
    path('movies/detail/<int:pk>', views.movie_detail, name='movie_detail')
>>>>>>> 606b57c67d2d46cc0e0eefed91d33501079749a1
]

