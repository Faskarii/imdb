from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from movies.models import Movie
from .serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



