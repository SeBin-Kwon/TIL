# App URL mapping

>  app의 view 함수가 많아지면서 사용하는 path() 또한 많아지고, app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음

- 하나의 프로젝트의 여러 앱이 존재한다면, 각각의 앱 안에 urls.py을 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁할 수 있음

- 각각의 app 폴더 안에 urls.py를 작성하고 다음과 같이 수정 진행

  ```python
  # articles/urls.py
  from django.urls import path from . import views
  urlpatterns = [
  path('index/', views.index), path('greeting/', views.greeting), path('dinner/', views.dinner), path('throw/', views.throw), path('catch/', views.catch), path('hello/<str:name>/', views.hello),
  ]
  ```

### Including other URLconfs

- urlpattern은 언제든지 다른 URLconf 모듈을 포함(include)할 수 있음

- **include되는 앱의 url.py에 urlpatterns가 작성되어 있지 않다면 에러가 발생**

  - pages 앱의 urlpatterns가 빈 리스트라도 작성되어 있어야 함

  ```python
  # firstpjt/urls.py
  from django.contrib import admin
  from django.urls import path, include
  urlpatterns = [
  path('admin/', admin.site.urls), path('articles/', include('articles.urls')), path('pages/', include('pages.urls')),
  ]
  ```

<br>

### include()

- 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 돕는 함수
- 함수 `include()`를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달

<br>

## Template namespace



- 장고는 templates 폴더를 하나로 인식
- 중복되는 html이 있다면 최근 html은 등록하지 않는다.
- templates 폴더 안에 앱 이름의 폴더를 또 만들어서 구분해준다.
- base.html은 expend를 위해 최상단 폴더에 위치하게끔 한다.
- base는 프로젝트 폴더에 templates 폴드를 만들거나 가장 최상단에 만든다.

---

```bach
python -m venv venv
. venv/bin/activate
pip install django==3.2.13
pip freeze > requirements.txt
django-admin startproject pt3
python manage.py startapp apppp
```

- 루트페이지 생성
- url 분리
  - import path, include
  - urls.py 생성
    - from . import views
    - urlatterns = [path("",views.index),]

- 앱폴더와 동일한 위치에 templates 폴더 > base.html
  - settings의 templates 객체 설정
    - BASE_DIR/'templates'
  - {% block content %}
  - {% endblock %}
- 쉘 진입
- Todo.objects.all()
  - 다 불러오기