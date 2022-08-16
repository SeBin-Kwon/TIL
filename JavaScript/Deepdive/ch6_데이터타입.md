# 데이터 타입

> 자바스크립트의 모든 값은 데이터 타입을 갖는다.

- 원시 타입

  - 숫자 타입

    : 숫자. 정수와 실수 구분 없이 하나의 숫자 타입만 존재

  - 문자열 타입

    : 문자열

  - 불리언 타입

    : 논리적 참(True)과 거짓(False)

  - undefined 타입

    : var 키워드로 선언된 변수에 암묵적으로 할당되는 값

  - null 타입

    : 값이 없다는 것을 의도적으로 명시할 때 사용하는 값

  - 심벌 타입

    : ES6에서 추가된 7번째 타입

- 객체 타입
  - 객체, 함수, 배열 등

<br>

## 1. 숫자 타입

> 자바스크립트는 독특하게 하나의 숫자 타입만 존재한다.

- 자바스크립트는 **모든 수를 `실수`로 처리**하며, 정수만 표현하기 위한 데이터 타입이 별도로 존재하지 않는다.

정수, 실수, 2진수, 8진수, 16진수 리터럴은 모두 메모리에 배정밀도 **64비트 부동소수점 형식의 2진수**로 저장된다.

이들 값을 참조하면 **모두 10진수로 해석**된다.

```javascript
var binary = 0b01000001; // 2진수
var octal = 0o101; // 8진수
var hex = 0x41; // 16진수

// 표기법만 다를 뿐 모두 같은 값이다.
console.log(binary); // 65
console.log(octal); // 65
console.log(hex); // 65
console.log(binary === octal); // true
console.log(octal === hex); // true

// 숫자 타입은 모두 실수로 처리된다.
console.log(1 === 1.0); // true
console.log(4 / 2); // 2
console.log(3 / 2); // 1.5
```

<br>

#### 숫자 타입의 추가적인 표현

- `Infinity` : 양의 무한대
- `-Infinity` : 음의 무한대
- `NaN` : 산술 연산 불가 (not-a-number)

```javascript
console.log(10 / 0); // Infinity
console.log(10 / -0); // -Infinity
console.log(1 * 'String'); // NaN
```

- 자바스크립트는 대소문자를 구분하므로 NaN이 아닌 다른 문자는 식별자로 해석한다.

<br>

## 2. 문자열 타입

> 텍스트 데이터를 나타내는 데 사용되며, 텍스트를 작은 따옴표('')나 큰 따옴표("") 또는 백틱(``)으로 감싼다.

- 자바스크립트의 문자열을 원시 타입이며, **변경 불가능한 값 (immutable value)**이다.

<br>

## 3. 템플릿 리터럴

> ES6부터 템플릿 리터럴이라고 하는 새로운 문자열 표기법이 도입되었다.

- 템플릿 리터럴은 멀티라인 문자열, 표현식 삽입, 태그드 템플릿 등 편리한 문자열 처리 기능을 제공한다.
- 런타임에 일반 문자열로 변환되어 처리된다.
- 일반 문자열과 비슷해 보이지만 따옴표 대신 백틱(``)을 사용해 표현한다.

```javascript
var template = `Template literal`;
console.log(template); // Template literal
```

### 멀티라인 문자열

> 일반 문자열 내에서는 줄바꿈(개행)이 허용되지 않는다. 따라서 백슬래시(\\)로 이스케이프 시퀀스를 사용해야 한다.

일반 문자열과 달리 템플릿 리터럴 내에서는 이스케이프 시퀀스를 사용하지 않고도 **줄바꿈이 허용**되며, **모든 공백도 있는 그대로 적용**된다.

```javascript
var template = '<ul>\n\t<li><a href="#">Home</a></li>\n</ul>';
console.log(template);
/* 
<ul>
    <li><a href="#">Home</a></li>
</ul>
*/

var template = `<ul>
    <li><a href="#">Home</a></li>
    </ul>`;
console.log(template);
/* 
<ul>
    <li><a href="#">Home</a></li>
</ul>
*/
```