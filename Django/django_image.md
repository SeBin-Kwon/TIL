# 이미지 업로드

### 1. pillow 라이브러리 설치, 이미지 리사이징

> 이미지 관리하기 위해서 (Python Image Library)

`python3 -m pip install --upgrade Pillow`

`pip install django-imagekit`

### 2. 모델 ImageField 정의, urls 설정, settings 설정

```python
from pyexpat import model
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(
        upload_to='images/', 
        blank=True, 
        processors=[ResizeToFill(200,200)], 
        format='JPEG',
        options={'quality':80}
        )
```

- 이미지 리사이징
  - ProcessedImageField()의 parameter로 작성된 값들은 변경이 되더라도 다시 makemigrations를 해줄 필요없이 즉시 반영 됨

```python
 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```python
MEDIA_ROOT = BASE_DIR / 'media'
```

- Root 설정

### 3. views 설정

```python
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
  
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)
```

### 4. templates 설정

```django
<h1>write</h1>
<form method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {% bootstrap_form form %}
  <input class="btn btn-outline-primary" type="submit" value="Submit">
  <a class="btn btn-outline-secondary" href="{% url 'articles:index' %}">Back</a>
</form>
```

> `<form action="" method="POST" enctype="multipart/form-data">`

- `enctype` : 파일을 업로드해서 서버 전송하려면 필수 옵션!

<br>

## 기타

- django widget tweaks으로 폼 커스텀 가능하다

- install 하기

- `{{ form.username|add_class:"form-control" }}`