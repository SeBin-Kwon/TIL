# Protocols

### 클래스 상속의 단점

- 클래스는 **하나만 상속 가능. 다중 상속 불가능**
- **상위 클래스의 메모리 구조를 따라가야만 함**
- 클래스라는 타입만 가능

**위 단점을 보완하기 위해 프로토콜이 생김**
프로토콜은 실생활에서 **자격증** 같은 것. **누구나 딸 수 있음**

## 정의

```swift
protocol SomeProtocol {
	func playPiano()
}
```
- **구체적인 구현을 하지 않음 -> 구체적인 구현은 채택한 곳에서 구현 함.**
- 이런 메서드를 반드시 구현해야 한다는 **요구 사항**
- **프로토콜을 타입으로 인식**
	- 메서드의 파라미터 타입을 프로토콜로 할 수 있음.

## 프로토콜이 구현해야한다고 선언하는 요구사항
1. 속성 요구사항
2. 메서드 요구사항 (메서드/생성자/서브스크립트)
### 1. 속성 요구사항
- 무조건 `var`로 선언해야함.
- `get`, `set` 키워드를 통해서 읽기/쓰기 여부를 설정
- 기본값을 넣을 수 없다.
- **최소한의 요구사항일 뿐이다.**

```swift
// 요구사항 정의
protocol RemoteMouse {
    var id: String { get }                // ===> let 저장속성 / var 저장속성 / 읽기계산속성 / 읽기,쓰기 계산속성
    var name: String { get set }          // ===> var 저장속성 / 읽기,쓰기 계산속성
    static var type: String { get set }   // ===> 타입 저장 속성 (static)
                                          // ===> 타입 계산 속성 (class)
}

// 채택 및 구현
struct TV: RemoteMouse {
    var id: String = "456" // let도 가능
    var name: String = "삼성티비" // 최소 set이므로 var나 get,set으로 구현
    static var type: String = "리모콘" // 타입으로 구현해야함.
}
```

#### 타입 속성 요구사항
- 저장 타입 속성으로 구현시 `static`키워드만 가능 (재정의 불가)
- 클래스에서 채택시 계산 타입 속성에서 `static`, `class` 모두 구현 가능
	- 타입 속성의 의미일 뿐
	- `class` 키워드는 재정의 가능



### 2. 메서드 요구사항

```swift
protocol RandomNumber {
    static func reset()
    func random() -> Int
    mutating func doSomething()
}
```
- 메서드 헤드 부분(인풋/아웃풋)만 요구사항으로 정의
- 타입 메서드는 구현하는 쪽에서 `static` 혹은 `class` 키워드를 붙여야 함.
- `mutating` 키워드는 메서드 내에서 값타입의 속성 변경을 의미할 뿐(클래스에서 사용 가능). 구현할 때에도 `mutating` 붙여야 함.



### 3. 생성자 요구사항
```swift
protocol SomeProtocol {
    init(num: Int)
}

class SomeClass: SomeProtocol {
    required init(num: Int) {
        // 실제 구현
    }
}

class SomeSubClass: SomeClass {
    // 하위 클래스에서 생성자 구현 안하면 필수 생성자는 자동 상속
    // required init(num: Int)
}
```
- **클래스는 `required`를 꼭 붙여서 구현해야함.**
	- 하위 클래스에 상속되는 걸 고려
- 클래스가 `final`로 선언하면 `required` 안 붙여도 됨.
	- 마지막 클래스이므로 상속되지 않기 때문
- 클래스에서 지정 생성자, 편의 생성자 상관없이 구현 가능
- 요구사항이 `init()?`이면 `init()?`, `init()` 다 상관없이 가능



### 4. 서브스크립트 요구사항
```swift
protocol DataList {
    subscript(idx: Int) -> Int { get }
}

struct DataStructure: DataList {
    subscript(idx: Int) -> Int {
        get {
            return 0
        }
        set {   // 구현은 선택
            // 상세구현 생략
        }
    }
}
```
- 서브스크립트 문법에서는 **get 필수 set 선택**
- 요구사항 get -> 읽기만 구현해도 됨.
- 요구사항 get/set -> 읽기쓰기 모두 구현해야 함.



## 프로토콜은 보통 확장에서 채택

> 코드를 좀 더 깔끔하게 정리할 수 있기 때문. **본체보다는 확장에서 채택 및 구현하는 것을 선호함.**

```swift
protocol Certificate {
    func doSomething()
}

class Person {
}

extension Person: Certificate {
    func doSomething() {
        print("Do something")
    }
}
```



