# Swift의 클로저

> 클로저는 실행가능한 코드 블럭

- 함수와 달리 **이름정의는 필요하지 않음**
- 함수와는 매개변수 전달과 반환 값이 존재 할 수 있다는 점이 동일
- 함수는 이름이 있는 클로저
- 일급객체로 전달인자, 변수, 상수 등에 저장 및 전달이 가능
- 다른 언어의 람다(`lambdas`)와 비슷하다.

## 클로저를 사용하는 이유

왜 이름이 필요없을까?
- 함수를 실행 할 때 전달하는 형태로 사용하기 때문
- 정의 하면서 동시에 전달하기 때문에 굳이 이름이 필요없다.

**본래 정의된 함수를 실행**시키면서, **클로저를 사후적으로 정의 가능**

사후적으로 정의가 가능하다 -> **활용도가 매우 높음**
- 실질적으로 순차적으로 실행됨.
- 향후 개발자가 원하는대로 확장과 응용 가능

```swift
{ (매개변수 목록) -> 반환타입 in
    실행 코드
}
```
```swift
// 함수를 사용한다면
func sumFunction(a: Int, b: Int) -> Int {
	return a + b
}
var sumResult: Int = sumFunction(a: 1, b: 2)
print(sumResult) // 3

// 클로저의 사용
// sum이라는 상수에 클로저를 할당
var sum: (Int, Int) -> Int = { (a: Int, b: Int) Int in
    return a + b
}

sumResult: Int = sum(1, 2)
print(sumResult) // 3

// 함수는 클로저의 일종이므로 sum 변수에 할당 가능
sum = sumFunction(a:b:)
sumResult = sum(1,2)
print(sumResult) // 3
```
### 함수의 전달인자로서의 클로저

- 클로저는 주로 함수의 전달인자로 많이 쓰인다.
- 함수 내부에서 원하는 코드블럭을 실행 할 수 있다.

```swift
let add: (Int, Int) -> Int
add = { (a: Int, b: Int) in
    return a + b
}

let substract: (Int, Int) -> Int
substract = { (a: Int, b: Int) in
    return a - b
}

let divide: (Int, Int) -> Int
divide = { (a: Int, b: Int) in
    return a / b
}

func calculate(a: Int, b: Int, method: (Int, Int) -> Int) -> Int {
    return method(a, b)
}

var calculated: Int

calculated = calculate(a: 50, b: 10, method: add)

print(calculated) // 60

calculated = calculate(a: 50, b: 10, method: substract)

print(calculated) // 40

calculated = calculate(a: 50, b: 10, method: divide)

print(calculated) // 5

//따로 클로저를 상수/변수에 넣어 전달하지 않고, 
//함수를 호출할 때 클로저를 작성하여 전달할 수도 있습니다.

calculated = calculate(a: 50, b: 10, method: { (left: Int, right: Int) -> Int in
    return left * right
})

print(calculated) // 500
```

## 다양한 클로저 표현

### 기본 클로저 표현

```swift
// 클로저를 매개변수로 갖는 함수 calculated(a:b:method:)와 결과값을 저장할 변수 result 선언
func calculate(a: Int, b: Int, method: (Int, Int) -> Int) -> Int {
    return method(a, b)
}

var result: Int
```

### 1. 후행 클로저

클로저가 **함수의 마지막 전달인자일때**, 마지막 매개변수 이름을 **생략**하고 함수 소괄호 **외부**에 클로저를 구현할 수 있다.

```swift
result = calculate(a: 10, b: 10) { (left: Int, right: Int) -> Int in
    return left + right
}

print(result) // 20
```

### 2. 반환타입 생략

`calculate(a:b:method:)` 함수의 method 매개변수는 `Int` 타입을 반환할 것이라는 사실을 컴파일러도 알기 때문에 
굳이 클로저에서 **반환타입을 명시하지 않아도 된다. 대신 `in` 키워드는 생략할 수 없다.**

```swift
result = calculate(a: 10, b: 10, method: { (left: Int, right: Int) in
    return left + right
})

print(result) // 20

// 후행클로저와 함께 사용할 수도 있음
result = calculate(a: 10, b: 10) { (left: Int, right: Int) in
    return left + right
}

print(result) // 20
```

### 3. 단축 인자이름

클로저의 매개변수 이름이 필요 없다면 **단축 인자이름**을 활용할 수 있다. 클로저의 매개변수의 순서대로 `$0`, `$1`, `$2`...로 표현한다.

```swift
result = calculate(a: 10, b: 10, method: {
    return $0 + $1
})

print(result) // 20


// 후행 클로저와 함께 사용할 수 있음
result = calculate(a: 10, b: 10) {
    return $0 + $1
}

print(result) // 20
```

### 4. 암시적 반환 표현

클로저가 반환하는 값이 있다면 클로저의 마지막 줄의 결과값은 암시적으로 반환값으로 취급하므로 `return` 생략 가능하다.

```swift
result = calculate(a: 10, b: 10) {
    $0 + $1
}

print(result) // 20

// 한줄 표현
result = calculate(a: 10, b: 10) { $0 + $1 }

print(result) // 20
```

### 축약 전과 후 비교

```swift
//축약 전
result = calculate(a: 10, b: 10, method: { (left: Int, right: Int) -> Int in
    return left + right
})

//축약 후
result = calculate(a: 10, b: 10) { $0 + $1 }

print(result) // 20
```

> 너무 축약된 코드는 타인이 보거나, 시간이 지난 뒤에 볼 때 명시성이 떨어질 수 있으므로 적정선에서 축약하도록 하자!