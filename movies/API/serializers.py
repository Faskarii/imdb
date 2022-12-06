from rest_framework import serializers
from movies.models import Genre, Role, Crew, MovieCrew, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title', 'is_valid', 'created_time', 'modified_time')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'title', 'is_valid', 'created_time', 'modified_time')


class CrewSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()

    class Meta:
        model = Crew
        fields = ('id', 'first_name', 'last_name', 'birthday', 'gender',
                  'avatar', 'is_valid', 'created_time', 'modified_time')

    def get_gender(self, obj):
        return obj.get_gender_display


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date', 'avatar',
                  'genres', 'is_valid', 'created_time', 'modified_time')


class MovieCrewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    crew = CrewSerializer()
    role = RoleSerializer()

    class Meta:
        model = MovieCrew
        fields = ('id', 'movie', 'crew', 'role', 'created_time', 'modified_time')
