from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    # 모든 데이터 가져오기
    articles = Article.objects.all()
    # context에 담아서 넘기기
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form' : article_form
#     }
#     return render(request, 'articles/new.html', context=context)

def create(request):
    # POST 메서드 일 때, create 페이지에서 글쓰기 버튼을 누르면서 POST 요청 발생
    if request.method == 'POST':
        # 요청을 토대로 모델폼 생성
        article_form = ArticleForm(request.POST) 
        # 이게 유효하다면
        if article_form.is_valid():
            # 이 데이터를 저장하고 보내기
            article_form.save()
            return redirect('articles:index')
    # GET 메서드 일 때, index 페이지에서 작성 버튼 누르고 create 페이지로 넘어오면서 GET 요청 발생
    else:
        # 모델폼으로 폼 만들기
        article_form = ArticleForm()
    # 해당 폼을 넘기기
    # 모델 폼이 유효하지 않을 때 다시 리턴
    context = {
    'article_form' : article_form
    }
    return render(request, 'articles/create.html', context=context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')

def update(request, pk):
    # POST이면(수정한 후 제출한다면) 검증하기
    # 해당 pk값 가져오기
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # 기존 데이터를 수정하는 것이므로 instance로 가져옴
        article_form = ArticleForm(request.POST,instance=article)
        if article_form.is_valid():
            # 참이면 저장하고 detail 페이지로 보내기
            article_form.save()
            return redirect('articles:detail',article.pk)
        # 유효성 검사에서 거짓이라면 if문 탈출하여 context로 가서 폼 렌더
    else:
        # GET이면 기존 값을 가져와서 폼으로 넘기기
        article_form = ArticleForm(instance=article)
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/update.html', context)