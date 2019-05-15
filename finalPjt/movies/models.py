from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    
    title = models.CharField(max_length=150, default='')
    genre = models.ManyToManyField(Genre, related_name = "movies", blank=True)
    director = models.CharField(max_length=200, default='') # 감독
    nation = models.CharField(max_length=200, default='') # 국가
    openDate = models.CharField(max_length=200, default='') # 개봉일
    watchGrade = models.CharField(max_length=200, default='') # 
    duration = models.CharField(max_length=200, default='')
    naver_link = models.CharField(max_length=300, default='')
    poster_image = models.CharField(max_length=300, default='')
    summary =models.TextField(default='')
    audience = models.CharField(max_length=200, default='')
    reservation = models.CharField(max_length=300, default='')
    user_Rating = models.FloatField(default=0)


class Rating(models.Model):
    comment = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.comment
        
class Image(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    url = models.CharField(max_length=300, default='')
