from django.urls import path, include
from . import views

app_name = "movies"

urlpatterns = [
    path('create/', views.create, name="create"),
    path('',views.list, name="list"),
    
    path('<int:movie_id>/', views.detail, name="detail"),
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    path('<int:movie_id>/update/', views.update, name='update'),
    
    path('<int:movie_id>/rating/create/', views.create_rating, name='create_rating'),
    path('<int:movie_id>/rating/<int:rating_id>/delete', views.delete_rating, name="delete_rating"),
    path('<int:movie_id>/rating/<int:rating_id>/update', views.update_rating, name="update_rating"),
    
]