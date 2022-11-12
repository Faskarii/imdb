from django.urls import path
from . import views

urlpatterns = [
    path('movies_list/', views.movies_list)
]

