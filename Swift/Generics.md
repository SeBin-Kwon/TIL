# 제네릭 문법

### 제네릭(Generics) 문법의 필요성
> 단순히 인풋 타입만 다르고 구현 내용은 완전히 동일한데.. 굳이 코드를 반복해야 할까?
```swift
let numbers = [2, 3, 4, 5]
let scores = [3.0, 3.3, 2.4, 4.0, 3.5]
let people = ["Jobs", "Cook", "Musk"]

// 출력하는 함수 만들기 => 각 케이스(타입)마다 필요한 함수를 만들어야함
func printIntArray(array: [Int]) {
    for number in array {
        print(number)
    }
}

func printDoubleArray(array: [Double]) {
    for number in array {
        print(number)
    }
}

func printStringArray(array: [String]) {
    for number in array {
        print(number)
    }
}

printIntArray(array: numbers)
printDoubleArray(array: scores)
printStringArray(array: people)
```
- 제네릭이 없다면 함수를 타입마다 모든 경우를 다 정의해야 한다.
- **제네릭은 형식에 관계없이, 한번의 구현으로 모든 타입을 처리하여 타입에 유연한 함수 작성 가능**
	- 유지보수 / 재사용성 증가
- 함수 뿐만 아니라 구조체, 클래스, 열거형도 제네릭으로 일반화 가능

## 제네릭 함수의 정의

```swift
// 파라미터의 타입에 구애받지 않는 일반적인(제네릭) 타입을 정의
func swapTwoValues<T>(_ a: inout T, _ b: inout T) { // 플레이스홀더의 역할(표시 역할일뿐) (같은 타입이어야함)
    let tempA = a
    a = b
    b = tempA
}

var num1 = 10
var num2 = 20
var string1 = "hello"
var string2 = "world"

// 같은 타입이라면, 어떠한 값도 전달 가능 해짐
swapTwoValues(&num1, &num2)
swapTwoValues(&string1, &string2) 
```
- 함수명 옆에 `< >`를 넣고 안에 타입 파라미터를 작성한다. (플레이스 홀더 역할)
	- 대문자 아무 단어나 넣으면 된다. 관습적으로 `T`를 사용한다.(Type을 의미)
	- 함수 내부에서 파라미터 형식이나 리턴형, 내부 변수 타입으로 사용됨.
- `<T, U>`, `<A, B>` 이렇게 타입파라미터를 2개 이상도 선언 가능
##### `inout` 키워드
> 기본적으로 상수인 함수의 파라미터 값을 변경하고 싶을 때 사용
```swift
func addOne(num: Int) -> Int {
    return num + 1
}

var myNum = 5
let result = addOne(num: myNum)
print(myNum)    // 출력: 5
print(result)   // 출력: 6

func addOne(inout num: Int) {
    num += 1
}

var myNum = 5
addOne(num: &myNum)
print(myNum)    // 출력: 6
```
- `inout`을 통해 전달인자의 메모리 주소를 전달하여 직접 값을 변경한다.
- 함수를 호출 할 때 파라미터 앞에 `&`를 붙여 해당 파라미터의 참조를 전달해야 한다.

### 사용 예시
> 스위프트에서 컬렉션은 모두 구조체의 제네릭 타입으로 구현되어 있음
```swift
// 배열 타입
let array1: [String] = ["Steve", "Allen"]
let array2: Array<String> = ["Cook", "Musk"]

// 딕셔너리 타입
let dictType1: [String: Int] = ["Steve": 20, "Paul": 24]
let dictType2: Dictionary<String, Int> = ["Alex": 25, "Michel": 18]

// 옵셔널 타입
var optionalType1: String?
var optionalType2: Optional<String>
```

## 제네릭 타입의 정의
> 제네릭(Generics) 구조체 / 클래스 / 열거형
- 클래스, 구조체를 정의하는 데, 안의 멤버 변수들은 여러가지 타입을 가질 수 있는 가능성이 있을 것 같다면? -> 제네릭으로 정의하기
```swift
// 구조체로 제네릭의 정의하기
struct Member {
    var members: [String] = []
}

struct GenericMember<T> {
    var members: [T] = []
}

var member1 = GenericMember(members: ["Jobs", "Cook", "Musk"])
var member2 = GenericMember(members: [1, 2, 3])

// 클래스로 제네릭의 정의하기
class GridPoint<A> {
    var x: A
    var y: A
    
    init(x: A, y: A){
        self.x = x
        self.y = y
    }
}

let aPoint = GridPoint(x: 10, y: 20)
let bPoint = GridPoint(x: 10.4, y: 20.5)

// 열거형에서 연관값을 가질때 제네릭으로 정의가능
// (어차피 케이스는 자체가 선택항목 중에 하나일뿐(특별타입)이고, 그것을 타입으로 정의할 일은 없음)
enum Pet<T> {
    case dog
    case cat
    case etc(T)
}

let animal = Pet.etc("고슴도치")
```
- 인스턴스로 찍어낸 경우, 타입이 정해진 것이므로 다른 타입으로 재할당은 불가능해진다.

