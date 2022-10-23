# A one-to-many relationship

## 1:N (Article - Comment) 

## 댓글 기능

> 댓글은 게시글 상세 페이지에 쓴다.

### 모델 관계 설정

```python
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = ProcessedImageField(
        upload_to='images/', 
        blank=True, 
        processors=[ResizeToFill(500,500)], 
        format='JPEG',
        options={'quality':80}
        )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

<br>

`article = Article.object.get()`

`comment = Comment.objects.create(content='111', article=article)`

`comment.article_id` => 13 (숫자)

`comment.article` => `<Article: Article object (13)>` (객체)

article 객체의 모든 댓글 가져오기

- `Comment.objects.filter(article_id = 13)` == `article.comment_set.all()`
- 모두 객체로 반환 `<QuerySet>`
  - 왜 쿼리셋이냐면 N개이기 때문

### forms 설정

```python
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content',]
```

### 댓글 출력할 때 views/templates

1. ```python
   def detail(requset, pk):
     article = Article.objects.get(pk=pk)
     comments_form = CommentForm()
     context = {
       'article' : article,
       'comments': article.comment_set.all(),
     }
     return redirect('articles:detail', article.pk)
   ```

   ```django
   {% for comment in comments %}
   <p>
     {{ comment.content}}
   </p>
   {% endfor %}
   ```

2. ```python
   def detail(requset, pk):
     article = Article.objects.get(pk=pk)
     context = {
       'article' : article
     }
     return redirect('articles:detail', article.pk)
   ```

   ```django
   {% for comment in article.commet_set.all %}
   <p>
     {{ comment.content}}
   </p>
   {% endfor %}
   ```

<br>

#### 댓글이 없을 때

```django
{% empty %}
  <p>
    댓글이 없어요.
</p>
```

<br>

<br>

### urls 설정 후 view

- 내가 넣어야할 값이 더 있기 때문에 바로 save 하지 않고 멈춘 다음에

  article 값(FK)을 같이 담아서 save한다.

- 모델폼의 `save` 메서드는 리턴 값이 그 모델의 인스턴스이다.
- 추가 값을 포함해야 할 때 `.save(commit=False)` (모델폼 인스턴스)를 해준다.
- 그 후 직접 `.save()`를 해준다. (모델 인스턴스)

```python
def comment_create(request, pk):
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm(request.POST)
  if comment_form.is_valid():
    comment = comment_form.save(commit=False)
    comment.article = article
    comment.save()
  return redirect('articles:detail', article.pk)
```

<br>

### 댓글 삭제

#### template

```django
  <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST"> 
    {% csrf_token %}
    {% if request.user == comment.user %}
      <input class="btn btn-outline-danger" type="submit" value="Delete">
      {% endif %}
  </form>
```

- a태그는 GET을, form태그는 POST로 보낸다.