from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    articles = Movie.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    # post 라면
    if request.method == 'POST':
        # 폼에 넣어서
        form = MovieForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # 저장하고
            form.save()
            # index로 리다이렉트
            return redirect('articles:index')
    # get 이라면
    else:
        # 폼 만들어서
        form = MovieForm()
    context = {
        'form' : form
    }
    # create 렌더
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Movie.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    Movie.objects.get(pk=pk).delete()
    return redirect('articles:index')

def update(request, pk):
    article = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = MovieForm(instance=article)
    context = {
        'form' : form
    }
    return render(request, 'articles/update.html', context)