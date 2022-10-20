from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments_forms = CommentForm()
    context = {
        'article' : article,
        'comments' : article.comment_set.all().order_by('-pk'),
        'comments_form' : comments_forms,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')

def comments(request, pk):
    article = Article.objects.get(pk=pk)
    comments_forms = CommentForm(request.POST)
    if comments_forms.is_valid():
        comment = comments_forms.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)

def comment_delete(request, pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()

    return redirect('articles:detail', pk)
    