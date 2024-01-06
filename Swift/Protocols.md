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



## 프로토콜은 타입이다.
> 스위프트는 프로토콜을 **일급 객체**로 취급
> **일급 객체** -> **타입으로 사용 가능하다는 의미**

- 프로토콜을 변수에 할당 가능
- 함수 호출할 때, 프로토콜을 파라미터로 전달 가능
- 함수에서 프로토콜로 반환 가능

```swift
protocol Remote {
    func turnOn()
    func turnOff()
}
struct SetTopBox: Remote {
    func turnOn() {
        print("셋톱박스켜기")
    }
    
    func turnOff() {
        print("셋톱박스끄기")
    }
    
    func doNetflix() {
        print("넷플릭스 하기")
    }
}
let sbox = SetTopBox()
sbox.turnOn()
sbox.turnOff()
//sbox.doNetflix() // 사용할 수 없음
```

프로토콜로 업캐스팅이 가능하지만 그러면 **프로토콜이 가진 메서드만 호출 가능**



### 프로토콜 타입 취급의 장점
1. 공통된 타입으로 쓸 수 있음.
1. 파라미터로 사용 가능
3. is, as 연산자 사용 가능
   - `is` : 타입 체크, 동일한 타입 혹은 서브클래스인 경우 `true`
   - `as` : 업 캐스팅 or 다운 캐스팅

```swift
let electronic: [Remote] = [tv, sbox]
func turnOnSomeElectronics(item: Remote) {
    item.turnOn()
}
electronic[0] is TV // true
let sbox2: SetTopBox? = electronic[1] as? SetTopBox
sbox2?.doNetflix()
```



### 프로토콜의 상속

- 프로토콜 간에 상속이 가능
- 다중 상속 가능

```swift
protocol SuperRemoteProtocol: Remote, AirConRemote {
    // func turnOn()     // 채택한 프로토콜 요구사항 모두 상속 받음 
    // func turnOff()
    // func Up()
    // func Down()
    func doSomething()
}
```



### 클래스 전용 프로토콜
> `AnyObject`프로토콜을 상속함으로써 **클래스 전용 프로토콜로 선언 가능**
- `AnyObject` : 어떤 **클래스** 타입의 인스턴스도 표현할 수 있는 프로토콜 타입



### 프로토콜 합성
> 프로토콜을 합성하여 임시 타입으로 활용 가능
- `&`를 사용하여 연결함.

```swift
func wishHappyBirthday(to celebrator: Named & Aged) {  // 임시 타입으로 인식
    print("생일축하해, \(celebrator.name), 넌 이제 \(celebrator.age)살이 되었구나!")
}
```



### 프로토콜의 선택적 요구사항의 구현 (Optional Protocol Requirements)
> 요구사항 구현을 해도 되고 안해도 됨.
- 어트리뷰트 (Attribute)
	- `@available, @objc, @escaping, @IBOutlet, @IBAction 등등`
	- 1. 선언에 대한 추가정보 제공 `@available`
	- 2. 타입에 대한 추가정보 제공 `@escaping`

### 선택적인 멤버 선언하기
```swift
@objc protocol Remote {
    @objc optional var isOn: Bool { get set }
    func turnOn()
    func turnOff()
    @objc optional func doNeflix()
}
```
- 프로토콜 앞에 `@objc` 키워드를 붙여야함.
	- `@objc`: Objective-C에서도 사용할 수 있게 하는 어트리뷰트
- 속성이나 메서드 앞에 `@objc optional` 키워드를 붙여야함.
- **클래스 전용 프로토콜임**
	- Objective-C는 구조체나 열거형에서 프로토콜 채택을 지원하지 않음.



## 프로토콜의 확장 (Protocol Extension)
### 기존 문제점
> 프로토콜을 반복해서 구현해야 하는 불편함이 있음.
```swift
protocol Remote {
    func turnOn()
    func turnOff()
}
class TV1: Remote {
    func turnOn() { print("리모콘 켜기") }
    func turnOff() { print("리모콘 끄기") }
}
struct Aircon1: Remote {
    func turnOn() { print("리모콘 켜기") }
    func turnOff() { print("리모콘 끄기") }
}
```

### 프로토콜 확장
> 기본(디폴트) 구현 제공 -> 코드 중복을 피할 수 있음
```swift
extension Remote {
    func turnOn() { print("리모콘 켜기") }    
    func turnOff() { print("리모콘 끄기") }   
    func doAnotherAction() {               
        print("TV 또 다른 동작") 
    }
}
class TV1: Remote {
    func turnOn() { print("TV 켜기") }
    func doAnotherAction() { print("리모콘 또 다른 동작") }
}
var tv1 = TV1()
tv1.turnOn() // TV 켜기
tv1.turnff() // 리모콘 끄기
tv1.doAnotherAction() // TV 또 다른 동작

var tv2: Remote = TV1()
tv2.doAnotherAction() // 리모콘 또 다른 동작
```
- 요구사항의 메서드도 구현하고 확장으로 기본 메서드도 구현했다면?
	- **1. 본체의 요구사항 메서드 -> 2. 기본 메서드** 순으로 적용
- 요구사항은 아니지만 본체와 확장 둘다 같은 메서드를 구현했다면?
	- **인스턴스의 타입에 따라 달라짐**

### 프로토콜의 확장을 통한 다형성 제공 - 프로토콜 지향 프로그래밍
**다형성:** 객체지향 프로그래밍에서의 중요한 개념으로, 여러 타입이나 객체가 동일한 인터페이스를 통해 동작할 수 있는 능력을 의미
**프로토콜 지향 프로그래밍:** 객체지향 프로그래밍에서의 상속 대신 프로토콜을 통해 다형성을 구현하는 개념

- 프로토콜로 정의되고 클래스로 구현하면 메서드가 클래스 테이블과 프로토콜 테이블에 저장됨. 그래서 인스턴스가 클래스면 클래스 테이블을, 프로토콜이면 프로토콜 테이블을 찾아가 실행함.

