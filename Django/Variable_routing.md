# Variable routing

### Variable routing의 필요성

> 템플릿의 많은 부분이 중복되고, 일부분만 변경되는 상황에서 비슷한 URL과 템플릿을 계속해서 만들어야 할까?

- URL 주소를 **변수**로 사용하는 것을 의미
- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

<br>

### Variable routing 작성

- 변수는 `<>`에 정의하며 view 함수의 인자로 할당됨
- 기본 타입은 string이며 5가지 타입으로 명시할 수 있음

1. str

   - `/`를제외하고비어있지않은모든문자열

   - 작성하지않을경우기본값

2. int
    • 0또는양의정수와매치

3. slug

4. uuid

5. path

```python
# urls.py
urlpatterns = [ ...,
    # path('hello/<str:name>/', views.hello),
    path('hello/<name>/', views.hello),
]
```

<br>

### View 함수 작성

- variable routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용할 수 있음

  ```python
  # articles/views.py
  def hello(request, name): 
    context = {
      'name': name, 
    }
    return render(request, 'hello.html', context)
  ```

  ```django
  <!-- articles/templates/hello.html -->
  {% extends 'base.html' %}
  {% block content %}
  <h1>만나서 반가워요 {{ name }}님!</h1>
  {% endblock %}
  ```

<br>

## Template inheritance

### 템플릿 상속

> 만약 모든 템플릿에 부트스트랩을 적용하려면 어떻게 해야 할까? 모든 템플릿에 부트스트랩 CDN을 작성해야 할까?

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤
- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 ‘skeleton’ 템플릿을 만들 수 있음

<br>

### 템플릿 상속에 관련된 태그

```django
{% extends '' %}
```

- 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
- **반드시 템플릿 최상단에 작성 되어야 함 (즉, 2개 이상 사용할 수 없음)**

```django
{% block content %}{% endblock content %}
```

- 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의
- 즉, 하위 템플릿이 채울 수 있는 공간
- 가독성을 높이기 위해 선택적으로 endblock 태그에 이름을 지정할 수 있음

<br>

### 추가 템플릿 경로 추가하기

> base.html의 위치를 앱 안의 template 디렉토리가 아닌 프로젝트 최상단의 templates 디렉토리 안에 위치하고 싶다면 어떻게 해야 할까?

- 기본 template 경로가 아닌 다른 경로를 추가하기위해 다음과 같은 코드를 작성

  ```python
  # settings.py
  TEMPLATES = [
      {
        ...
        'DIRS': [BASE_DIR / 'templates',],
        ...
  ```

<br>

### [참고] BASE_DIR

```python
# settings.py
BASE_DIR = Path(__file__).resolve().parent.parent
```

- settings.py에서 특정 경로를 절대 경로로 편하게 작성할 수 있도록 Django에서 미리 지정해둔 경로 값

- “객체 지향 파일 시스템 경로”

  - 운영체제별로 파일 경로 표기법이 다르기 때문에 어떤 운영체제에서

    실행되더라도 각 운영체제 표기법에 맞게 해석될 수 있도록 하기 위해 사용

- [공식문서](https://docs.python.org/ko/3.9/library/pathlib.html#module-pathlib)

<br>

## Sending and Retrieving form data

<br>

### 기타

- GET은 딕셔너리이기 때문에 `request.GET[""]` 이렇게 해도 된다.

```bash
python -m pip install --upgrade pip
```

- pip 업그레이드

