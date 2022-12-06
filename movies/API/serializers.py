from rest_framework import serializers
from movies.models import Genre, Role, Crew, MovieCrew, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie


class MovieCrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCrew
