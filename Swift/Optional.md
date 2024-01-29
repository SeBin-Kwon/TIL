# 옵셔널 (Optional)
> 값이 있을 수도, 없을 수도 있다.

값이 있을 수도 있고 없을 수도 있는 변수를 정의할 때, 타입 바로 뒤에 `?`를 붙여 정의한 변수를 **옵셔널(Optional)**이라고 한다.

## 왜 써야하는가?

- `nil`이 들어올 수도 있는, `nil`의 가능성을 코드만으로 표현이 가능하다.
	
    - 문서/주석 작성 시간을 절약해준다.
    
- 전달받은 값이 옵셔널이 아니라면 `nil` 체크를 하지 않고 사용할 수 있다.
	
    - 효율적인 코딩을 할 수 있다.
    - 예외 상황을 최소화 하는 안전한 코딩을 할 수 있다.

## 사용 방법

- 옵셔널에 초기값을 지정하지 않으면 기본값은 `nil` 이다.

```swift
var email: String?
print(email) // nil

email = "sbkwon98@gmail.com"
print(email) // Optional("sbkwon98@gmail.com")
```

- 옵셔널로 정의한 변수는 일반적인 변수와는 다르므로 일반적인 변수에 대입할 수 없다.

```swift
let optionalEmail: String? = "sbkwon98@gmail.com"
let requiredEmail: String = optionalEmail // 컴파일 에러
```
`requiredEmail`은 옵셔널이 아닌 `String`이므로 **항상 값을 가지고 있어야 한다.** 하지만 `optionalEmail`은 옵셔널이므로 **값이 없을 수도 있기 때문에** `requiredEmail`에는 옵셔널을 대입할 수 없다.

# Optional Unwrapping

## 옵셔널 바인딩 (Optional Binding)
> 옵셔널의 값을 꺼내오는 방법 중 하나

- `nil` 체크와 동시에 안전한 값을 추출할 수 있다.

- `if let` 또는 `if var`를 사용하여 옵셔널 값이 있다면 if문에 들어가고, 값이 `nil`이라면 그냥 통과한다.

- if문에서 `,`콤마로 구분하여 여러 옵셔널을 바인딩할 수 있다.
**사용한 모든 옵셔널 값이 존재해야 if문 안에 진입한다.**

### if-let

```swift
let optionalEmail: String? = "sbkwon98@gmail.com"

if let email = optionalEmail {
  print(email) // optionalEmail 값이 있다면 출력됨.
}
// 없다면 그냥 통과됨.

var optionalName: String? = "전수열"
var optionalEmail: String? = "devxoul@gmail.com"

if let name = optionalName, email = optionalEmail {
  // name과 email 값이 존재
}

// 코드가 너무 길 땐 여러 줄에 걸쳐서 작성하는 편이 바람직하다.
if let name = optionalName,
  let email = optionalEmail {
  // name과 email 값이 존재
}

```

## 강제 추출 (Force Unwrapping)

### 암시적 추출 옵셔널 (Implicitly Unwrapped Optional)

> `?` 대신 `!`를 사용하면 옵셔널 바인딩을 하지 않아도 값에 바로 접근할 수 있다.

**값이 없는데 접근을 시도하면 런타임 에러가 발생**하고 런타임 에러가 발생하면 iOS 앱은 강제로 종료된다.
그래서 가급적이면 **일반적인 옵셔널을 사용해서 정의하고, 옵셔널 바인딩 또는 옵셔널 체이닝을 통해 값에 접근하는 것**이 더 바람직하다.

```swift
func printName(_ name: String) {
	print(name)
}

var myName: String? = "sebin"

printName(myName!)
// sebin

myName = nil
printName(myName!)
// 강제 추출 시 값이 없으므로 런타임 오류 발생

var yourName: String! = nil
printName(yourName)
// nil 값이 전달되기 때문에 런타임 오류 발생
```

> Swift 3 버전부터 `"\(email)"`과 같이 문자열 포맷팅할 때, 암시적 추출 옵셔널과 일반 옵셔널을 거의 동일하게 취급해서 `sbkwon98@gmail.com`이 아닌 `Optional("sbkwon98@gmail.com")`로 포맷팅이 되니 주의해야 한다.

## 옵셔널 체이닝(Optional Chaining) 문법
> 옵셔널 타입에 `.` 접근 연산자를 사용할 때, `nil`일수도 있음을 알리기 위해서 반드시 앞에 `?`를 붙여야함

