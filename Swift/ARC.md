# 메모리 관리

## 값 형식과 참조 형식
> 참조 형식은 메모리 관리가 필요하다.

|                       | 값 형식 Value Type                                          | 참조 형식 Reference Type                                     |
| --------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| 메모리 상의 저장 위치 | 메모리의 값이 복사되어 전달<br>값의 저장: **Stack**         | 메모리의 주소를 전달<br>값의 저장: **Heap**<br>주소 저장: **Stack** |
| 메모리 관리 방식      | 값이 들어있는 스택의 스코프가 종료되면 **자동 제거**        | **ARC 모델 :** **RC(Reference Counting)**을 통해 메모리 관리 |
| 타입 예시             | 기본 타입들(Int, String 등), tuple, Struct, enum, 컬렉션 등 | **클래스, 클로저**                                           |

## 메모리 구조

- 메모리
	- 코드(프로그램)
		- 명령어/프로그램
		- 앱의 모든 코드(Text)
	- 데이터
		- 전역 변수/ 타입(static,class)변수
		- 공통으로 공유하기 위한 데이터
		- 붕어빵 틀
		- **앱이 실행되는 동안 불변**
	- **힙**
		- **동적 할당**: 힙을 스캔 하고 비어있는 부분에 저장하는 방식
		- 일반적으로 오랫동안, 긴시간 동안 저장
		- 크기가 크고, 관리할 필요가 있는 데이터
		- 붕어빵 틀로 찍어낸 인스턴스
		- **개발자가 잘 관리해야함**
			- 힙에 할당된 데이터는 메모리에서 헤제가 되긴 하지만 만약 **해제되지 않으면 ==메모리 누수(Memory Leak) 현상 발생==**
				- 데이터가 계속 쌓여서 메모리 꽉차면 앱이 꺼지기도 함
	- 스택
		- **함수 실행을 위한 임시적 공간**
		- 크기가 작고 빠르게 사용하기 위한 데이터
		- 스택 스코프가 종료되면 데이터가 제거되면서 **알아서 자동 관리됨**

# ARC(Automatic Reference Counting)
> 스위프트의 메모리 관리 모델

RC(참조 숫자)를 세서 만약 참조하는 숫자가 0이라면 메모리 해제함
```swift
class Dog {
    var name: String
    var weight: Double
    init(name: String, weight: Double) {
        self.name = name
        self.weight = weight
    }
    deinit {
        print("\(name) 메모리 해제")
    }
}

var choco: Dog? = Dog(name: "초코", weight: 15.0)  //retain(choco)   RC: 1
var bori: Dog? = Dog(name: "보리", weight: 10.0)   //retain(bori)    RC: 1

choco = nil   // RC: 0 // 초코 메모리 해제
//release(choco)
bori = nil    // RC: 0 // 보리 메모리 해제
//release(bori)
```

- 예전 언어(C, C++)는 모든 메모리를 수동 관리 했음.
- 현대적 언어(Python, Java, Swift)는 자동 관리함.
- 컴파일시에 컴파일러가(Xcode) **메모리 관리 코드를 알아서 심어줌**, 메모리 해제 시점을 결정
	- 프로그램의 메모리 관리에 대한 안정성 증가

```swift
var dog1: Dog?
var dog2: Dog?
var dog3: Dog?


dog1 = Dog(name: "댕댕이", weight: 7.0)     // RC + 1   RC == 1
dog2 = dog1                               // RC + 1   RC == 2
dog3 = dog1                               // RC + 1   RC == 3


dog3?.name = "깜둥이"
dog2?.name // 깜둥이
dog1?.name // 깜둥이



dog3 = nil                                // RC - 1   RC == 2
dog2 = nil                                // RC - 1   RC == 1
dog1 = nil  // 깜둥이 메모리 해제             // RC - 1   RC == 0    
```

## 강한 참조 사이클과 메모리 누수
> 강한 참조 사이클이 일어나는 경우는 메모리 누수가 발생한다.

