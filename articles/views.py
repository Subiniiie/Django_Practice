from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
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
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


'''
def new(request):
    return render(request, 'articles/new.html')


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

    
# ModelForm class 사용
def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)

def create(request):
    form = ArticleForm(request.POST)
    # 유효성 검사 / 데이터가 유효한가?
    if form.is_valid():
        article = form.save()
        # url detail에 article.pk를 보냄    
        return redirect('articles:detail', article.pk)
    # 유효하지 않다면(빈 값이 있으면)
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
'''


def create(request):
    # 만약 데이터가 요청되었다면(들어왔다면)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        # 만약 데이터가 유효하다면
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else :
        # 데이터가 없음 / 인스턴스만 생성
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


'''
def edit(request, pk):
    # 어느 게시물을 살펴볼 것인가
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    # 게시물을 수정하는 거니까 무조건 유효할거임
    # 어떤 게시물을 수정할건지 알아야 하니까
    # article도 보냄
    # edit.html에서 article.pk 사용
    context = {
        'article': article,
        'form': form,
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

# ModelForm 클래스 사용
def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_vaild:
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/detail.html', context)
'''


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else :
        form = ArticleForm()
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)