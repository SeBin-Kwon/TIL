# 회원가입 및 로그인

## 1. 가상환경 생성 및 실행

```bash
$ python -m venv venv
$ . venv/bin/activate
(venv)
```

### 1-1. Django / Bootstrap5 설치 및 기록

```bash
# upgrade pip
$ python -m pip install --upgrade pip

# install Django 
$ pip install django==3.2.13

# install Bootstrap5
$ pip install django-bootstrap5

# 내가 활용하고 있는 패키지들 기록지에 남기기
$ pip freeze > requirements.txt
```

### 1-2. Django 프로젝트 생성

```bash
# 현재 위치(.)에 pjt 라는 이름의 프로젝트를 생성
$ django-admin startproject pjt .

# 서버 실행되는지 확인
$ python manage.py runserver
```

#### 1-2-1. 시크릿키, .gitignore 설정

```
# .gitignore
venv/
secrets.json
```

```python
# settings.py
from pathlib import Path
import os, json
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")
```

```json
{
	"SECRET_KEY": ""
}
```

### 1-3. Django 프로젝트 설정 및 앱 생성,등록

> 앱, 부트스트랩 등록
>
> 언어, 시간 설정

```bash
$ python manage.py startapp app_name
```

#### 1-3-1. base.html 생성

- 최상단에 templates 폴더 생성, 그 안에 base.html 생성
- settings.py에 등록

#### 1-3-2. static 생성

- 최상단에 static 폴더 생성
- settings.py에 등록

```python
INSTALLED_APPS = [
    'accounts',
    'django_bootstrap5',
  ...
]

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC' 부분을 아래와 같이 변경

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

# 템플릿 등록
TEMPLATES = [
	'DIRS': [BASE_DIR/"templates"],
  ...
  
# 스테틱 등록
# 해당 코드 써주기
STATICFILES_DIRS = [
    BASE_DIR/'static',
]
```

## 2. 모델 정의

> 모델 이름 : User
>
> Django **AbstractUser** 모델 상속

- AbstractUser는 암호화 기능을 가지고 있음

### 1-2. AUTH_USER_MODEL 정의하기

```python
# settings.py
# 최하단에 아래와 같은 코드 추가
# accounts 앱에 있는 User 가 이제부터 사용할 사용자 정보라고 입력하는 것

# User Model
AUTH_USER_MODEL = 'accounts.User'
```

### 1-3. 내부에 있던 모델 상속 받아오기

```python
# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
```

### 1-4. DB에 반영

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

## 3. 폼 생성 및 설정

> 기본 auth.User로 되어있기 때문에 accounts.User로 바꿔줘야한다.

- 회원가입

  - Django 내장 회원가입 폼 UserCreationForm을 상속받아서 **CustomUserCreationForm** 생성

    해당 폼은 아래 필드만 출력

    - username
    - email
    - password1
    - password2

```python
# forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username','email','password1','password2']
```

## 4. urls 분리 및 앱 네임 

```python
# pj/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
```

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
]
```

## 5. CRUD 구현

> 회원가입과 로그인에 필요한 모든 URL

```python
# accounts/urls.py
urlpatterns = [
    path('', views.main, name='main'),
    path('accounts/', views.index, name='index'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/<int:pk>', views.detail, name='detail'),
    path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logout, name='logout'),
]
```

### 5-1. 회원가입 기능 

#### 5-1-1.view

```python
# views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)
```

#### 5-1-2. template

```django
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% load static %}
{% block content %}
<h1>signup</h1>
<form method="POST"> 
  {% csrf_token %}
  {% bootstrap_form form %}
  <input type="submit" value="완료">
</form>
{% endblock %}
```

### 5-2. 회원가입 조회 및 detail

#### 5-2-1. view

```python
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# 회원 목록
@login_required
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users' : users
    }
    return render(request, 'accounts/index.html', context)
  
# 회원 프로필
@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user' : user
    }
    return render(request, 'accounts/detail.html', context)
```

#### 5-2-1. template

- index.html

```django
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% load static %}
{% block content %}
<h1>index</h1>
{% for user in users %}
<p><a href="{% url 'accounts:detail' user.pk %}">{{ user.username }}</a></p>
{% endfor %}
<a href="{% url 'accounts:main' %}">뒤로</a>
<a href="{% url 'accounts:logout' %}">로그아웃</a>
{% endblock %}
```

- detail.html

```django
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% load static %}
{% block content %}
<h1>{{ user.username }}'s profile</h1>
<p>{{ user.username }}</p> 
<p>{{ user.email }}</p>
<a href="{% url 'accounts:index' %}">뒤로</a>
{% endblock %}
```

### 5-3. 로그인 기능 

#### 5-3-1. view

```python
# views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:main')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)
```

#### 5-3-2. template

- 로그인 페이지

```django
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% load static %}
{% block content %}
<h1>login</h1>
<form method="POST"> 
  {% csrf_token %}
  {% bootstrap_form form %}
  <input type="submit" value="완료">
</form>
{% endblock %}
```

- 메인 페이지

  > 로그인 상태에 따라 다른 화면 출력한다.

```django
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% load static %}
{% block content %}

{% if request.user.is_authenticated %}
  <h1 class="title">Hello, <a href="{% url 'accounts:detail' user.pk %}">{{ user }}!</a></h1>
  <a href="{% url 'accounts:index' %}">회원 목록</a>
  <a href="{% url 'accounts:logout' %}">로그아웃</a>
{% else %}
  <h1 class="title">Welcome!</h1>
  <a href="{% url 'accounts:signup' %}">회원 가입</a>
  <a href="{% url 'accounts:login' %}">로그인</a>
  <a href="{% url 'accounts:index' %}">뒤로</a>
{% endif %}
{% endblock %}
```

### 5-4. 로그아웃 기능

#### 5-4-1. view

```python
from django.contrib.auth import logout as auth_logout
def logout(request):
    auth_logout(request)
    return redirect('accounts:main')
```