```swift
class Dog {
    var name: String
    var owner: Person?
    init(name: String) {
        self.name = name
    }
    deinit {
        print("\(name) 메모리 해제")
    }
}

class Person {
    var name: String
    var pet: Dog?
    init(name: String) {
        self.name = name
    }
    deinit {
        print("\(name) 메모리 해제")
    }
}

var bori: Dog? = Dog(name: "보리") // RC: 1
var gildong: Person? = Person(name: "홍길동") // RC: 1

// 객체 서로가 참조
bori?.owner = gildong // RC: 2
gildong?.pet = bori // RC: 2

// 아래 코드를 추가해야지만 메모리 해제 가능
// bori?.owner = nli
// gildong?.pet = nil

// 강한 참조 사이클(Strong Reference Cycle)이 일어남. 메모리 해제 안됨.
bori = nil // RC: 1
gildong = nil // RC: 1
```
- **객체가 서로를 참조하는 강한 참조 사이클**로 인해 **변수의 참조에 `nil`을 할당해도 메모리 해제가 되지 않는 메모리 누수(Memory Leak)의 상황**이 발생.

## 메모리 누수 해결 방안
### weak과 unowned 키워드
#### 공통점
- 가르키는 인스턴스의 **RC 숫자를 올라가지 않게 함** (인스턴스 사이의 강한 참조 제거)
- weak/unowned로 선언한 변수를 통해 인스턴스에 접근은 가능하지만, 인스턴스를 유지시키는 것은 불가능.

#### 차이점
**weak**
- **무조건 `var`에 옵셔널로만 선언 가능**
	- `nil`이 할당 될 수 있도록 해야하기 때문
- **`nil` 자동 할당**
- 소유자에 비해, 보다 짧은 생명주기를 가진 인스턴스를 참조할 때 주로 사용
	- 인스턴스가 `nil`로 확인 가능
	- `nil`인 경우 작업을 중단하는 것 가능
- `unowned`는 한번 더 고려해야 할 것이 있어서 **`weak`이 실제 프로젝트에서 더 많이 사용**

**unowned**
- Swift 5.3 버전 이후, 옵셔널로 선언 가능
- **`nil` 자동 할당 하지 않음**
	- 에러가 발생할 수 있어서 따로 `nil`을 할당해줘야 함
- 소유자 보다 인스턴스의 생명주기가 더 길거나, 같은 경우에 사용
	- 인스턴스가 `nil`로 확인 불가능
	- 실제 인스턴스가 해제되었다면 에러 발생
- `weak`보다 이론상 좀 더 빠름

### Weak Reference (약한 참조)

```swift
class Dog {
    var name: String
    weak var owner: Person?     // weak 키워드 ==> 약한 참조
    init(name: String) {
        self.name = name
    }
    deinit {
        print("\(name) 메모리 해제")
    }
}

class Person {
    var name: String
    weak var pet: Dog?         // weak 키워드 ==> 약한 참조
    init(name: String) {
        self.name = name
    }
    deinit {
        print("\(name) 메모리 해제")
    }
}

var bori: Dog? = Dog(name: "보리")
var gildong: Person? = Person(name: "홍길동")

// 강한 참조 사이클이 일어나지 않음
bori?.owner = gildong
gildong?.pet = bori

// 메모리 해제가 잘됨(사실 이 경우 한쪽만 weak으로 선언해도 상관없음)
bori = nil // 보리 메모리 해제
gildong = nil // 홍길동 메모리 해제
```
- 약한 참조의 경우, **참조하고 있던 인스터스가 사라지면 `nil`로 초기화 되어있음.**

```swift
gildong = nil
bori?.owner // nil
```
- `gildong`만 메모리 해제시켰음에도 `nil`로 자동 초기화 되어있다.

### Unowned Reference (비소유 참조)

```swift
class Dog1 {
    var name: String
    // Swift 5.3 이전버전에서는 비소유참조의 경우, 옵셔널 타입 선언이 안되었음
    unowned var owner: Person1?
    init(name: String) {
        self.name = name
    }
    deinit {
        print("\(name) 메모리 해제")
    }
}

class Person1 {
    var name: String
    unowned var pet: Dog1?
    init(name: String) {
        self.name = name
    }
    deinit {
        print("\(name) 메모리 해제")
    }
}

var bori1: Dog1? = Dog1(name: "보리1")
var gildong1: Person1? = Person1(name: "홍길동1")

// 강한 참조 사이클이 일어나지 않음
bori1?.owner = gildong1
gildong1?.pet = bori1
```
- 비소유 참조의 경우, **참조하고 있던 인스턴스가 사라지면 `nil`로 초기화 되지 않음.**
	- 메모리 주소가 없는데 `nil`이 아니여서 에러 발생함.

