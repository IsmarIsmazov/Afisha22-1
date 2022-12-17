from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)
    id = models.ForeignKey


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='reviews')

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', default=1)
