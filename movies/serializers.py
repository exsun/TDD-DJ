from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie_title', 'movie_description', 'release_date']