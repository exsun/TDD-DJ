from rest_framework.test import APITestCase
from ..models import Movie, Genre, Cast
from django.utils import timezone
from model_bakery import baker


class TestSetUp(APITestCase):
    def setUp(self):
        self.make_movie = baker.make('movies.Movie')
        self.make_genre = baker.make('movies.Genre', make_m2m=True)
        self.make_cast = baker.make('movies.Cast', make_m2m=True)
        # pprint(self.movie.__dict__)
        # pprint(self.genre.__dict__)
        # pprint(self.cast.__dict__)

        self.movie = Movie.objects.create(
                movie_title='Fast & Faurios 8',
                movie_description='Action Movie',
                release_date=timezone.now()
                )


        self.genre = Genre.objects.create(
                genre_name='Action'
                )


        self.cast = Cast.objects.create(
                cast_name='Rock',
                cast_age=50,
                cast_awards='Test Awards'
            )