# 접근 제어
> 코드 세부 구현 내용을 숨기는 것이 가능하도록 만드는 개념
- **객체지향 - 은닉화가 가능해짐**

```swift
class SomeClass {
	// 내부적으로만 사용하겠다고 제한
    private var name = "이름"
    func nameChange(name: String) {
	    // 어떤 로직을 넣을 수도 있음
        if name == "길동" {
            return             
        }
        self.name = name
    }
}
let object1 = SomeClass()
// 이름을 바꾸려면 특정 메서드로 실행만 가능
object1.nameChange(name: "민영")
```

## Swift의 5가지 접근 수준 (Access Levels)
1. `open` : 다른 모듈에서도 접근 가능 / 상속 및 재정의도 가능 (제한 낮음)
2. `public` : 다른 모듈에서도 접근 가능 (상속 / 재정의 불가)
3. `internal`: 같은 모듈 내에서만 접근 가능 (default)
4. `fileprivate` : 같은 파일 내에서만 접근 가능
5. `private` : 같은 scope내에서만(중괄호) 접근가능 (제한 높음)

- 모듈(module) : 프레임워크, 라이브러리, 앱 등 import해서 사용할 수 있는 외부의 코드
- 따로 명시하지 않으면 `internal` 설정임 (default)
- 모듈(프레임워크나 라이브러리)을 만들어서 배포하려면, `public`이상으로 선언해야함
- 클래스의 접근수준을 가장 넓히면 - `open` / 구조체 - `public`
	- 클래스 - `open` (상속, 재정의와 관계)
	- 구조체 - `public` (구조체는 어차피 상속이 없기 때문)

### 접근 제어를 가질 수 있는 요소
> Swift 문서 : 엔터티 / 독립된 개체 -> 사실상 모든 요소임
1. 타입 (클래스/구조체/열거형/스위프트 기본타입 등)
2. 변수/속성 
3. 함수/메서드 (생성자, 서브스크립트 포함)
4. 프로토콜도 특정영역으로 제한될 수 있음

## 접근 제어 기본 원칙
> 타입은 타입을 사용하는 변수(속성)나, 함수(메서드)보다 높은 수준(넓은)으로 선언되어야함.

```swift
// public variable에 속한 타입은 더 낮은 접근 수준을 가지지 못함
// (public/internal/fileprivate/private) 만 사용 가능
var some: String = "접근가능" // open 키워드 사용 불가능, String이 public이기 때문

// 파라미터, 리턴 타입이 더 낮은 접근 수준을 가지지 못함
// (internal/fileprivate/private) 만 사용 가능
internal func someFunction(a: Int) -> Bool {
    print(a)         // Int 타입
    print("hello")   // String 타입
    return true      // Bool 타입
}
```
- 자신보다 내부에서 더 낮은 타입을 사용하면 접근을 못해서, 사용하지 못할 수 있음

#### 기본 문법
```swift
// 타입
public class SomePublicClass {}
internal class SomeInternalClass {}
fileprivate class SomeFilePrivateClass {}
private class SomePrivateClass {}


// 변수 / 함수
public var somePublicVariable = 0
internal let someInternalConstant = 0
fileprivate func someFilePrivateFunction() {}
private func somePrivateFunction() {}


// 아무것도 붙이지 않으면?
class SomeInternalClass1 {}         // 암시적인 internal 선언
let someInternalConstant1 = 0
```

### 실무에서 사용하는 관습적인 패턴
> 실제 프로젝트에서 많이 사용하는 관습적인 패턴
```swift
// 속성(변수)를 선언시 private으로 외부에 감추려는 속성은 _(언더바)를 사용해서 이름 지음
class SomeOtherClass {
    private var _name = "이름"         // 쓰기 - private
    var name: String {                // 읽기 - internal
        return _name
    }
    func changeName(name: String) {
	    self._name = name
    }
}

// 저장속성의 (외부에서) 쓰기를 제한하기 ⭐️
class SomeAnotherClass {
    private(set) var name = "이름"      // 읽기 - internal / 쓰기 - private
}
```
- 쓰기를 할 경우 메서드를 선언해서 사용해야함
- 이제는 보통 `private(set)`으로 많이 사용함. 

## 커스텀 타입의 접근 제어
> 타입의 내부 멤버는 타입 자체의 접근 수준을 넘을 수 없음

```swift
// 명시적인 public 선언
public class SomePublicClass {
    // open 이라고 설정해도 public으로 작동 ⭐️
    open var someOpenProperty = "SomeOpen"
    public var somePublicProperty = "SomePublic"
    // 원래의 기본 수준
    var someInternalProperty = "SomeInternal"
    fileprivate var someFilePrivateProperty = "SomeFilePrivate"
    private var somePrivateProperty = "SomePrivate"
}

let somePublic = SomePublicClass()
somePublic.someOpenProperty
somePublic.somePublicProperty
somePublic.someInternalProperty
// 같은 파일 안이기 때문에 접근 가능
somePublic.someFilePrivateProperty
// 스코프 외부이기 때문에 접근 불가능
//somePublic.somePrivateProperty


// 암시적인 internal 선언
class SomeInternalClass {
	// open 이라고 설정해도 internal으로 작동 ⭐️
    open var someOpenProperty = "SomeOpen"
    public var somePublicProperty = "SomePublic"
    var someInternalProperty = "SomeInternal"
    fileprivate var someFilePrivateProperty = "SomeFilePrivate"
    private var somePrivateProperty = "SomePrivate"
}


let someInternal = SomeInternalClass()
someInternal.someOpenProperty
someInternal.somePublicProperty
someInternal.someInternalProperty
someInternal.someFilePrivateProperty
//someInternal.somePrivateProperty


// 명시적인 file-private 선언
fileprivate class SomeFilePrivateClass {
    open var someOpenProperty = "SomeOpen"
    public var somePublicProperty = "SomePublic"
    var someInternalProperty = "SomeInternal"
    var someFilePrivateProperty = "SomeFilePrivate"
    private var somePrivateProperty = "SomePrivate"
}


// 변수선언(internal) <=> 타입선언(fileprivate)은 불가능 (fileprivate / private 선언가능)
//internal let someFilePrivate = SomeFilePrivateClass()
fileprivate let someFilePrivate = SomeFilePrivateClass()
// fileprivate
someFilePrivate.someOpenProperty
// fileprivate
someFilePrivate.somePublicProperty
// fileprivate
someFilePrivate.someInternalProperty
// 같은 파일 안이기 때문에 접근 가능
someFilePrivate.someFilePrivateProperty
//someFilePrivate.somePrivateProperty

// 현재의 scope에서 private
private let someFilePrivate2 = SomeFilePrivateClass()
```

