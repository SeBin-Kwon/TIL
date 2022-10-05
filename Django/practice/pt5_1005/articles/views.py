from django.shortcuts import render, redirect
from articles.models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    # post 라면
    if request.method == 'POST':
        # post로 보낸 데이터로 모델 폼 만들기
        form = ArticleForm(request.POST)
        # 모델 폼이 유효하다면
        if form.is_valid():
            # db에 저장해주기
            form.save()
            # article = Article.objects.get(pk=form.pk)
            # 목록 페이지로 가기
            return redirect('articles:index')
    # get이라면
    else:
        # 새로운 모델 폼 만들기
        form = ArticleForm()
    # 유효하지 않을 경우 그냥 만들어둔 폼 그대로 create페이지 다시 보여주기
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

def detail(request,pk):
    # pk를 이용해 해당 데이터 가져오기
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request,pk):
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')

def update(request,pk):
    # pk를 이용해 해당 데이터 가져오기
    article = Article.objects.get(pk=pk)
    # 기존 데이터와 함께 모델폼 생성
    # post일 때
    if request.method == 'POST':
        # 새로 작성된 것과 기존의 것을 함께 모델 폼 생성
        form = ArticleForm(request.POST,instance=article)
        # 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    # get일 때
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form
    }
    return render(request, 'articles/update.html', context)