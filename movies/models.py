from django.db import models
# Create your models here
class Genere(models.Model):
    genere_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genere_name


class Movie(models.Model):
    movie_title = models.CharField(max_length=255)
    movie_description = models.TextField()
    release_date = models.DateTimeField(auto_now=True, null=True)
    genere = models.ManyToManyField(Genere, null=True, blank=True)
    casts = models.ManyToManyField('Cast', null=True, blank=True)

    def __str__(self):
        return self.movie_title


class Cast(models.Model):
    cast_name = models.CharField(max_length=255)
    cast_age = models.IntegerField()
    cast_awards = models.CharField(max_length=255)

    def __str__(self):
        return self.cast_name