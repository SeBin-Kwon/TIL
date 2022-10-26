# 사용자 - 글

> 모델 바꾸기 -> 모델 폼 -> 뷰(유저정보 저장) -> 유저 정보 출력 -> 템플릿

- 모델을 바꾸면서 새로운 행이 생김

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

사용자로부터(요청) 받을 수 있는 정보는?

- request(request.POST/request.GET)
  - Form
  - Form에서 값 입력해서 줘
- URL(variable routing)
  - 내가 깔아놓은 길(게시글 보기)

```python
@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            # 로그인한 유저가 => 작성자!
            article.user = request.user
            article.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
```

```django
{{ article.user}}
```

- 원래 article 테이블에는 user_id가 없었지만 새로 생김

- `.save()`가 db에 저장하는 건데 user_id가 없는채로 저장할 수 없음

  - `ArticleForm(request.POST, request.FILES)` 여기에는 user_id 값을 저장하는게 없기 때문
  - NUTNULL 때문

- `article = article_form.save(commit=False)`로 db에 저장하는걸 막고 변수에 담음

- `article.user = request.user` 

  article 테이블에 있는 user_id를 request.user로 채워줌

- `article.save()` db에 저장

<br>

### 작성자만 수정할 수 있게 하기

```django
{% if request.user == article.user %}
```

```python
def update()
article = Article.objects.get(pk=pk)
	if request.user == article.user:
    ...
  else:
    form django.http import HTTPResponseForbidden
   return HTTPResponseForbidden() 
		# 아니면
  massages.warning(request,'작성자만 수정할 수 있습니다.')
  return redirect('articles:detail', article.pk)
```

- HTTP response를 직접 보내준다. (403에러)

### 몇개 작성했는지?

```django
{{ user.article_set.count }}개를 작성하였습니다.
```

## 사용자 - 댓글

1. 댓글 모델에도 유저 포린키 복붙

2. view에도 복붙

```python
if comments_forms.is_valid():
        comment = comments_forms.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
```

```django
{% if request.user.is_authenticated %}
{{ comment.user.username }} {{ comment.content}}
{% endif %}
```

#### 내가 쓴 댓글 누르면 해당 페이지 가기

```django
{% url 'articles:detail' comment.article_id %}
```

- user가 작성한 글 중 첫번째 글의 댓글 중에 첫번째의 user
  - `user.article_set.all()[0]`
    - article로 이뤄진 QuerySet의 첫번째 인스턴스
  - `.comment_set.all()[0]`
    - 인스턴스의 댓글들로 이뤄진 QuerySet의 첫번째
  - `.user`
    - 그 첫번째 댓글의 유저

### 메시지 알람

#### 1. 세팅

```python
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
```

#### 2. 뷰

```python
from django.contrib import messages
messages.success(request, '글 작성이 완료되었습니다.')
messages.warning(request, '작성자만 수정할 수 있습니다.')
```

#### 3. 템플릿

```django
{% if messages %}
    {% for message in messages %}
      <div class="alert alert-{{ message.tags }}">
        {{ message }}
      </div>
    {% endfor %}
  {% endif %}
```

<br>

## 글 작성과 글 수정 templates를 합치려면

```django
{% if request.resolver_match.url_name == 'create' %}
<h1> 글쓰기 </h1>
{% else %}
<h1> 수정하기 </h1>
{% endif %}

<form action="" method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {% bootstrap_form article_form %}
  {% bootstrap_button button_type="submit" content="OK" %}
</form>
```

> {% if request.resolver_match.url_name == 'create' %}`

- `request.resolver_match` (요청 url 정보)

  그것에 대한 ` url_name`

- 그게 `create`와 같은지? (urls.py의 `name='create'`부분)
