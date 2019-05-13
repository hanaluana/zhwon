from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Rating
# from .forms import MovieForm, RatingForm
from .models import Movie, Rating
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
