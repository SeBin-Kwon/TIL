# 표현식과 문

## 1. 값

> 값은 식(표현식)이 평가되어 생성된 결과를 말한다.
>
> 평가 : 식을 해석해서 값을 생성하거나 참조하는 것을 의미

```javascript
// 평가되어서 숫자 값 30을 생성
10 + 20;

// 변수에는 10 + 20이 평가되어 생성된 숫자 값 30이 할당 된다.
var sum = 10 + 20;
```

모든 값은 `데이터 타입`을 가지며 메모리 2진수, 즉 `비트의 나열`로 저장된다.

변수 이름 sum이 기억하는 메모리 공간에 저장된 것은 10 + 20이 아니라 값 30이다.

**따라서 할당 이전에 평가되어 값을 생성해야 한다.**



## 2. 리터럴

> 리터럴은 사람이 이해할 수 있는 문자 또는 약속된 기호를 사용해 값을 생성하는 표기법을 말한다.
>
> 값을 생성하기 위해 미리 약속한 표기법

|      리터럴       |                예시                |
| :---------------: | :--------------------------------: |
|    정수 리터럴    |                100                 |
| 부동소수점 리터럴 |                0.5                 |
|   2진수 리터럴    |             0B01000001             |
|   문자열 리터럴   |              'Hello'               |
|   불리언 리터럴   |            true, false             |
|    null 리터럴    |                null                |
| undefined 리터럴  |             undefined              |
|    객체 리터럴    | { name: 'kwon', address: 'seoul' } |
|    배열 리터럴    |            [ 1, 2, 3 ]             |
|    함수 리터럴    |           function() {}            |

자바스크립트 엔진은 코드가 실행되는 시점인 `런타임`에 리터럴을 평가해 값을 생성한다.

```javascript
// 숫자 리터럴 50
50
```

위 예제의 50은 단순한 아라비아 숫자가 아닌 `숫자 리터럴`이다.

아라비아 숫자를 사용해 `숫자 리터럴 50`을 코드에 기술하면 자바스크립트 엔진은 이를 평가해 `숫자 값 50`을 생성한다.



## 3. 표현식

> 표현식은 값으로 평가될 수 있는 문이다. 즉, 표현식이 평가되면 새로운 값을 생성하거나 기존 값을 참조한다.

- 리터럴은 값으로 평가되므로 **리터럴도 표현식이다.**

```javascript
var score = 50 + 50;
score; // 100
```

50 + 50은 리터럴과 연산자로 이뤄져있지만 평가되어 `숫자 값 100`을 생성하므로 표현식이다.

변수 식별자를 참조하면 `변수 값`으로 평가되어 표현식이다.



## 4. 문

> 문은 프로그램을 구성하는 기본 단위이자 최소 실행 단위다. = 명령문

문의 집합으로 이뤄진 것이 **프로그램**, 문을 작성하고 순서에 맍게 나열하는 것이 **프로그래밍**이다.

> 토큰 : 문법적인 의미를 가지며, 문법적으로 더 이상 나눌 수 없는 코드의 기본 요소를 의미한다.
>
> ex) 키워드, 식별자, 연산자, 리터럴, 세미콜론(;), 마침표(.)

문은 선언문, 할당문, 조건문, 반복문 등으로 구분할 수 있다.

```javascript
// 변수 선언문
var x;

// 할당문
x = 5;

// 함수 선언문
function foo() {}

// 조건문
if (x>1) { console.log(x); }

// 반복문
for (var i=0; i<2; i++) { console.log(i); }
```



## 5. 세미콜론과 세미콜론 자동 삽입 기능

> 세미콜론(;)은 문의 종료를 나타낸다.

- 단, 0개 이상의 문을 `중괄호로 묶은 코드 블록({...})` 뒤에는 **세미콜론을 붙이지 않는다.**

  ex) if 문, for 문, 함수 등

세미콜론은 세미콜론 자동 삽입 기능 때문에 생략은 가능하지만 예측과 달리 동작을 안할 수도 있기 때문에 세미콜론 사용을 권장한다.



## 6. 표현식인 문과 표현식이 아닌 문

> 표현식은 문의 일부일 수도 있고 그 자체로 문이 될 수도 있다.

```javascript
// 변수 선언문은 값으로 평가될 수 없으므로 표현식이 아니다.
var x;

// 모두 표현식이다.
1
2
1 + 2

// 할당문은 표현식이면서 완전한 문이다.
x = 1 + 2;
x = 100;
```

변수에 할당하는 것으로 표현식인 문인지 아닌지 구별할 수 있다.

- 표현식인 문은 값으로 평가되므로 **변수에 할당할 수 있다.**

- 표현식이 아닌 문은 값으로 평가할 수 없으므로 **변수에 할당할 수 없다.**

```javascript
// 표현식이 아닌 문은 값처럼 사용할 수 없다.
var foo = var x; // SyntaxError: Unexpected token var

// 표현식인 문은 값처럼 사용할 수 있다.
var foo = x = 100;
console.log(foo); // 100
```



### 완료 값

> 크롬 개발자 도구에서 표현식이 아닌 문을 실행하면 언제나 undefined를 출력한다. 이를 `완료 값`이라 한다.

`완료 값`은 **표현식의 평가 결과가 아니다.** 따라서 다른 값과 같이 변수에 할당할 수 없고 참조할 수도 없다.

```javascript
// 변수 선언문 및 할당문
var foo = 10; // undefined
// 조건문
if (true) {} // undefined

//표현식 문: 표현식은 평가된 값을 반환한다.
100 + num; // 110

// 할당문
num = 100; // 100
```

