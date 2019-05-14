from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('cgv/<int:type_id>/<int:gender>/<int:age>/', views.cgv, name='cgv'),
    path('naver/<int:type_id>', views.naver, name="naver"),
    path('current/', views.current, name="current"),
]
