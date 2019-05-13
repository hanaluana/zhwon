from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.movie_list, name="list"), 
    path('<int:movie_id>/', views.movie_detail, name="detail"),
    
    path('<int:movie_id>/comment/create/<int:rating_id>/', views.rating, name='comment'),
]