from django.db import models
from django.conf import settings
# Create your models here


class Movie(models.Model):
    movie_title = models.CharField(max_length=255)
    movie_description = models.TextField()
    release_date = models.DateTimeField(auto_now=True)
    genres = models.ManyToManyField('Genre', related_name="genres")
    casts = models.ManyToManyField('Cast', related_name="casts")

    def __str__(self):
        return self.movie_title

class Review(models.Model):
    SCORE_RATE = [
         ('0', 0),
         ('1', 1),
         ('2', 2),
         ('3', 3),
         ('4', 4),
         ('5', 5),
         ('6', 6),
         ('7', 7),
         ('8', 8),
         ('9', 9),
         ('10', 10)
    ]

    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_score = models.CharField(choices=SCORE_RATE, max_length=2)
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review_text


class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class Cast(models.Model):
    cast_name = models.CharField(max_length=255)
    cast_age = models.IntegerField()
    cast_awards = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.cast_name