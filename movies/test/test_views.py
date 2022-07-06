from . import TestSetUp
from rest_framework import status
from django.urls import reverse
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieTestViews(TestSetUp):

    def test_movies_list_views(self):

        url = reverse('movies:movie_list')
        print(url)
        resp = self.client.get(url)
        
        movie = Movie.objects.all()

        serializer = MovieSerializer(movie, many=True)

        print(serializer.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, serializer.data)