# Django Practice 4

1. 가상환경 생성, 장고 설치, 프로젝트 생성
2. 앱 생성 및 등록
3. urls.py 설정
   1. `include`를 사용하여 url 분리하기
   2. 앱 `articles`에 urls.py 설정하기
   3. `app_name` 지정
   4. path 설정하기

4. model 정의

   1. 클래스 정의
   2. `makemigrations`, `migrate` 로 DB에 반영하기

5. 최상위 templates에 base.html 만들기

   1. 경로 지정하기

6. CRUD 기능 구현

   1. `forms.py` 생성

      ```python
      from django import forms
      from .models import Article
      
      class ArticleForm(forms.ModelForm):
      
          class Meta:
              model = Article
              # 해당 데이터만 가져오기
              fields = ['title','content']
              # 폼 모델에 부트스트랩 적용하기
              widgets = {
                  'title' : forms.TextInput(attrs={'class': 'form-control'}),
                  'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
              }
      ```

   2. urls => views => templates 순

   3. index 게시글 목록보기

      1. `articles = Article.objects.all()`

   4. create 게시글 작성하기

      1. request의 method에 따라(`GET`,`POST`) 조건문으로 나누기

         1. 모델  폼 받기

      2. 유효성 검사하기

         `if article_form.is_valid():`

   5. detail 게시글 상세보기

      1. templates에서 해당 링크로 pk 넘기기
      2. `article = Article.objects.get(pk=pk)`

   6. delete 게시글 삭제하기

      1. `article = Article.objects.get(pk=pk).delete`

   7. update 게시글 수정하기

      1. 해당 글의 pk 가져오기

         `article = Article.objects.get(pk=pk)`

      2. 기존 데이터를 모델 폼의 `instance`로 가져온다.

         `article_form = ArticleForm(request.POST,instance=article)`

         