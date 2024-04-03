from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('<int:num>/', views.detail, name='detail'),
    path('hello/<str:name>/', views.greeting, name='greeting'),
    path('new/', views.new, name='new'),
]
