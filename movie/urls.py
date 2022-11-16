from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movies_list, name='movie_list'),
    path('movies/detail/<int:pk>', views.movie_detail, name='movie_detail')
]

