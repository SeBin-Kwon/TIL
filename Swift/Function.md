# Swift 함수

- Swift는 **함수형 프로그래밍 패러다임**을 포함하는 다중 패러다임 언어이다.
- Swift의 함수는 **일급객체**이므로 변수, 상수 등에 저장이 가능하며 매개변수를 통해 전달도 가능하다.
- 하나의 **데이터 타입으로 표현할 수 있다.**

## 함수 선언의 기본 형태

```swift
func 함수 이름 (매개변수1 이름: 매개변수1 타입, 매개변수2 이름: 매개변수2 타입...) -> 반환 타입 {
	함수 구현부
	return 반환값
}

func sum(a: Int, b: Int) -> Int {
	return a + b
}
```
**반환 값이 없는 경우** `Void`를 사용한다. `Void`는 **생략 가능 하다.**
```swift
func printMyName(name: String) -> Void {
	print(name)
}

func printYourName(name: String) {
	print(name)
}
```
**매개변수가 없는 경우** 괄호만 쓴다.
```swift
func maximumIntegerValue() -> Int {
	return Int.max
}
```
**반환 값과 매개변수 둘 다 없는 경우**
```swift
func hello() -> Void { print("hello") }

func bye() -> { print("bye") }
```

## 함수의 호출

```swift
sum(a: 3, b: 5) // 8

printMyName(name: "sebin") // sebin

printYourName(name: "haha") // haha

maximumIntegerValue() // Int의 최댓값

hello() // hello

bye() // bye
```
---

## 매개변수 기본값

> 매개변수 기본값(default)을 설정하면 값이 들어오지 않을 때, 기본값이 대신 들어간다.

기본값을 갖는 매개변수는 매개변수 목록 중 뒤쪽에 위치하는 것이 좋으며, 호출 시 생략 가능하다.

```swift
func greeting(friend: String, me: String = "sebin") {
	print("Hello \(friend)! I'm \(me)")
}

greeting(friend: "haha") // Hello haha! I'm sebin
greeting(friend: "john", me: "eric") // Hello john! I'm eric
```

## 전달 인자 레이블

> 함수를 호출할 때 매개변수의 역할을 좀 더 명확하게 설명해준다.
> 함수 사용자의 입장에서 표현하고자 할 때 사용한다.

- 전달 인자 레이블은 매개변수 앞에 작성한다.
- 아래 예시에서의 전달 인자 레이블은 `from`과 `to`이다.
- **함수 외부에서 호출할 땐, 전달 인자 레이블을 사용한다.**
- 함수 내부에선 매개변수 이름을 사용한다.

이름이 같은 함수여도 전달 인자 레이블이 다르면 다른 함수로 인식한다. **함수 중복 정의(오버로드)로 동작하게 된다.**

```swift
func greeting(to friend: String, from me: String) {
	print("Hello \(friend)! I'm \(me)")
}

greeting(to: "john", from: "eric") 
// Hello john! I'm eric
```

## 가변 매개변수

> 전달 받을 값의 개수가 명확하지 않을 때 사용 할 수 있다.
> **가변 매개변수는 함수당 하나만 가질 수 있다.**

- `...`을 사용하여 작성한다.
- 맨 뒤에 위치하는 것이 좋다.
- 전달 인자가 없거나 `nil`을 넣어주게 되면 에러가 난다.
- 가변 인자에 아무것도 넣고 싶지 않다면 그냥 생략하자.

```swift
func sayHelloToFriends(me: String, friends: String...) -> String {
	return "Hello \(friends)! I'm \(me)!"
}

print(sayHelloToFriends(me: "sebin", friends: "haha", "eric", "park"))
// Hello ["haha", "eric", "park"]! I'm sebin!

print(sayHelloToFriends(me: "sebin"))
// Hello []! I'm sebin!
```

## 데이터 타입으로서의 함수

```swift
(매개변수1 타입, 매개변수2 타입 ...) -> 반환 타입
```
- 반환 타입은 생략할 수 없다.
- 타입이 다른 함수는 할당할 수 없다.

```swift
// 변수에 String 타입을 가진 매개변수 2개를 받으면서 반환 값이 없는 함수가 들어올 수 있는데 greeting 함수를 할당함
var someFunction: (String, String) -> Void = greeting(to:from:)

someFunction("eric", "sebin")
// Hello eric! I'm sebin

someFunction = greeting(friend:me:)
someFunction("eric", "sebin")
// Hello eric! I'm sebin

someFunction = sayHelloToFriends(me: friends:)
// 에러 발생
// sayHelloToFriends 함수는 가변 매개변수를 가지기 때문에 타입이 다르다.

// 함수의 매개변수로 함수가 왔다.
// runAnother 함수안에 function 함수를 실행한다.
func runAnother(function: (String, String) -> Void) {
	function("jenny", "mike")
}

runAnother(function: greeting(friend:me:))
// Hello jenny! I'm mike
runAnother(function: someFunction)
// Hello jenny! I'm mike
```