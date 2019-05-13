from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Rating
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST']) #허용할 http method를 적어줌
def movie_list(request):
    pass
    # if request.method=="GET":
    #     movies = Movie.objects.all()
    #     form = RatingForm()
    #     return render(request, 'movies/list.html', {'form':form, 'movies':movies})
    # else:
    #     # CREATE
    #     music = request.data
    #     # Create an article from the above data
    #     serializer = MusicSerializer(data=music)
    #     if serializer.is_valid(raise_exception=True):
    #         music_saved = serializer.save()
    #     return Response(music_saved.data)
    
@api_view(['GET','PUT','DELETE'])
def movie_detail(request, movie_id):
    pass
    # if request.method=="GET":
    #     music = get_object_or_404(Music, id=music_id)
    #     serializer = MusicSerializer(music, many=False)
    #     return Response(serializer.data)
    # elif request.method=="PUT":
    #     saved_music = get_object_or_404(Music.objects.all(), pk=music_id)
    #     music = request.data
    #     serializer = MusicSerializer(instance=saved_music, data=music, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         music_saved = serializer.save()
    #     return Response(music_saved)
    # else:
    #     music = get_object_or_404(Music.objects.all(), pk=music_id)
    #     music.delete()
    #     return Response(status=204)
    
def rating(request, movie_id, rating_id):
    pass
