from django.urls import path
from . import views


app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('occur/', views.occur, name='occur'),
    path('arrest/', views.arrest, name='arrest'),
]
