# 🧩 Grid system (web design)

- 요소들의 디자인과 배치에 도움을 주는 시스템
- 기본 요소
  - `Column` : 실제 컨텐츠를 포함하는 부분
  - `Gutter` : 칼럼과 칼럼 사이의 공간 (사이 간격)
  - `Container` : Column들을 담고 있는 공간
- Bootstrap Grid system은 flexbox로 제작됨
- container, rows, column으로 컨텐츠를 배치하고 정렬
- 반드시 기억해야 할 2가지!
  1. **12개의 column**
     - 12를 넘어가면 밑으로 내려가버린다.
  2. **6개의 grid breakpoints**

```html
<div class="container"> <div class="row">
    <div class="col"></div>
    <div class="col"></div>
    <div class="col"></div>
</div> </div>
```

<br>

### Grid system breakpoints

```html
<div class="row">
<div class="box col-9">col-9</div> <div class="box col-4">col-4</div> <div class="box col-3">col-3</div>
</div>

<h2 class="text-center">alignment</h2>
<div class="row parent justify-content-center align-items-center">
<div class="box col-4">justify-content-center / align-items-center</div> </div>
```

<br>

### 미디어쿼리

```css
@media (min-width: 576px) { .container-sm, .container {
  max-width: 540px;
} }
@media (min-width: 768px) {
  .container-md, .container-sm, .container {
max-width: 720px; }
}
@media (min-width: 992px) {
.container-lg, .container-md, .container-sm, .container { max-width: 960px;
} }
@media (min-width: 1200px) {
.container-xl, .container-lg, .container-md, .container-sm, .container {
    max-width: 1140px;
  }
}
@media (min-width: 1400px) {
.container-xxl, .container-xl, .container-lg, .container-md, .container-sm, .container { max-width: 1320px;
} }
```