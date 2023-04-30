# Swift 기본 문법 정리

## 이름짓기 규칙
- function, method, variable, constant
=> `Lower Camel Case`
ex) someVariableName

- type(class, struct, enum, extension...)
=> `Upper Camel Case`
ex) Person, Poing, Week

## 주석
- 한줄 주석 `//`
- 여러줄 주석 `/* */`

## 콘솔로그
```swift
print()
```
- 단순 문자열 출력

```swift
dump()
```
- 인스턴스의 자세한 설명(description 프로퍼티)까지 출력
```swift
import Swift

class Person {
	var name: String = "sebin"
    var age: Int = 10
}
let sebin: Person = Person()

print(sebin)
// __11db_expr_256.Person
dump(sebin)
/* __11db_expr_256.Person 
- name: "sebin"
- age: 10 */
```

## 문자열 보간법
> 사용자 정의 데이터를 문자열에 주입하는 방법

- `\()`
백슬래쉬 뒤 괄호 안에 변수나 상수를 넣을 수 있고, 연산이 가능하다.

```swift
import Swift

let age: Int = 10
print("안녕하세요! 저는 \(age + 5)살입니다.")
// "안녕하세요! 저는 15살입니다."
```

## 상수, 변수
```swift
import Swift

// 상수 선언
let 이름: 타입 = 값

// 변수 선언
var 이름: 타입 = 값

// 값의 타입이 명확하다면 타입 생략 가능
let 이름 = 값
var 이름 = 값

// 나중에 할당할 땐 타입 꼭 명시해야함
let sum: Int
let inputA: Int = 100
let inputB: Int = 200

// 선언 후 할당 가능, 상수는 그 이후 변경 불가능
sum = inputA + inputB
```


> [참고한 Swift 기초 강의](https://www.youtube.com/playlist?list=PLz8NH7YHUj_ZmlgcSETF51Z9GSSU6Uioy)

<br>

# Swift의 기본 데이터 타입
> Bool, Int, UInt, Float, Double, Character, String

## 1. Bool
- 불리언 타입
- 🚨**0과 1은 `int`로 인식하여 에러가 발생한다.**
```swift
var someBool: Bool = true
somBool = false

someBool = 0
someBool = 1
// error: cannot assign value of type 'Int' to type 'Bool'
```

## 2. Int
- 64비트 정수형 타입
- 양수, 음수, 0 모두 포함
- 실수형은 에러 발생
```swift
var someInt: Int = -100

someInt = 100.1
// error: cannot assign value of type 'Double' to type 'Int'
```

## 3. UInt
- Unsigned Int
- 부호가 없는 양의 정수형 타입
- 양수와 0만 가능
```swift
var someUInt: UInt = 100

someUInt = -100
// error: negative integer '-100' overflows when stored into unsigned type 'UInt'

someUInt = someInt
// error: cannot assign value of type 'Int' to type 'UInt'
```

## 4. Float
- 32비트 부동소수형 타입
- **정수형 타입도 받을 수 있다.**
```swift
var someFloat: Float = 3.14
someFloat = 3
```

## 5. Double
- 64비트 부동소수형 타입
- **정수형 타입도 받을 수 있다.**
- `Float`은 받을 수 없다.
```swift
var someDouble: Double = 3.14
someDouble = 3

someDouble = someFloat
// error: cannot assign value of type 'Float' to type 'Double'
```

## 6. Character
- 한 글자 문자형 타입
- 유니코드로 표현하는 모든 문자가 가능하다.
- 문자열은 안된다.
```swift
var someCharacter: Character = "🍎"
someCharacter = "👍"
someCharacter = "가"
someCharacter = "A"

someCharacter = "안녕"
// error: cannot assign value of type 'String' to type 'Character'
```

## 7. String
- 문자열 타입
- 여러 문자 가능
- `+` 연산자로 문자열을 합칠 수 있다.
- **`Character` 타입을 받을 수 없다.**
```swift
var someString: String = "애플 🍎"
someString = someString + "Apple"
// 애플 🍎 Apple

someString = someCharacter
// error: cannot assign value of type 'Character' to type 'String'
```

<br>

# Any, AnyObject, nil이란?

## Any
- **Swift의 모든 타입을 지칭하는 키워드**
- 모든 타입을 수용할 수 있다.
- 다른 타입에 할당할 수 없다.

```swift
var someAny: Any = 100
someAny = "어떤 타입도 가능"
someAny = 123.12

let someDouble: Double = someAny
// Cannot convert value of type 'Any' to specified type 'Double'
```

## AnyObject
- **모든 클래스 타입을 지칭하는 프로토콜**
- 모든 클래스 타입의 인스턴스를 나타낼 수 있다.

```swift
class SomeClass {}
var someAnyObject: AnyObject = SomeClass()

someAnyObject: 123.12
// Value of type 'Double' does not conform to 'AnyObject' in assignment
```

## nil
- **없음을 의미하는 키워드**
- Any 타입, AnyObject 타입에 nil 값을 넣을 수 없다.
- 메모리에 공간조차 만들지 않고 아무것도 없다.

```swift
var array: Array<Int> = []
// array는 빈 배열이 존재하는 empty 상태이며, nil과 다르다.
```