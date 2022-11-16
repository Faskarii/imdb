from django.urls import path
from .views import movies_list

urlpatterns = [
    path('movies_list/', movies_list, name='movie_list'),

]

