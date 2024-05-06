# tuple
> 튜플은 Collection Type이 아니다

- **여러 타입을 섞어서 저장이 가능하다.**
- `.`으로 값에 접근한다.
- **선언한 후 자료형 및 멤버 개수는 수정 불가능하다.**

```swift
let tuple = ("good", 12, 341.4)
tuple.0 // "good"
```

- 튜플 멤버들에 이름을 붙일 수 있다.
- 멤버 수 만큼 분해 가능하다.(언패킹)
	- 필요 없는 멤버는 `_` 와일드카드 패턴으로 생략 가능

```swift
var tuple = (str: "good", int: 12, dou: 341.4)
tuple.int // 12

let (name, width, height) = tuple
let (name, width, _) = tuple
```

- `typealias`와 같이 쓰면 깔끔하게 사용 가능하다.

```swift
typealias People = (name:String, age:Int, height:Double)

var person: People = ("son", 22, 160.5)
```