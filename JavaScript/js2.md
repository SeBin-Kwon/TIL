# 🌪 ECMA Script

### 코딩 스타일 가이드

- 코딩 스타일의 핵심은 합의된 원칙과 일관성
  - 절대적인 하나의 정답은 없으며, 상황에 맞게 원칙을 정하고 일관성 있게 사용하는 것이 중요
- 코딩 스타일은 코드의 품질에 직결되는 중요한 요소
  - 코드의 가독성, 유지보수 또는 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼침
- (참고) 다양한 자바스크립트 코딩 스타일 가이드
  - [Airbnb Javascript Style Guide](https://github.com/airbnb/javascript)
  - [Google Javascript Style Guide](https://google.github.io/styleguide/jsguide.html)
  - [standardjs](https://standardjs.com/#javascript-style-guide-linter-and-formatter)

<br>

## 변수와 식별자

- `식별자(identifier)`는 변수를 구분할 수 있는 변수명을 말함
- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예약어* 사용 불가능
  - 예약어 예시 : for, if, function 등
- `선언 (Declaration)`
  - 변수를 생성하는 행위 또는 시점 
- `할당 (Assignment)`
  - 선언된 변수에 값을 저장하는 행위 또는 시점
- `초기화 (Initialization)`
  - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

<br>

### let, const

- `let` (재할당 가능) (재선언 불가능)

  ```js
  let foo // 선언
  console.log(foo) // undefined
  
  foo = 11 // 할당
  console.log(foo) // 11
  
  let bar = 0 // 선언 + 할당
  console.log(bar) // 0
  
  let number = 10
  let number = 50
  
  // Uncaught SyntaxError : Identifier 'number' has already been declared
  ```

- `const` (재할당 불가능) (재선언 불가능)

  ```js
  const number = 10 
  // 1. 선언 및 초기값 할당
  number = 10
  // 2. 재할당 불가능
  
  // Uncaught TypeError : Assignment to constant variable
  
  const number = 10
  const number = 50
  
  // Uncaught SyntaxError : Identifier 'number' has already been declared
  ```

- **블록 스코프 (block scope)**

  - if, for, 함수 등의 중괄호 내부를 가리킴
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

  ```js
  let x = 1
  
  if (x === 1) {
    let x = 2
    console.log(x)  // 2
  }
  console.log(x) // 1
  ```

<br>

### var

- var로 선언한 변수는 재선언 및 재할당 모두 가능

- ES6 이전에 변수를 선언할 때 사용되던 키워드
- `호이스팅`되는 특성으로 인해 예기치 못한 문제 발생 가능
  - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장

```js
var number = 10
// 1. 선언 및 초기값 할당
var number = 50
// 2. 재할당

console.log(bar) // 50
```

- **함수 스코프 (function scope)**

  - 함수의 중괄호 내부를 가리킴
  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

  ```js
  function foo() {
    var x = 5
    console.log(x)  // 5
  }
  
  // ReferenceError : is not defined
  console.log(x)
  ```

### 호이스팅

- 호이스팅 (hoisting)
  - 변수를 선언 이전에 참조할 수 있는 현상
  - 변수 선언 이전의 위치에서 접근 시 undefined를 반환

- 자바스크립트는 모든 선언을 호이스팅한다.
- 즉, var, let, const 모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생 하여 일시적 사각지대가 존재하지 않는다.

<br>

## 데이터 타입