from django import forms
from .models import Movie, Rating

# Post라는 모델을 조작할 수 있는 PostForm 정의

class RatingForm(forms.ModelForm):
    comment = forms.CharField(label="", widget = forms.TextInput(attrs={'class': 'form-control', 'style': "width:90%", 'placeholder': '영화평'}))
    score = forms.IntegerField(label='')
    
    class Meta:
        model = Rating
        fields = ['comment','score']