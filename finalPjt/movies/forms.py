from django import forms
from .models import Movie, Rating

class MovieForm(forms.ModelForm):
    title = forms.CharField(label="영화 제목", widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    director = forms.CharField(label="감독", widget=forms.TextInput(attrs={'placeholder': 'Director'}))
    nation = forms.CharField(label="국가", widget=forms.TextInput(attrs={'placeholder': 'Nationality'}))
    openDate = forms.CharField(label="개봉일", widget=forms.TextInput(attrs={'placeholder': 'Released Date'}))
    watchGrade = forms.CharField(label="관람 등급", widget=forms.TextInput(attrs={'placeholder': 'Grade'}))
    duration = forms.CharField(label="상영 시간", widget=forms.TextInput(attrs={'placeholder': 'Duration'}))
    naver_link = forms.CharField(label="네이버 링크", widget=forms.TextInput(attrs={'placeholder': 'Naver Link'}))
    poster_image = forms.CharField(label="포스터", widget=forms.TextInput(attrs={'placeholder': 'Poster Link'}))
    summary = forms.CharField(label="줄거리", widget=forms.Textarea(attrs={'placeholder': 'Summary'}))
    audience = forms.CharField(label="누적관객수", widget=forms.TextInput(attrs={'placeholder': 'Audience Number'}))
    reservation = forms.CharField(label="예약", widget=forms.TextInput(attrs={'placeholder': 'Reservation Link'}))
    user_Rating = forms.CharField(label="네이버 평점", widget=forms.TextInput(attrs={'placeholder': 'Naver Rating'}))
    
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'director', 'nation','openDate','watchGrade',
        'duration','naver_link', 'poster_image', 'summary','audience','reservation','user_Rating']
        
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score','comment']
        