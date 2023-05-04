# Swift의 조건문과 반복문

## 조건문

### if 문

- **조건에는 항상 `Bool` 타입이 들어와야 한다.**

```swift
if condition {
	statements
} else if condition {
	statements
} else {
	statements
}
```

```swift
let someInteger = 100

if someInteger < 100 {
    print("100 미만")
} else if someInteger > 100 {
    print("100 초과")
} else {
    print("100")
} // 100

// if someInteger { }
// someInteger는 Bool 타입이 아닌 Int 타입이기 때문에 컴파일 오류 발생한다.
```

### switch 문

- 범위 연산자를 활용하면 쉽고 유용하다.
- 대부분의 기본 타입을 사용할 수 있다.
- `default` 구문은 필수이다.
- `break`를 쓰지 않아도 자동으로 `case`마다 `break` 된다.
- `fallthrough` 키워드로 `break`를 무시할 수 있다.
- `,`를 사용하여 하나의 `case`에 여러 패턴을 명시할 수 있다.
- 다뤄야할 케이스가 많은 경우, if문보다 더 빠른 성능을 보여준다.

```swift
switch value {
case pattern:
    code
default:
    code
}
```

#### 범위 연산자

- 1 `..<` 100 : 1이상 100 미만
- 101 `...` Int.max : 101이상 최대값 이하

```swift
switch someInteger {
case 0:
    print("zero")
case 1..<100:
    print("1~99")
case 100:
    print("100")
case 101...Int.max:
    print("over 100")
default:
    print("unknown")
} // 100

switch "sebin" {
case "jake":
    print("jake")
    fallthrough
case "mina":
    print("mina")
case "sebin":
    print("sebin")
case "haha", "hoho":
    print("haha")
default:
    print("unknown")
} // sebin
```

## 반복문

### for-in 문

- 범위 연산자와 함께 사용할 수 있다.
- 순서가 필요 없다면 변수자리에 `_` 키워드를 사용해서 성능을 높일 수 있다.
- `Dictionary`의 item은 key와 value로 구성된 `tuple` 타입이다.
- `Dictionary`는 넣었던 순서대로 순회하지 않는다.

```swift
for item in items {
	code
}
```

```swift
var integers = [1, 2, 3]
let people = ["yagom": 10, "eric": 15, "mike": 12]

for integer in integers {
    print(integer)
}

for (name, age) in people {
    print("\(name): \(age)")
}

let base = 3
let power = 10
var answer = 1
for _ in 1...power {
    answer *= base
}
print("\(base) to the power of \(power) is \(answer)")
// 3 to the power of 10 is 59049
```

### while 문

- **조건에는 항상 `Bool` 타입이 들어와야 한다.**

```swift
while condition {
	code
}
```

```swift
while integers.count > 1 {
    integers.removeLast()
}
```

### repeat-while 문

- 구문을 최소 한 번 이상 실행하고 `while` 조건이 거짓일 때까지 반복한다.

```swift
repeat {
	code
} while condition
```

```swift
repeat {
	integers.removeLast()
} while integers.count > 0
```