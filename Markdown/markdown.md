# ✒️ Markdown Syntax



## Heading

> 문서의 제목이나 소제목으로 사용

- #뒤에 띄어쓰기 하기
- #의 개수에 따라 h1~h6 까지 표현 가능
- 문서의 구조를 위해 작성되며 **글자 크기를 조절하기 위해 사용되어서는 안됨**
- `cmd+(숫자)`로 쉽게 수정 가능



## List

> 순서가 있는 리스트(ol)와 순서가 없는 리스트(ul)로 구성

목록 활용시 단계를 tab과 shift + tab으로 조절한다.

- 순서가 있는 리스트
  - `(숫자).`후에 쓰면 된다.

- 순서가 없는 리스트
  - `-`(hypen)후에 쓰면 된다. 혹은` *`(asterisk)



## Fenced Code block

- backtick 기호 3개를 활용하여 작성(\``` ```)
- 특정 언어 명시하면 Syntax highlighting 적용 가능
  - 일부 환경에서는 적용 안될 수도 있음

```html
<h1>
   제목
</h1>
<!-- 주석 -->
```

```python
print('hello')
```



## Inline Code block

- backtick 기호 1개를 인라인에 활용하여 작성(``)

`print`는 파이썬에서 출력하는 함수이다



## Link

- [링크이름\](url)



## 이미지

- ![문자열\](url)

![lemon](markdown.assets/svitlana.jpg)

- 다른 사람에게 공유할 때, 상대 경로로 설정 해야 한다.



## Blockquotes (인용문)

> `>`를 통해 인용문을 작성



## Table (표)

- 본문 > 표 > 표삽입 / 커맨드+옵션+ t

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |



## text 강조

> 굵게(bold), 기울임(Italic)을 통해 특정 글자들을 강조

**굵게(볼드체)** `**`  cmd + b

*기울림(이탤릭체)* `*` cmd + i

~~취소선~~ `~~`

***기울임굵게***`***`



## 수평선

- 3개 이상의 asterisks (***), dashes (---), or underscores (___)

`---`



---