## 제네릭(Generics) 구조체의 확장
```swift
// 정의
struct Coordinates<T> {
    var x: T
    var y: T
}

// 제네릭을 Extension(확장)에도 적용할 수 있다. (확장 대상을 제한하는 것도 가능은 함)
extension Coordinates {     // Coordinates<T> (X)
    // 튜플로 리턴하는 메서드
    func getPlace() -> (T, T) {
        return (x, y)
    }
}

let place = Coordinates(x: 5, y: 5)
print(place.getPlace())

// where절 추가도 가능
// Int타입에만 적용되는 확장과 getIntArray() 메서드
extension Coordinates where T == Int {     // Coordinates<T> (X)
    // 튜플로 리턴하는 메서드
    func getIntArray() -> [T] {
        return [x, y]
    }
}

let place2 = Coordinates(x: 3, y: 5)
place2.getIntArray()

//let place3 = Coordinates(x: 3.5, y: 2.5)
//place3.getIntArray()
```
- 확장에는 `< >`를 사용하지 않는다.
- `where`로 조건을 추가하면 해당 타입에만 적용시킬 수 있다.

## 타입 제약 (Type Constraint)
> 제네릭에서 타입을 제약할 수 있음.
- 타입 매개 변수 이름 뒤에 콜론으로 "프로토콜" 제약 조건 또는 "단일 클래스"를 배치 가능
	- 프로토콜 제약 `<T: Equatable>`
	- 클래스 제약 `<T: SomeClass>`
```swift
// Equatable 프로토콜을 채택한 타입만 해당 함수에서 사용 가능 하다는 제약
func findIndex<T: Equatable>(item: T, array:[T]) -> Int? {     
// <T: Equatable>
    for (index, value) in array.enumerated() {
        if item == value {
            return index
        }
    }
    return nil
}

let aNumber = 5
let someArray = [3, 4, 5, 6, 7]

if let index = findIndex(item: aNumber, array: someArray) {
    print("밸류값과 같은 배열의 인덱스: \(index)")
}
// 밸류값과 같은 배열의 인덱스: 2
```
- `Equatable` : `==`을 사용하여 비교할 수 있게 하는 프로토콜
- `<T: Equatable>` 해당 프로토콜을 채택한 타입만 사용 가능 하다는 뜻

```swift
// 클래스 제약의 예시
class Person {}
class Student: Person {}

let person = Person()
let student = Student()

// 특정 클래스와 상속관계에 내에 있는 클래스만 타입으로 사용할 수 있다는 제약  (구조체, 열거형은 사용 못함)
// (해당 타입을 상속한 클래스는 가능)
func personClassOnly<T: Person>(array: [T]) {
    // 함수의 내용 정의
}

personClassOnly(array: [person, person])
personClassOnly(array: [student, student])
personClassOnly(array: [Person(), Student()])
```
- `Person`의 상속 구조에 속해 있는 타입만 해당 함수를 사용할 수 있다는 뜻

### 반대로 구체/특정화(specialization) 함수 구현도 가능
> 항상 제네릭을 적용시킨 함수를 실행하면 불편하지 않을까?
- 제네릭 함수가 존재하더라도 **동일한 함수명에 구체적인 타입을 명시하면, 해당 구체적인 타입의 함수가 실행됨.**
```swift
func findIndex(item: String, array:[String]) -> Int? {
    for (index, value) in array.enumerated() {
        if item.caseInsensitiveCompare(value) == .orderedSame {
            return index
        }
    }
    return nil
}

let aString = "jobs"
let someStringArray = ["Jobs", "Musk"]

if let index2 = findIndex(item: aString, array: someStringArray) {
    print("문자열의 비교:", index2)
}
```
- 제네릭 함수를 호출하려 해도 파라미터로 문자열을 넣으면 해당 문자열 함수를 호출한다.

## 프로토콜에서의 제네릭 문법의 사용
> Associated Types (연관 타입)
- 프로토콜에서 제네릭을 사용하면 타입을 명시하지 않아도 된다.
```swift
protocol RemoteControl { // <T>의 방식이 아님
    associatedtype T     // 연관형식은 대문자로 시작해야함(UpperCamelcase)
    func changeChannel(to: T) // 관습적으로 Element를 많이 사용
    func alert() -> T?
}

// 연관형식이 선언된 프로토콜을 채용한 타입은, typealias로 실제 형식을 표시해야함
struct TV: RemoteControl {
    typealias T = Int       // 생략 가능
    func changeChannel(to: Int) {
        print("TV 채널바꿈: \(to)")
    }
    func alert() -> Int? {
        return 1
    }
}

class Aircon: RemoteControl {
    // 연관형식이 추론됨
    func changeChannel(to: String) {
        print("Aircon 온도바꿈: \(to)")
    }
    func alert() -> String? {
        return "1"
    }
}

```
- **`<T>`가 아니라 `associatedtype T` 이런 식으로 정의해야 한다.**
- `typealias`으로 타입명을 바꿀 수 있다.
	- 구체적으로 무슨 타입을 쓸건지 `typealias`를 통해 명시할 수 있다.
	- 요구사항들을 통해 연관형식을 추론할 수 있기 때문에 생략 가능하다.
- 요구사항 구현할 때 구체적 타입을 써야한다.
- 애플에서는 관습적으로 `Element`라는 타입명을 사용한다.

### 연관 형식에 제약 추가
```swift
protocol RemoteControl2 {
    associatedtype Element: Equatable // <T: Equatable> 제약조건 추가
    func changeChannel(to: Element)
    func alert() -> Element?
}
```