```swift
class Dog {
    var name: String?
    var weight: Int
    init(name: String, weight: Int) {
        self.name = name
        self.weight = weight
    }
    func sit() {
        print("\(self.name)가 앉았습니다.")
    }
    func layDown() {
        print("누웠습니다.")
    }
}

class Human {
    var dog: Dog?
}

var human = Human()
human.dog = choco
human.dog?.name
print(human.dog?.name)     // Optional("초코얌")

var human2: Human? = Human()
human2?.dog = choco
human2?.dog?.name
print(human2?.dog?.name)      // Optional("초코얌")
```
- **옵셔널 체이닝의 결과는 항상 옵셔널이다.** 
- 옵셔널체이닝에 값 중에서 하나라도 nil을 리턴한다면, 이어지는 표현식을 평가하지 않고 nil을 리턴
- 마지막은 옵셔널이어도 `?`를 안붙여도 된다. 하지만 앞부분이 옵셔널이라면 반드시 붙여야 한다.

### 옵셔널 체이닝 Unwrapping
```swift
// 1) 앞의 옵셔널타입에 값이 있다는 것이 확실한 경우
print(human2!.dog!.name)     // name 자체가 옵셔널타입이기 때문에 Optional("초코얌")
print(human2!.dog!.name!)
print(human2!.dog!.weight)   // weight 자체는 옵셔널타입이 아니기 때문에   15

// 2) if let 바인딩
if let name = human2?.dog?.name {    // Optional("초코얌")
    print(name)                      // 초코얌
}

// 3) Nil-Coalescing 연산자
var defaultName = human2?.dog?.name ?? "멍탱구리"
print(defaultName)
```
- Nil-Coalescing 연산자는 기본값을 부여함으로써 if let 바인딩과 같은 효과이다.

### 함수 관련 표기법
```swift
class Cat {
    var name: String?
    var myMaster: (() -> Person?)?
    // 함수를 변수에 저장하므로 @escaping 키워드가 필요함.
    init(aFunction: @escaping () -> Person?) {
        self.myMaster = aFunction
    }
}

class Person {
    var name: String?
}

// 함수를 정의
func meowmeow() -> Person? {
    let person = Person()
    person.name = "Jobs"
    return person
}

var cat: Cat? = Cat(aFunction: meowmeow) // 정의한 함수를 할당
var name = cat?.myMaster?()?.name
print(name) // Optional("Jobs")
```
- `cat?.myMaster?()?.name`
	- `cat?` : `Cat`이 없을 수도 있음.
	- `myMaster?` : `myMaster`함수가 없을 수도 있음.
	- `myMaster?()?`: `myMaster`함수의 결과값 `Person`이 없을 수도 있음.

### 딕셔너리 관련 표기법
```swift
class Library1 {
    var books: [String: Person]?
}

var person1 = Person()
person1.name = "Jobs"
print(person1.name)

var person2 = Person()
person2.name = "Musk"
print(person2.name)

var library = Library1()
library.books = ["Apple": person1, "Tesla": person2]

library.books?["Apple"]?.name
library.books?["Tesla"]?.name
```
- `books?` : 딕셔너리 자체가 없을 수도 있음.
- `books?["Apple"]?` : 딕셔너리의 결과값이 없을 수도 있음.
	- **딕셔너리는 접근할 때 항상 옵셔널임**

### 옵셔널 체이닝에서 함수의 실행
> 옵셔널 타입에 접근해서 실행하는 함수는 그냥 실행됨. 앞의 타입을 벗기지 않아도 된다.

```swift
var bori: Dog? = Dog(name: "보리", weight: 20)

bori?.layDown()  // 앞의 타입이 옵셔널이라고 해서 메서드가 실행이 안되는 것은 아님
bori?.sit()  // Optional("보리")가 앉았습니다.

bori = nil
bori?.layDown()     
```
1. 함수가 리턴형이 없는 경우
	- 타입에 값이 있으면 함수 실행
	- 타입에 값이 없으면 nil
2. 함수가 리턴형이 있는 경우
	- 타입에 값이 있으면 **옵셔널 리턴 타입으로 반환 (원래 리턴형이 옵셔널이 아니더라도)**
	- 타입에 값이 없으면 nil