```swift
gildong1 = nil
bori1?.owner // 메모리 주소가 없는데 접근해서 에러 발생

gildong1 = nil
bori1?.owner = nil
bori1?.owner // nil
```
- 에러 발생하지 않게 하려면, **==`nil`로 재설정이 필요하다.==**

# 클로저와 메모리 관리
[[Closure]]

## 값(Value) 타입의 캡처 현상 / 캡처리스트
### 캡처
- **힙**
	- 클로저
		- 함수
		- num(변수) -> 스택 프레임에 있는 **num 변수 주소 저장** 
			- **값 타입 (참조를 캡처)**
			- 캡처리스트를 사용하지 않을 때, 변수의 주소를 캡처
```swift
var num = 1
let closure = {
	print("밸류값: \(num)")
}
```
- 클로저 외부에 존재하는 밸류 타입의 참조(변수 주소)를 캡처함
- 외부요인에 의해 값이 변했을 때도 계속 참조
### 캡처리스트
#### 값 타입에서 캡처리스트를 사용해야 하는 이유
> 값을 복사 및 캡처하여 외부적인 요인에 의한 값 변경 방지
```swift
// 파라미터가 없는 경우
let closure = {[num] in
	print("밸류값: \(num)")
}

// 파라미터가 있는 경우
let closure = {[num] (파라미터) -> 리턴형 in
	print("밸류값: \(num)")
}
```
- 클로저 외부에 존재하는 밸류 타입의 값을 복사해서 사용 **(변수 주소를 참조하는게 아닌 값을 복사함)** 
- **외부요인에 의해 해당 값의 변경을 방지할 때 사용**

## 참조(Reference) 타입의 캡처 현상 / 캡처리스트
#### 참조 타입에서 캡처리스트를 사용해야 하는 이유
> 클로저에서 약한 참조, 비소유 참조를 선언할 수 있도록 도와줌 -> 강한 참조 사이클 문제 해결 가능

```swift
class SomeClass {
    var num = 0
}

var x = SomeClass()
var y = SomeClass()

print("참조 초기값(시작값):", x.num, y.num) // 0, 0

let refTypeCapture = { [x] in
    print("참조 출력값(캡처리스트):", x.num, y.num)
}
x.num = 1
y.num = 1

print("참조 초기값(숫자변경후):", x.num, y.num) // 1, 1
refTypeCapture()                           // 1, 1     (Not) 0, 1
print("참조 초기값(클로저실행후):", x.num, y.num) // 1, 1
```
- `x` - 캡처리스트: (참조타입) 주소값 캡처, **x를 직접 참조로 가르킴**
	- 클로저 외부에 존재하는 참조 타입의 주소값을 복사해서 사용
		- 외부요인에 의해 해당 인스턴스의 해제를 방지할 때 사용
	- **==가르키는 인스턴스 RC를 올라가게 함==** -> 메모리 해제 가능성 방지
- `y` - 캡처 현상: 변수를 캡처해서, **y변수를 가르킴(간접적으로 y도 동일)**
### 강한 참조 사이클 문제 해결
> 캡처리스트 + `weak` / `unowned`

```swift
var z = SomeClass()

let refTypeCapture1 = { [weak z] in
    print("참조 출력값(캡처리스트):", z?.num)
}
refTypeCapture1() // Optional(0)

let refTypeCapture2 = { [unowned z] in
    print("참조 출력값(캡처리스트):", z.num)
}
refTypeCapture2() // 0

var s = SomeClass()

// 캡처리스트에서 바인딩 가능
// 내부에서 변수명 바꿔서 사용가능 (외부변수와 헷갈리는 것을 방지)
let captureBinding = { [z = s] in   
    print("바인딩의 경우:", z.num)
}

let captureWeakBinding = { [weak z = s] in
    print("Weak 바인딩 경우:", z?.num)
}
```
- `weak`과 `unowned`로 **가르키는 참조 타입(인스턴스)의 RC를 올라가지 않게 함**
	- `weak` - 옵셔널 타입으로 바뀜