> 타입 자체를 `private`으로 선언하는 것은 의미가 없어짐
> -> `fileprivate`으로 동작
```swift
// 타입을 private으로 선언하면 아무곳에서도 사용할 수 없기 때문에 의미가 없음 ⭐️

// 명시적인 private 선언
private class SomePrivateClass {
    open var someOpenProperty = "SomeOpen"
    public var somePublicProperty = "SomePublic"
    var someInternalProperty = "SomeInternal"
    // 실제 fileprivate 처럼 동작 ⭐️ (공식문서 오류)
    var someFilePrivateProperty = "SomeFilePrivate"
    private var somePrivateProperty = "SomePrivate"
}


fileprivate let somePrivate = SomePrivateClass()
somePrivate.someOpenProperty
somePrivate.somePublicProperty
somePrivate.someInternalProperty
// 같은 파일 안이기 때문에 접근 가능
somePrivate.someFilePrivateProperty
//somePrivate.somePrivateProperty

// 튜플, 함수, 열거형(원시값, 연관값)에 대한 접근제어 관련 구체적인 법칙이 있지만, 필요할때 찾아서 사용
```

## 내부 멤버 (Nested Type)의 접근 제어 수준
> 내부 멤버가 명시적 선언을 하지 않는다면, 접근 수준은 `internal`로 유지
```swift
open class SomeClass {
    var someProperty = "SomeInternal"
    // internal 임 ➞ 클래스와 동일한 수준을 유지하려면 명시적으로 open선언 필요
}
```
- 타입의 접근 수준이 높다고, 내부 멤버의 접근 수준이 무조건 따라서 높아지는 것 아님

## 상속과 확장의 접근 제어
> 상속 관계(Subclassing)의 접근 제어

```swift
public class A {
    fileprivate func someMethod() {}
}

// public 이하의 접근 수준만 가능(public/internal/fileprivate)
internal class B: A {
	// 접근 수준 올려서 재정의 가능 ⭐️
    override internal func someMethod() {
	    // (더 낮아도) 모듈에서 접근가능하기 때문에 호출 가능
        super.someMethod()
    }
}
```
- 타입 관련: 상속해서 만든 서브클래스는 상위클래스보다 더 높은 접근 수준을 가질 수는 없음
- 멤버 관련: 동일 모듈에서 정의한 클래스의 상위 멤버에 **접근 가능하면**, 접근 수준 올려서 재정의(`override`)도 가능 -> 호출 가능하기 때문

### 확장(Extension)의 접근 제어
> 기본법칙 - 원래 본체와 동일한 접근 수준을 유지하고, 본체의 멤버에는 기본적인 접근 가능
```swift
public class SomeClass {
    private var somePrivateProperty = "somePrivate"
}

extension SomeClass {   // public으로 선언한 것과 같음
    func somePrivateControlFunction() {
        somePrivateProperty = "접근가능"
    }
}
```
- 같은 본체로 인식하기 때문에 `private`에도 접근 가능

## 속성과 접근 제어
> 속성의 읽기 설정(getter)과 속성의 쓰기 설정(setter)의 접근 제어
> - 저장, 계산 속성의  읽기와 쓰기의 접근 제어 수준을 구분해서 구현 가능
- **일반적으로 밖에서 쓰는 것(setter)은 불가능하도록 구현하는 경우가 많음**

```swift
struct TrackedString {
	// 외부에서도 변경 가능해서 위험함
    //var numberOfEdits = 0        
    // 이렇게 선언하면, 읽기도 불가능해서 불편함          
    //private var numberOfEdits = 0
    
    // setter에 대해서만 private 선언 ⭐️
    private(set) var numberOfEdits = 0
    //internal private(set) var numberOfEdits = 0 이것과 같음
    
    // 속성 관찰자
    var value: String = "시작" {
        didSet {
            numberOfEdits += 1
        }
    }
}

var stringToEdit = TrackedString()
stringToEdit.value = "첫설정" // 1
stringToEdit.value += " 추가하기1" // 2
stringToEdit.value += " 추가하기2" // 3
stringToEdit.value += " 추가하기3" // 4
print("수정한 횟수: \(stringToEdit.numberOfEdits)") // 4
print(stringToEdit.value) // 첫설정 추가하기1 추가하기2 추가하기3

// 외부에서 직접설정하는 것은 불가능 (읽는 것은 가능) ⭐️
//stringToEdit.numberOfEdits = 3
```
- 속성의 읽기설정과 속성의 쓰기설정에 대해 각각 명시적으로 선언도 가능
- 변수 및 속성, 서브스크립트에 쓰기(setter)수준을 읽기(getter)수준 보다 낮은 접근 수준으로 설정 가능
- 저장속성/계산속성 모두에 설정 가능
- **`private(set)`는 중요하고 자주 쓰임**