from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments_forms = CommentForm()
    context = {
        'article' : article,
        'comments' : article.comment_set.all().order_by('-pk'),
        'comments_form' : comments_forms,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')
    else:
        messages.warning(request, '작성자만 삭제할 수 있습니다.')
        return redirect('articles:detail', article.pk)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 글 생성자만 수정,삭제 가능하게 하기
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form' : form
        }
        return render(request, 'articles/form.html', context)
    else:
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)

@login_required
def comments(request, pk):
    article = Article.objects.get(pk=pk)
    comments_forms = CommentForm(request.POST)
    if comments_forms.is_valid():
        comment = comments_forms.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)

@login_required
def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        return redirect('articles:detail', pk)
    else:
        messages.warning(request, '작성자만 삭제할 수 있습니다.')
        return redirect('articles:detail', comment.article.pk)    

# @login_required
# def comment_update(request, pk, comment_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     if request.user == comment.user:
#         if request.method == 'POST':
#             comments_forms = CommentForm(request.POST, instance=comment)
#             if comments_forms.is_valid():
#                 comment.save()
#                 return redirect('articles:detail', pk)
#         else:
#             comments_forms = CommentForm(instance=comment)
#         context = {
#             comments_forms
#         }
#         return redirect('articles:detail', context, pk)
#     else:
#         messages.warning(request, '작성자만 수정할 수 있습니다.')
#         return redirect('articles:detail', pk)   