## 일반적인 클로저의 사용 (객체 내에서 사용과 self 키워드)
> 클래스 내에 클로저가 존재하는 경우가 많음.

클로저 내에서 객체의 속성 및 메서드에 접근 시 **`self`키워드를 반드시 사용해야 함.**
- `self.name`
- `[self]` -> Swift 5.3 이후 가능
구조체는 `self` 생략 가능 -> Swift 5.3 이후 가능

```swift
class Dog {
    var name = "초코"

    func doSomething() {
        // 비동기적으로 실행하는 클로저 // 강한 참조
        DispatchQueue.global().async {
            print("나의 이름은 \(self.name)입니다.")
        }
        DispatchQueue.global().async [self] in {
            print("나의 이름은 \(name)입니다.")
        }
        // 약한 참조
        DispatchQueue.global().async [weak self] in {
            print("나의 이름은 \(self?.name)입니다.")
        }
    }
}
```
- 비동기적으로 실행 -> 2번 CPU(Thread)가 2번 스택에서 따로 실행 할 수 있도록 해줌.
- **==클로저를 객체 내에서 사용할 때는 대부분 `weak`와 함께 사용한다고 보면 됨.==**
### DispatchQueue 관련 코드
- 비동기적으로 실행하는 코드는 오래 저장할 필요가 있음 -> **힙에 저장**
	- **새로운 스택을 만들어서 실행하기 때문**
		- 덕분에 메인 Thread와 별도로 실행 가능
- **코드, 데이터, 힙 영역의 메모리는 공유되어 모든 스택이 이용할 수 있지만 스택끼리 공유 안됨.**
- 2번 Thread에서 클로저를 실행하고 일이 종료되면, 실제 힙에 저장되어 있던 클로저도 사라짐

```swift
class Person {
    let name = "홍길동"
    func sayMyName() {
        print("나의 이름은 \(name)입니다.")
    }
    func sayMyName1() {
        DispatchQueue.global().async {
            print("나의 이름은 \(self.name)입니다.")
        }
    }
    func sayMyName2() {
        DispatchQueue.global().async { [weak self] in
            print("나의 이름은 \(self?.name)입니다.")
        }
    }
    func sayMyName3() {
        DispatchQueue.global().async { [weak self] in
            guard let weakSelf = self else { return }   // 가드문 처리 ==> 객체없으면 일종료
            print("나의 이름은 \(weakSelf.name)입니다.(가드문)")
        }
    }
}

let person = Person()
person.sayMyName()
person.sayMyName1()
person.sayMyName2() // 옵셔널(홍길동)
person.sayMyName3()
```
- 보통 `weak`을 사용하고 `weak`을 사용하면 옵셔널 타입이 되기 때문에 **`guard let` 구문을 많이 사용한다.**

# 메모리 누수(Memory Leak)의 사례
> 강한 참조 사이클로 인한 메모리 누수의 사례

```swift
class Dog {
    var name = "초코"
    var run: (() -> Void)?
    func walk() {
        print("\(self.name)가 걷는다.")
    }
    func saveClosure() {
        // 클로저를 인스턴스의 변수에 저장
        run = {
            print("\(self.name)가 뛴다.")
        }
    }
    deinit {
        print("\(self.name) 메모리 해제")
    }
}

func doSomething() {
    let choco: Dog? = Dog()
    choco?.saveClosure()  // 강한 참조사이클 일어남 (메모리 누수가 일어남)
}

doSomething()
```
- `doSomething()` 로컬 함수 안에 `Dog` 인스턴스 생성, `choco`라는 변수에 할당
	- 인스턴스 RC: 1
- `saveClosure()`를 통해 클로저를 `Dog` 인스턴스의 속성 `run`에 저장함, 클로저는 힙에 유지
	- 인스턴스 RC: 2, 클로저 RC: 1
- **인스턴스의 속성 `run`에는 클로저 주소(`var run`)를, 클로저에는 인스턴스 주소(`self.name`)를 담아 서로 가리킴**
	- **강한 참조 사이클**
