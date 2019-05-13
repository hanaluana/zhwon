from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    user_Rating = models.FloatField(default=0)
    title = models.CharField(max_length=150, default='')
    genre = models.ManyToManyField(Genre, related_name = "movies", blank=True)
    director = models.CharField(max_length=200, default='')
    naver_link = models.TextField(default='')
    image =models.TextField(default='')
    
    def __str__(self):
        return self.title

class Rating(models.Model):
    comment = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.comment
