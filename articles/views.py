from django.shortcuts import render
from .models import Article
import random

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'name': 'Jane',
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    # throw.hml에서 
    # message == name
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)
    
    
def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')