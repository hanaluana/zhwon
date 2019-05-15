from django import forms
from .models import Movie, Rating

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'director', 'nation','openDate','watchGrade',
        'duration','naver_link', 'poster_image', 'summary','audience','reservation','user_Rating']
        
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['comment', 'score']
        