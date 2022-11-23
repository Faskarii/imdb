from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_list, name='movie_list'),
    path('movies_detail/<int:pk>/', views.movies_detail, name='movie_detail'),
    path('movie_edit/<int:pk>/', views.movie_edit, name='movie_edit'),
    path('movies_add/', views.movies_add, name='movie_add'),
    path('movie_delete/', views.movie_delete, name='movie_delete'),

]

