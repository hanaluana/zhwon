from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm, RatingForm
from .models import Movie, Rating
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model, update_session_auth_hash

from django.template.defaulttags import register

from django.db.models import Avg

## 영화
# 영화 생성 - superuser인 경우에만 가능하도록
def create(request):
    # superuser인가? 
    if request.user.is_superuser:
        if request.method == "POST":
            form = MovieForm(request, request.FILES)
            if form.is_valid():
                movie = form.save()
                # 성공하면 영화 상세 페이지로 간다.
                return render(request, 'movies/detail.html', movie)
            else:
                return render(request, 'error.html')

        else:
            form = MovieForm()
        return render(request, 'movies/create.html', {'form':form})
        
    else:
        return redirect('movies:list')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# 영화 리스트 - 현재 상영작
def list(request):
    originMovies = Movie.objects.all()
    movies= originMovies
    # 동무들 평점 
    avg_score = {}
    for movie in movies:
        sum = Rating.objects.filter(movie=movie).aggregate(Avg('score'))
        if sum['score__avg']:
            avg_score[movie.id] = sum['score__avg']  
        else:
            avg_score[movie.id] = 0
    
    # 영화 3개씩 나누기 - for carousel
    newMovie = []
    i = 1
    for movie in movies:
        if (movie.id) % 3 == 0:
            newMovie.append(movies[movie.id-3:movie.id])
    newMovie.append(movie)
    return render(request, 'movies/list.html', {'movies':movies, 'avg_score':avg_score, 'newMovie':newMovie})
        

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    ratings = Rating.objects.filter(movie=movie)
    check = True
    rated = ''
    
    for rating in ratings:
        if request.user == rating.user:
            check = False
            rated = rating
    rating_form = RatingForm()
    
    sum = Rating.objects.filter(movie=movie).aggregate(Avg('score'))
    if sum['score__avg']:
        avg_score = sum['score__avg']  
    else:
        avg_score = 0

    context = {
        'movie':movie,
        'rating_form': rating_form,
        'ratings': ratings,
        'check': check,
        'avg_score': avg_score,
        'rated': rated
    }
    
    return render(request, 'movies/detail.html', context )

def update(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if not request.user.is_superuser:
        return redirect('movies:list')
    
    if request.method == "POST": 
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = MovieForm(instance=movie)
        return render(request, 'movies/update.html', {'form':form})

@require_POST
def delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.user.is_superuser:
        movie.delete()
    return redirect('movies:list')

## 영화 평점 매기기 - 영화 상세정보 페이지에서 남김
@login_required
def create_rating(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = RatingForm(request.POST)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.user = request.user
        rating.movie = movie
        rating.save()
    # 다음에 다시 상세페이지로 보내기
    return redirect('movies:detail', movie.id)
    
@require_POST
def delete_rating(request, movie_id, rating_id):
    rating = Rating.objects.get(pk=rating_id)
    if rating.user == request.user:
        rating.delete()
    return redirect('movies:detail', movie_id)
    
@login_required
def update_rating(request, movie_id, rating_id):
    rating = Rating.objects.get(pk=rating_id)
    if rating.user == request.user:
        if request.method == "POST":
            form = RatingForm(request.POST, instance=rating)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie_id)
        else:
            form = RatingForm(instance=rating)
        return render(request, 'movies/update.html', {'form':form})
        
    else:
        return redirect('movies:list')

def current(request):
    return render(request, 'movies/current.html')

def recommend(request):
    return render(request, 'movies/recommend.html')

def show(request):
    movies = Movie.objects.all()
    newMovies = []
    cnt = 0
    print(movies)
    return render(request, 'movies/carousel.html')    
    
def start(request):
    return render(request, 'movies/start.html')
    
def error_404(request):
    data = {}
    return render(request,'error.html')

def error_500(request):
    data = {}
    return render(request,'404.html')