- `doSomething()` 함수가 종료되어 `choco` 변수가 사라짐 
	- 인스턴스 RC: 1, 클로저 RC: 1
- 하지만 인스턴스와 클로저는 사라지지 않고 서로를 가리키며 **메모리 누수를 일으킴.**

#### 해결 방법: 캡처리스트 + `weak` 또는 `unowned`
```swift
func saveClosure() {
        run = { [weak self] in
            print("\(self?.name)가 뛴다.")
        }
    }
```
- `saveClosure()`를 통해 클로저를 `choco` 인스턴스의 속성 `run`에 저장함, 클로저는 힙에 유지
- 하지만 `weak`로 RC를 카운팅하지 않는다.
	- 인스턴스 RC: 1, 클로저 RC: 1

## 캡처리스트 실제 사용예시
> 강한 참조(Strong Reference)의 경우
- 강한 참조 사이클은 일어나지 않지만, 강한 참조는 일어나기 때문에 생각해 볼 부분이 있음.
```swift
class ViewController: UIViewController {
    var name: String = "뷰컨"
    func doSomething() {
        DispatchQueue.global().async {
            sleep(3)
            print("글로벌큐에서 출력하기: \(self.name)")
        }
    }
    deinit {
        print("\(name) 메모리 해제")
    }
}

func localScopeFunction() {
    let vc = ViewController()
    vc.doSomething()
}   // 이 함수는 이미 종료 ==> vc변수 없음

localScopeFunction()
// (3초후)
// 글로벌큐에서 출력하기: 뷰컨
// 뷰컨 메모리 해제
```
- `ViewController` 인스턴스 생성, `vc` 변수에 할당, `doSomething()` 실행
	- 인스턴스 RC: 1
- `DispatchQueue` 클로저 실행, 힙에 저장 후 다른 쓰레드에서 동작, `sleep(3)`으로 CPU 3초간 멈춤
	- **클로저는 힙에 남아 인스턴스 주소 가르킴**
		- 인스턴스 RC: 2
	- 메인 쓰레드에서 실행되던 `doSomething()`는 이미 종료, `vc` 변수 없어짐
		- 하지만 클로저에 의해 인스턴스는 남아있음.
		- 인스턴스 RC: 1
- `print()`에서 **인스턴스 `name` 속성의 값 `"뷰컨"`을 출력**, 클로저 종료 및 없어짐
	- 클로저가 사라지며 인스턴스 메모리 해제
	- 인스턴스 RC: 0

> 약한 참조(Weak Reference)의 경우
```swift
class ViewController1: UIViewController {
    var name: String = "뷰컨"
    func doSomething() {
        // 강한 참조 사이클이 일어나지 않지만, 굳이 뷰컨트롤러를 길게 잡아둘 필요가 없다면
        // weak self로 선언
        DispatchQueue.global().async { [weak self] in
            //guard let weakSelf = self else { return }
            sleep(3)
            print("글로벌큐에서 출력하기: \(self?.name)")
        }
    }
    deinit {
        print("\(name) 메모리 해제")
    }
}

func localScopeFunction1() {
    let vc = ViewController1()
    vc.doSomething()
}

localScopeFunction1()
// 뷰컨 메모리 해제
// (3초후)
// 글로벌큐에서 출력하기: nil
```
- `ViewController` 인스턴스 생성, `vc` 변수에 할당, `doSomething()` 실행
	- 인스턴스 RC: 1
- `DispatchQueue` 클로저 실행, 힙에 저장 후 다른 쓰레드에서 동작, `sleep(3)`으로 CPU 3초간 멈춤
	- **클로저는 힙에 남아 인스턴스 주소 가르키지만, `weak`으로 인해 RC를 카운팅 하지 않음**
		- 인스턴스 RC: 1
	- 메인 쓰레드에서 실행되던 `doSomething()`는 이미 종료, `vc` 변수 없어짐
		- 인스턴스 RC: 0
	- 인스턴스를 가리키는게 없기 때문에 **인스턴스 메모리 해제 및 `deinit`이 실행**
- 인스턴스가 없기 때문에 `print()`에서 **`nil`을 출력**, 클로저 종료 및 없어짐