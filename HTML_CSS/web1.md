# 😄 Happy Web

## 웹 사이트의 구성 요소

- **HTML** : 구조
- **CSS** : 표현
- **Javascript** : 동작

<br>

### 웹 사이트와 브라우저

- 웹 사이트는 브라우저를 통해 동작함
- 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음 (파편화)
- 해결책으로 웹표준이 등장

<br>

### 웹 표준

> [W3C](https://www.w3.org/), [WHATWG HTML Living Standard](https://html.spec.whatwg.org/multipage/)

- 웹에서 표준적으로 사용되는 기술이나 규칙
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함 (크로스 브라우징)

### Can I use?

> [브라우저별 호환성 체크](https://caniuse.com/)

<br>

## 개발 환경 설정

### Visual Studio Code

- HTML/CSS 코드 작성을 위한 Visual Studio Code 추천 확장 프로그램
  - Open in browser
  - Auto Rename Tag
  - Auto Close Tag
  - Intellisense for CSS class names in HTML
  - HTML CSS Support

### 크롬 개발자 도구

- 웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공
  - 주요기능
    - Elements–DOM탐색및CSS확인및변경
      - Styles – 요소에 적용된 CSS 확인
      - Computed – 스타일이 계산된 최종 결과
      - Event Listeners – 해당 요소에 적용된 이벤트 (JS)
    - Sources, Network, Performance, Application, Security, Audits 등

<br>

## HTML 기초

> Hyper Text Markup Language
>
> **웹 페이지를 작성(구조화)하기 위한 언어**

**Hyper Text**

- 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

**Markup Language**

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
  - HTML, Markdown

<br>

## HTML 기본 구조

```html
<!DOCTYPE html> 
<html lang="en"> 
<head>
  <meta charset="UTF-8">
  <title>Document</title> 
</head>
<body>
</body>
</html>
```

- `html` :  문서의 최상위(root) 요소
  - `html` 요소의 `lang`특성에 유효한 IETF 언어 식별 태그를 지정하면 스크린 리더가 음성 표현에 사용할 언어를 선택할 때 도움이 된다.

- `head` :  문서 **메타데이터** 요소 (데이터를 위한 데이터)
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등 일반적으로 브라우저에 나타나지 않는 내용
- `body` : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

<br>

### head 예시

```html
<head>
  <title>HTML 수업</title>
  <meta charset="UTF-8">
  <link href="style.css" rel="stylesheet">   
  <script src="javascript.js"></script>  
  <style>
    p{
      color: black;
    }
  </style>
</head>
```

- `<title>` : 브라우저 상단 타이틀
- `<meta>` : 문서 레벨 메타데이터 요소
- `<link>` : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
- `<script>` : 스크립트 요소 (JavaScript 파일/코드)
- `<style>` : CSS 직접 작성

#### Open Graph Protocol

>메타 데이터를 표현하는 새로운 규약

- HTML 문서의 메타 데이터를 통해 문서의 정보를 전달

- 메타 정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의

<br>

### 요소(element)

> HTML의 요소는 태그와 내용(contents)로 구성되어 있다.

- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 내용이 없는 태그들도 존재 (닫는 태그가 없음)
    - br, hr, img, input, link, meta
- 요소는 중첩(nested)될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야 함
    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음

<br>

### HTML with 개발자 도구

- elements : 해당 요소의 HTML 태그
  - 마우스 포인터 모양 버튼 : 원하는 요소를 선택할 수 있음 (복잡한 형태의 경우 Elements에서 HTML 구조를 추가 탐색)

![스크린샷 2022-08-29 오후 2.08.13](web.assets/스크린샷 2022-08-29 오후 2.08.13.png)

<br>

### 속성(attribute)

> 태그별로 사용할 수 있는 속성은 다르다.

- 속성(attribute) 작성 방식 통일하기
  - 공백은 꼭 없애기
  - `""` 쌍따옴표 사용하기
- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음

#### HTML Global Attribute

> 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성 (몇몇 요소에는 아무 효과가 없을 수 있음)

- **`id`** : 문서 전체에서 유일한 고유 식별자 지정
- **`class`** : 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근)
- `data-*` : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
- **`style`** : inline 스타일
- `title` : 요소에 대한 추가 정보 지정
- `tabindex` : 요소의 탭 순서

<br>

### HTML 코드 예시

```html
<!DOCTYPE html> 
<html lang="en"> 
<head>
  <meta charset="UTF-8">
  <title>Document</title> 
</head>
<body>
  <!-- 이것은 주석입니다. -->
  <h1>나의 첫번째 HTML</h1>
  <p>이것은 본문입니다.</p>
  <span>이것은 인라인요소</span>
  <a href="https://www.naver.com">네이버로 이동!!</a>
</body>
</html>
```

<br>

### 렌더링(Rendering)

> 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정

<br>

### DOM(Document Object Model) 트리

> 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조

- HTML 문서에 대한 모델을 구성함
- HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함

<br>

### 인라인 / 블록 요소

> HTML 요소는 크게 인라인 / 블록 요소로 나눔

- 인라인 요소는 글자처럼 취급

- 블록 요소는 한 줄 모두 사용

<br>

### 텍스트 요소

```html
<!-- a태그(anchor) -->
<a href="https://google.com">구글</a>
<b>굵은 글</b>
<strong>중요한 굵은 글씨</strong>
&nbsp; 띄어쓰기
<i>이탤릭</i>
<em>중요한 기울임 글씨</em>
<br> 개행
<!-- 이미지 태그 -->
<img src="https://item.kakaocdn.net/do/9d4a4d8368feb0ea31d42724f36156f5f604e7b0e6900f9ac53a43965300eb9a" alt="보노보노">
<span>의미 없는 인라인 컨테이너</span>
```

-  `<img>` 요소

  - `src` 특성은 **필수**이며, 포함하고자 하는 이미지로의 경로를 지정 (절대 경로 혹은 상대 경로)

  - `alt` 특성은 이미지의 텍스트 설명이다. 필수는 아니지만, 스크린 리더가 `alt`의 값을 읽어 사용자에게 이미지를 설명하므로, 접근성 차원에서 **매우 유용**하다.

     또한 네트워크 오류, 콘텐츠 차단, 죽은 링크 등 이미지를 표시할 수 없는 경우에도 이 속성의 값을 대신 보여준다.

### 그룹 컨텐츠

```html
<p>하나의 문단 (paragraph)</p> 
<hr> 수평선 (문단 레벨 요소에서의 주제의 분리를 의미)
<ol>
  <li>순서가 있는 리스트</li>
  <li>(ordered)</li>
</ol>

<ul>
  <li>순서가 없는 리스트</li>
  <li>(unordered)</li>
</ul>  

<pre>HTML에 작성한 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백문자를 유지</pre>

<blockquote> 텍스트가 긴 인용문, 주로 들여쓰기를 한 것으로 표현됨</blockquote> 
<div>의미 없는 블록 레벨 컨테이너</div> 
```

[자주 사용하는 태그 순위](https://www.advancedwebranking.com/seo/html-study/)

[HTML 요소 참고서](https://developer.mozilla.org/ko/docs/Web/HTML/Element)

`<form>`

- 사용자로부터 입력을 받을 수 있는 HTLM 입력 폼(form)을 정의함.

`<input>`

- 사용자로부터 입력을 받을 수 있는 입력 필드(input filed)를 정의함.

`<script>`

- 자바스크립트와 같은 클라이언트 사이드 스크립트(client-side scripts)를 정의함.

`<link>`

- 해당 문서와 외부 소스(external resource) 사이의 관계를 정의함.

`<map>`

- 클라이언트 사이드 이미지맵(client-side image-map)을 정의함.
- `<area>`요소와 함께 이미지 맵(클릭 가능한 링크 영역)을 정의할 때 사용함

`<area>`

- 이미지 맵(image-map)에서 하이퍼링크가 연결될 영역을 정의함.

- `<map>`요소 안에서만 사용할 수 있다.

  ```html
  <map name="primary">
    <area shape="circle" coords="200,250,25" href="another.htm" />
    <area shape="default" nohref />
  </map>
  <img usemap="#primary" src="http://placehold.it/350x150" alt="350 x 150 pic">
  ```

---

<br>

## CSS 기초

> **Cascading(위에서 아래로 흐르는)** Style Sheets
>
> 스타일을 지정하기 위한 언어

### CSS 구문

```html
h1(선택자(Selector)) {
  color: blue;(선언(Declaration))
  font-size(속성(Property)): 15px(값(Value));
}
```

- CSS 구문은 선택자를 통해 스타일을 지정할 **HTML 요소를 선택**

- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 (Property) : 어떤 스타일 기능을 변경할지 결정
  - 값 (Value) : 어떻게 스타일 기능을 변경할지 결정

<br>

### CSS 정의 방법 1 : 인라인 - ❌

```html
<body>
   <h1 style="color: blue; font-size: 100px;">Hello</h1>
</body>
```

- 해당 태그에 직접 `style 속성`을 활용
- **가독성이 낮고 유지보수가 용이하지 않기 때문에 쓰지 않는다.**

### CSS 정의 방법 2 : 내부 참조

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
  <title>Document</title>
  <style> 
    h1 {
      color: blue;
      font-size: 100px; 
    }
  </style>
</head>
```

- `<head>` 태그 내에 `<style>`에 지정

### CSS 정의 방법 3 : 외부 참조 - ✅

> 주로 써야할 방법

```html
<head>
    <link rel="stylesheet"href="/examples/media/expand_style.css">
</head>
```

```css
body { background-color: lightyellow; }
p { color: red; text-decoration: underline; }
```

- 외부 CSS 파일을 `<head>`내 `<link>`를 통해 불러오기

<br>

### CSS with 개발자 도구

- styles : 해당 요소에 선언된 모든 CSS
- computed : 해당 요소에 최종 계산된 CSS

1. 개발자 도구에서 이것저것 바꿔보며 찍어보기, "음.. 25px이 더 좋은 것 같은데?"
2. vs코드에서 코드 수정
3. 웹 새로고침, 수정된 것 확인하기

<br>

### CSS 기초 선택자

- 요소 선택자

  - HTML 태그를 직접 선택
  - **잘 쓰지 않는다.**

- **클래스(class) 선택자**

  - 마침표(`.`)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
  - **일반적으로 CSS 스타일링은 클래스로만 한다.**

- 아이디(id) 선택자

  - `#`문자로 시작하며, 해당 아이디가 적용된 항목을 선택

  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장
  - **id는 잘 활용하지 않고, 자바스크립트(JS)로 개발할 때 보통 활용한다.**

<br>

#### 스타일 우선 순위

> id > class > 태그 순으로 우선순위를 가진다.

- 적용에는 우선순위가 있다. 
- 같은 레벨이라면 나중에 '선언'된 것이 적용된다. 

<br>

### CSS 예시

```html
<!DOCTYPE html>
<html>
  <head>
    <title>제목</title>
    <style>

      /* h3 {
        color: brown;
      }
      h4 {
        color: brown;
      } */
      .title-brown { 
        color: brown;
      }
      .title-blue {
        color: blue;
      }
      #title-yellow {
        color: yellow;
      }
      h1 {
        color: red;
        font-size: 25px;
      }
    </style>
  </head>
  <body>
    <h1 class="title-blue title-brown">H1! 갈색</h1>
    <h1>h1 빨간색</h1>
    <h2 style="color: blue; font-size: 15px;">h2</h2>
    <h3 class="title-brown">11</h3>
    <h4 class="title-brown">22</h4>
    <h4 id="title-yellow" class="title-brown">33</h4>
  </body>
</html>
```
