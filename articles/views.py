from django.shortcuts import render, redirect
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
'''
def create(request):
    # new.html에서 form action="articles:create"에 의해
    # urls에서 create로 가서 create view함수로 옴
    # request 안에 요청된 데이터들이 들어있음
    title = request.GET.get('title')
    content = request.GET.get('content')
    # DB에 저장
    article = Article(title=title, content=content)
    article.save()
    return render(request, 'articles/create.html')
'''

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article(title=title, content=content)
    article.save()
    # url detail에 article.pk를 보냄
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 기존값(article.title)을 
    # 받아온 값(request.POST.get('title')로 바꿈)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)

