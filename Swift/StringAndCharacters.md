# 문자열과 문자 (String and Characters)

## 문자열의 기본 다루기
> 멀티라인 스트링 리터럴 (Multiline String Literals)
- 문자열을 한 줄에 입력 -> 명시적인 줄바꿈이 불가능
- 줄바꿈을 원하면, `\n` 입력   `\ (Escape character)`
#### 문자열을 여러줄 입력하고 싶을때
- `"""` (쌍따옴표 3개를 연속으로 붙여서 입력) - 첫째줄/마지막줄에 입력
- 해당 줄에는 문자열 입력 불가
- 문자열 내부에서 쓰여진대로 줄바꿈됨.
- 줄바꿈 하지 않으려면 `\`(백슬레시) 입력
- 특수문자는 문자 그대로 입력됨
- 마지막(`"""`)는 들여쓰기의 기준의 역할
```swift
let singleLineString = "These are \nthe same."
print(singleLineString)
// These are
// the same.

let quotation = """
The White Rabbit put on his spectacles.  "Where shall I begin,
please your Majesty?" he asked.

"Begin at the beginning," the King said gravely, "and go on
till you come to the end; then stop."
"""
print(quotation)
```

### 문자열 내에서 특수문자 (Escape sequences)
> Escape character sequences
> - `\0`  (null문자)
> - `\\`  (백슬레시)
> - `\t`  (탭)
> - `\n`  (줄바꿈 - 개행문자)
> - `\r`  (캐리지 리턴 - 앞줄이동)
> - `\"`  (쌍따옴표)
- `\'` (작은따옴표)
- `\u{유니코드값}`   (1~8자리의 16진수)

### 로스트링 (Raw String) - 확장 구분자 (Extended String Delimiters) `#`
> 샵 기호 (`#`)로 문자열 앞뒤를 감싸면 내부의 문자열을 글자 그대로 인식
```swift
var name = #""Steve""#
print(name) 
// "Steve"

// 특수문자가 그대로 인식됨
let string1 = #"Line 1\nLine 2"# 
print(string1) 
// Line 1\nLine 2

let string2 = #"Line 1\#nLine 2"#
print(string2)
// Line 1
// Line 2

// 샵의 갯수를 개발자 임의로 조절 가능
let string3 = ###"Line 1\###nLine 2"###
print(string3)
// Line 1
// Line 2

// 이스케이프 시퀀스 효과를 사용하려면, 샵을 입력
let string4 = #"My name is \#(name)"#

let threeMoreDoubleQuotationMarks = #"""
Here are three more double quotes: """
"""#
print(threeMoreDoubleQuotationMarks)
// Here are three more double quotes: """
```

## 문자열 보간법 (String Interpolation)
> 문자열 보간법의 동작원리
> - 문자열 내에서  `"\(표현식 등)"`
- 상수, 변수, 리터럴값, 그리고 표현식의 값을 표현가능
```swift
let multiplier = 3
let message = "\(multiplier) times 2.5 is \(Double(multiplier) * 2.5)"
print(message)
// 3 time 2.5 is 7.5

struct Dog {
    var name: String
    var weight: Double
}

let dog = Dog(name: "초코", weight: 15.0)
print("\(dog)")
print(dog)
// Dog(name: "초코", weight: 15.0)  출력 형태를 애플이 지정해 놓음
// Dog(name: "초코", weight: 15.0)
```
- `print()`대신 `dump()` 사용시 좀 더 자세하게 출력 가능
	- 문자열 보간법을 사용하면 그대로임
### 출력 형태(방법)을 직접 구현 가능
> `CustomStringConvertible` 프로토콜을 채택해서 구현하면 스트링 인터폴레이션을 직접 구현 가능
```swift
protocol CustomStringConvertible {
      var description { get }
}

extension Dog: CustomStringConvertible {
    var description: String {
        return "강아지의 이름은 \(name)이고, 몸무게는 \(weight)kg 입니다."
    }
}
print("\(dog)")
print(dog)
// 강아지의 이름은 초코이고, 몸무게는 15.0kg 입니다.
// 강아지의 이름은 초코이고, 몸무게는 15.0kg 입니다.
```
- `\()` 는 `description` 변수를 읽어서 출력하는 것이다.

### Swift 5에서의 문자열 보간법의 동작원리
> 각자의 타입에 구현하는 게 아니라 문자열 자체에다가 메서드를 구현하는 방식이다.
- 메서드로 바뀌면서 활용도가 높아짐 (다른 파라미터 지정 가능)
```swift
struct Point {
    let x: Int
    let y: Int
}

let p = Point(x: 5, y: 7)
print("\(p)")

extension String.StringInterpolation {
    mutating func appendInterpolation(_ value: Point) {
        appendInterpolation("X좌표는 \(value.x), Y좌표는 \(value.y)입니다.")
    }
	mutating func appendInterpolation(_ value: Dog) {
        appendInterpolation("강아지의 이름은 \(value.name), 몸무게는 \(value.weight)키로 입니다.")
    }
}

print("\(p)")
print("\(dog)")
// X좌표는 5, Y좌표는 7입니다.
// 강아지의 이름은 초코, 몸무게는 15.0키로 입니다.
```
- `\()`는 `appendInterpolation()`를 실행하는 것이다.

```swift
extension String.StringInterpolation {

    mutating func appendInterpolation(_ value: Point, style: NumberFormatter.Style) {
        
        // "숫자" <====> "문자" 변환을 다루는 객체
        let formatter = NumberFormatter()
        formatter.numberStyle = style

        // 지정된 스타일로 문자열을 구성
        if let x = formatter.string(for: value.x), let y = formatter.string(for: value.y) {
            appendInterpolation("X좌표는 \(x) x Y좌표는 \(y)")
        }else  {
            appendInterpolation("X좌표는\(value.x) x Y좌표는\(value.y)")
        }
    }
}

print("\(p)")
print("\(p, style: .spellOut)")     // X좌표는 five x Y좌표는 seven
print("\(p, style: .percent)")      // X좌표는 500% x Y좌표는 700%
print("\(p, style: .scientific)")   // X좌표는 5E0 x Y좌표는 7E0
```
- `String.StringInterpolation`을 확장하고 `appendInterpolation`을 구현해주면 된다.

## 숫자(정수/실수) 등을 문자열로 변환 출력 할 때
> 변수/표현식 등을 포함, 반올림의 구현

### 출력 형식 지정자(Format Specifiers)
```swift
var string: String = ""

string = String(3.1415926)
// 3.1415926

// 반올림
string = "원하는 숫자는 " + String(format: "%.3f", pi)
// 원하는 숫자는 3.142

string = "원하는 숫자는 " + String(format: "%.2f", pi)
// 원하는 숫자는 3.14

string = "원하는 숫자는 " + String(format: "%.1f", pi)
// 원하는 숫자는 3.1

// %.2f 자리에 pi를 대체
string = String(format: "원하는 숫자는 %.2f", pi)
// 원하는 숫자는 3.14
```

#### 출력 형식 지정자(Format Specifiers)의 종류
```swift
// %d, %D -> 정수
string = String(format: "%d", 7)
// 7

// 두자리로 표현
string = String(format: "%2d", 7)
//  7

// 두자리로 표현하되, 0포함
string = String(format: "%02d", 7)
// 07

// 일곱자리로 표현하되 0과 .(dot) 포함, (소수점아래는 3자리)
string = String(format: "%07.3f", pi)
// 003.142

// %@ -> 문자열
var swift = "Swift"
string = String(format: "Hello, %@", swift)
// Helle, Swift
```
- [참고](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265-SW1)

#### 형식 지정자 활용 예시
```swift
// CustomStringConvertible과 결합해서 사용해보기
struct Point: Codable {
    var x: Double
    var y: Double
}

extension Point: CustomStringConvertible {
    var description: String {
        let formattedValue = String(format: "%1$.2f , %2$.2f", self.x, self.y)
        //let formattedValue = String(format: "%.2f", x) + " , " + String(format: "%.2f", y)
        return "\(formattedValue)"
    }
}

let p = Point(x: 3.1415926, y: 2.5963756)
print("\(p)")
// 3.14 , 2.60

// 자주 사용하는 경우
var firstName = "Gildong"
var lastName = "Hong"
// 1$ 첫번째 파라미터, 2$ 두번째 파라미터
var korean = "사용자의 이름은 %2$@ %1$@ 입니다."
var english = "The username is %1$@ %2$@."

string = String(format: korean, firstName, lastName)
print(string)
// 사용자의 이름은 Hong Gildong 입니다.

string = String(format: english, firstName, lastName)
print(string)
// The username is Gildong Hong.
```

### NumberFormatter
> 보통 이걸 더 많이 씀. 숫자 <=> 문자 변환을 다루는 클래스
- `.roundingMode` : 반올림 모드
- `.maximumSignificantDigits` : 최대 자릿수
- `.minimumSignificantDigits` : 최소 자릿수
- `.numberStyle` : 숫자 스타일
```swift
// 소수점 버리기
let numberFormatter = NumberFormatter()
// 버림으로 지정
numberFormatter.roundingMode = .floor
// 최대 표현하길 원하는 자릿수
numberFormatter.maximumSignificantDigits = 3

let value = 3.1415926
// 문자열화시키는 메서드
var valueFormatted = numberFormatter.string(for: value)!
print(valueFormatted)
// 3.14

// 소수점 필수적 표현하기
// 버림으로 지정
numberFormatter.roundingMode = .floor
// 최소 표현하길 원하는 자릿수
numberFormatter.minimumSignificantDigits = 4
let value2 = 3.1
// 문자열화시키는 메서드
valueFormatted = numberFormatter.string(for: value2)!
// 3.100
print(valueFormatted)

// 세자리수마다 콤마 넣기 ⭐️
numberFormatter.numberStyle = .decimal
let price = 10000000
let result = numberFormatter.string(for: price)!
print(result)
 // "10,000,000"
```

## 서브 스트링 (Substring)
> `String.SubSequence` 타입
- 문자열의 메모리 공간의 공유 개념
```swift
var greeting = "Hello, world!"
// ,(콤마)의 인덱스
let index: String.Index = greeting.firstIndex(of: ",") ?? greeting.endIndex
// 처음부터 인덱스까지
let beginning: String.SubSequence = greeting[..<index]
// "Hello" // ⭐️ String.SubSequence 타입

var word: String.SubSequence = greeting.prefix(5)
word     
// "Hello" // String.SubSequence 타입

// 원본을 바꾸는 순간 Substring 문자열들은 새로운 문자열 공간을 만들어서 저장
greeting = "Happy"

print(beginning) // "Hello"
print(word) // "Hello"

word = greeting.suffix(3)
word     
// "ppy" // String.SubSequence 타입

// 아니면 명시적으로 문자열로 변환해서 저장 가능 (서브스트링에서 벗어남)
let newString: String = String(word)
```
- `prefix(...)` 메서드 등 사용시, **`beginning` 문자열은 `greeting` 문자열의 메모리 공간을 공유**
- 스위프트 내부적으로 최적화 되어있음
- 수정 등이 일어나기 전까지 메모리 공유
- 오랜기간 저장하기 위해선 새롭게 문자열로 저장할 필요 있음

## ==문자열을 배열로 변환==
> 문자열의 배열화, (문자열)배열의 문자열화
- 문자열 <-> 배열 쉽게 변형 가능

```swift
var someString = "Swift"

// map은 배열로 리턴
var array = someString.map { chr in // Character 타입
	String(chr) // String 타입으로 변환
}

// 1) 문자열을 문자열(String) 배열화 하기 ⭐️
var array: [String] = someString.map { String($0) }
print(array)
// ["S", "w", "i", "f", "t"]

// 2) 문자열을 문자(Character) 배열화 하기
// [Character], typealias Element = Character
var array2: [Character] = Array(someString)

// (참고) 문자열을 문자열(String) 배열화하는 추가적 방법
// [String]
var array3: [String] = Array(arrayLiteral: someString)
```

### 문자열 배열을 문자열로 변환
```swift
// 3) 문자열 배열 [String] => 문자열
var newString = array.joined()
// "Swift"

// 4) 문자 배열  [Character] => 문자열
var newString2 = String(array2)
// "Swift"
```

### 문자열을 뒤죽박죽 섞는다면?
> 먼저 문자열을 배열로 변환하는 것을 생각해내기
```swift
someString = "Swift"

// 문자열에서 랜덤으로 요소 하나 뽑아내는 것 가능
someString.randomElement() // "t"
// 섞어서 문자(Character) 배열로 리턴
someString.shuffled() 
// ["t", "i", "w", "S", "f"]

// 불가능 (문자배열 이기때문)
//someString.shuffled().joined()

var newString3 = String(someString.shuffled())
print(newString3)
// "wSfti"

// map고차함수를 사용해서 변환 ⭐️
newString3 = someString.map { String($0) }.shuffled().joined()
print(newString3)
// "fitwS"
```
- `String()`을 이용해 배열화 하는 것 보다 `map`을 이용해 배열화 하는 것이 더 제약이 없고 많이 쓰인다. 

## 문자열 다루기

### 문자열의 대소문자 변형
> Swift는 대문자와 소문자를 다른 문자로 인식 (유니코드 다름)
```swift
var string = "swift"

// 전체 소문자로 바꾼 문자열 리턴 (원본 그대로)
string.lowercased()
// 전체 대문자로 바꾼 문자열 리턴 (원본 그대로)
string.uppercased()
// 대문자로 시작하는 글자로 리턴하는 속성 (원본 그대로)
string.capitalized
//"swift".capitalized

// 소문자로 변형시키서 비교하는 것은 가능
"swift" == "Swift" // false
"swift".lowercased() == "Swift".lowercased() // true
```

#### `count`, `isEmpty` 속성

```swift
// [공백]이 포함된 문자열
var emptyString = " "

// 문자열은 길이를 기준으로 빈문장열을 판단
emptyString.count     // 1
emptyString.isEmpty   // false

// [빈] 문자열 (nil이 절대 아님)
emptyString = ""
emptyString.count        // 0
emptyString.isEmpty      // true

// 빈 문자열은 nil이 아님 => String타입 (O)
if emptyString == nil {
	// String?타입 (X)
	print("nil")
}
```

### String의 인덱스 (색인/순번) 타입
> 문자열도 **Collection 프로토콜** (Array/Dictionary/Set)을 따르고 있음 -> 데이터 바구니
- **문자열의 인덱스는 정수가 아님**
	- 스위프트는 문자열을 글자의 의미 단위로 사용하기 때문에, 정수 인덱스 사용 불가 (메모리상의 일정하지 않은 간격으로 데이터가 존재)
- `문자열.index(<#i: String.Index#>, offsetBy: <#String.IndexDistance#>)` 를 많이 사용함. 

```swift
let greeting = "Guten Tag!"

greeting.startIndex
print(greeting.startIndex)
// Index(_rawBits: 1)
greeting[greeting.startIndex]
// "G"

// 정수형태를 한번 변형해서(걸러서) 사용하는 방식 ⭐️
var someIndex = greeting.index(greeting.startIndex, offsetBy: 2)
greeting[someIndex]
// "t"

someIndex = greeting.index(greeting.startIndex, offsetBy: 1)
greeting[someIndex]
// "u"

someIndex = greeting.index(after: greeting.startIndex)
greeting[someIndex]
// "u"

someIndex = greeting.index(before: greeting.endIndex)
greeting[someIndex]
// "!"

// 개별 문자의 인덱스에 접근
for index in greeting.indices {
    print("\(greeting[index]) ", terminator: "")
}
// 출력결과는 동일하지만 접근법이 다름
for char in greeting {
    print("\(char) ", terminator: "")
}

// 공백 문자열 다음의 글자를 알고 싶을때
var firstIndex = greeting.firstIndex(of: " ")!
var nextOfEmptyIndex = greeting.index(firstIndex, offsetBy: 1)
greeting[nextOfEmptyIndex]
// "T"

// 세번째 글자를 알고 싶을때
var thirdCharIndex  = greeting.index(greeting.startIndex, offsetBy: 2)           // 스타트 인덱스에서 2만큼 이동한 인덱스로
var thirdCh = greeting[thirdCharIndex]

// 범위를 벗어나면 에러 발생 주의 ⭐️
// greeting[greeting.endIndex] 에러 발생
greeting[greeting.index(greeting.endIndex, offsetBy: -1)]
greeting[greeting.index(before: greeting.endIndex)]
// !

// 아래와 같이 올바른 범위에서 실행
someIndex = greeting.index(greeting.startIndex, offsetBy: 7)
if greeting.startIndex <= someIndex && someIndex < greeting.endIndex { // 범위를 벗어나지 않는 경우 코드 실행
    print(greeting[someIndex])
}

// indices를 직접 출력해보기
for i in greeting.indices {
    print(i)
}

// 문자열 특정범위를 추출
let lower = greeting.index(greeting.startIndex, offsetBy: 2)
let upper = greeting.index(greeting.startIndex, offsetBy: 5)
greeting[lower...upper]
// "ten"

// 실제로는 뒤에서 배울, 교체/삭제에서 주로 범위를 활용
var range = greeting.range(of: "Tag!")!
greeting[range]
// "Tag!"

// option에서 .caseInsensitive는 대소문자 구별하지 않는다는 뜻
range = greeting.range(of: "tag", options: [.caseInsensitive])!
greeting[range]
// "Tag"

// 정수 형태 수치로 거리 측정
var distance = greeting.distance(from: lower, to: upper)
print(distance)
// 3
```

## 문자열의 삽입/교체/추가/삭제
> 문자열은 배열과 유사한 데이터 바구니
- **삽입하기 - insert**
	- `insert(_:,at:)` - 특정인덱스에 문자
	- `insert(contentsOf:,at:)` - 특정인덱스에 문자열

```swift
var welcome = "Hello"

welcome.insert("!", at: welcome.endIndex)
// "Hello!"

welcome.insert(contentsOf: " there", at: welcome.index(before: welcome.endIndex))
// "Hello there!"
```
- **교체하기 - replace**
	 - `replaceSubrange(_:,with:)` - 범위기준 교체
	 - `replacingOccurrences(of:,with:)` - (존재하면) 해당글자가 있으면 교체 => 원본은 그대로
	 - `replacingOccurrences(of:,with:,options:,range:)`
```swift
welcome = "Hello there!"
print(welcome)

// 범위를 가지고
if let range = welcome.range(of: " there!") {
	// 교체하기
    welcome.replaceSubrange(range, with: " Swift!")
    print(welcome)
    // "Hello Swift!"
}

// 교체하되, 문자열 원본은 그대로 (occurrence: 존재하는)
var newWelcome = welcome.replacingOccurrences(of: "Swift", with: "World")
// "Swift"라는 문자열이 존재하면, "World"로 교체
print(welcome) // "Hello Swift!"
print(newWelcome) // "Hello World!"

// 대소문자 무시 옵션
newWelcome = welcome.replacingOccurrences(of: "swift", with: "New World", options: [.caseInsensitive])
print(welcome) // "Hello Swift!"
print(newWelcome) // "Hello New World!"
```
- **추가하기 - append**
	 - 문자열 기본 연산자 `+` / `+=`
	 - `append(_:)`
```swift
"swift" + "!"

welcome.append("!")
welcome.append(" Awesome!")
```
- **삭제하기 - remove**
	 - `remove(at:)` - 특정인덱스의 문자
	 - `removeSubrange(_:)` - 특정인덱스의 문자열
	 - `removeFirst(2)`
	 - `removeLast(2)`
	 - `removeAll()`
	 - `removeAll(keepingCapacity: true)`
```swift
welcome = "Hello Swift!"

// 인덱스를 가지고 지우기
// (endIndex의 전 인덱스)
// "!" 지우기
welcome.remove(at: welcome.index(before: welcome.endIndex))
welcome // "Hello Swift"


// 인덱스 범위파악
var range = welcome.index(welcome.endIndex, offsetBy: -6)..<welcome.endIndex
//range = welcome.range(of: " Swift")!

// " Swift"의 범위를 파악하고 지우기
welcome.removeSubrange(range)
welcome // "Hello"

welcome.removeAll()
welcome.removeAll(keepingCapacity: true)
```
 - **Subrange만 반환 (원본은 그대로)**
	 - `dropFirst(2)` - 앞의 두글자 뺀 나머지 반환
	 - `dropLast(2)` - 뒤의 두글자 뺀 나머지 반환

### 문자열 삽입과 삭제의 활용
```swift
var string = "Hello world"

// 1) " " 공백 문자열의 인덱스 찾기
// 2) " " 공백 문자열의 인덱스에 " super" 삽입하기
if let someIndex = string.firstIndex(of: " ") {
    string.insert(contentsOf: " super", at: someIndex)
    print(string)
    // "Hello super world"
}

// 1) 첫 " " 공백 문자열의 인덱스 찾기
// 2) " super" 문자열의 범위 만들기
// 3) 범위 삭제하기
if let firstIndex = string.firstIndex(of: " ") {
    let range = firstIndex...string.index(firstIndex, offsetBy: 5)
    string.removeSubrange(range)
    print(string)
    // "Hello world"
}

// 바꿀 문자열을 정확하게 알고 있다면 => 범위를 직접 리턴하는 메서드 활용 ⭐️
if let range = string.range(of: " world") {
    string.removeSubrange(range)
    print(string)
}
```

## 문자열 비교하기
- 대소문자 구별함
- 크기 비교 가능
	- 앞 글자부터 유니코드 순서 비교
	- 소문자가 더 뒤에 위치해서 더 큼
```swift
// 비교연산자 (대소문자 구별)
"swift" == "Swift" // false
"swift" != "Swift" // true   => 둘의 문자는 다른 것임

// 크기 비교하기 (유니코드 비교)
"swift" < "Swift" // false => 첫 글자의 (유니코드) 순서를 비교
"swift" <= "Swift" // false => 소문자가 (유니코드/아스키코드) 더 뒤에 위치
// "Swift" <= "swift" // true

// 대소문자 일치시킨 후 비교
"swift".lowercased() == "Swift".lowercased() // true
```
### 대소문자 무시하고 비교하는 메서드
- `caseInsensitiveCompare(문자열)`
	- `NSComparisonResult`이라는 새로운 타입이 나옴 -> 열거형임
		- `.orderedSame` - 동일
		- `.orderedAscending` - 오름차순
		- `.orderedDescending` - 내림차순
		- 구체적인 정보를 알 수 있고 활용성이 높음
```swift
var a = "swift"
var b = "Swift"
a.caseInsensitiveCompare(b) // NSComparisonResult
a.caseInsensitiveCompare(b) == ComparisonResult.orderedSame
```

### 문자열 비교 메서드
- `문자열.compare(_: ,options: ,range: ,locale: )`
	- 일치 여부 확인
	- 다양한 옵션 적용이 가능
		- `options: .caseInsensitive` - 대소문자 무시
		- `.regularExpression` - 정규식 검증
		- 옵션 입력 부분 -> `OptionSet` 프로토콜 채택
			- 여러 옵션을 배열 형식으로 전달 가능

```swift
var name = "Hello, Swift"

name.compare("hello", options: [.caseInsensitive]) == .orderedDescending // true
// name이 글자가 더 많아서 뒤에 있다고 인식 -> 내림차순
```

### 문자열 (일부) 포함 여부 및 앞/뒤 글자의 반환

```swift
let string = "Hello, world!"

// 전체문자열에서 포함여부
string.contains("Hello")
string.lowercased().contains("hello")
string.contains("world")

// 접두어/접미어 포함여부
string.hasPrefix("Hello")
string.hasPrefix("world") // false
string.lowercased().hasPrefix("world")

string.hasSuffix("!")
string.hasSuffix("world!")

// 접두어/접미어 반환 (앞에서 또는 뒤에서 몇글자 뽑아내기)
string.prefix(2)
string.suffix(3)

// 공통 접두어 반환
string.commonPrefix(with: "Hello, swift")
string.commonPrefix(with: "hello", options: [.caseInsensitive])

// 앞/뒤를 drop시킨 나머지 반환
string.dropFirst(3)
string.dropLast(3)
```

## 정규식/정규표현식
> 정규식: 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어
- 여러 언어에서 공통적으로 사용함
- 러프한 전화번호 - `#"[0-9]{3}[- .]?[0-9]{4}[- .]?[0-9]{4}"#`
- 러프한 이메일 - `#".*@.*\..*"#`
- 러프한 우편번호 - `#"[0-9]{3}\-[0-9]{3}"#`

```swift
// 올바른 전화번호 형식일까?
let number = "010-1234-12345"

// 정규식 (RawString으로 작성하면 메타문자를 바로 입력가능) => 가독성 높아짐
// (스위프트에서는 \ 백슬레시를 이스케이프 문자로 인식하기 때문)
var telephoneNumRegex = #"[0-9]{3}\-[0-9]{4}\-[0-9]{4}"#

if let _ = number.range(of: telephoneNumRegex, options: [.regularExpression]) {
    print("유효한 전화번호로 판단")
}
```
#### 정규식 참고
- https://www.youtube.com/watch?v=Gg0tlbrxJSc
- https://www.youtube.com/watch?v=-5cnj7q1-YY
- https://regexr.com/
- https://regexr.com/5nvc2

## 특정 문자의 (검색 및) 제거
- `문자열.trimmingCharacters(in: <#CharacterSet#>)`
	- 앞뒤의 특정 문자를 제거하는 메서드
```swift
// 1) 앞뒤의 공백문자의 제거
var userEmail = " my-email@example.com "
var trimmedString = userEmail.trimmingCharacters(in: [" "])
print(trimmedString)
// "my-email@example.com" (처음, 마지막의 공백 문자열 제거)

// CharacterSet 개념 활용
trimmedString = userEmail.trimmingCharacters(in: .whitespaces)
print(trimmedString)

// 2) 앞뒤의 특정문자의 제거
var someString = "?Swift!"
var removedString = someString.trimmingCharacters(in: ["?","!"])
print(removedString) // Swift

someString = "?Swi!ft!"
removedString = someString.trimmingCharacters(in: ["?","!"])
print(removedString) // Swi!ft
// 중간에 있는 !는 제거하지 못함
```

- `문자열.components(separatedBy: <#CharacterSet#>).joined()`
	- 문자열 중간에 특정 문자를 제거하는 방법
	- 해당 특정 문자 기준으로 잘라서 문자열을 배열로 -> 다시 배열을 문자열로 변환
```swift
// 3) (중간에 포함된)공백문자의 제거
var name = " S t e v e "
var removedName = name.components(separatedBy: " ").joined()    //["", "S", "t", "e", "v", "e", ""] -> "Steve"
print(removedName)

// 4) (중간에 포함된)특수문자의 제거
var phoneNum = "010-1234-1234"
var newPhoneNum = phoneNum.components(separatedBy: "-").joined()   // ["010", "1234", "1234"] -> "01012341234"
print(newPhoneNum)

// 5) 여러개의 특수문자를 한꺼번에 제거
var numString =  "1+2-3*4/5"
var removedNumString =  numString.components(separatedBy: ["+","-","*","/"]).joined()
print(removedNumString) // "12345"

// 6) components(separatedBy:)와 거의 동일한 메서드 split(separator:) 그러나 차이는 있음
var str =  "Hello Swift"
var arr = str.split(separator: " ") // 서브스트링으로 리턴함
print(arr) // ["Hello", "Swift"]
print(arr.joined()) // "HelloSwift"

// - (1) split은 Substring 배열로 리턴
str.split(separator: " ")

// - (2) split은 클로저를 파라미터로 받기도 함 (클로저에서 원하는 함수내용을 정의하면 되므로 활용도가 더 높을 수 있음)
str.split { $0 == " " }
```
- (2) `str.split(whereSeparator: <#(Character) throws -> Bool#>)`
	- 파라미터를 클로저 형태로 받을 수 있음
	- 활용도가 더 높아짐
- (미리 정의된) 특정 문자 집합(Set)의 개념을 이용하면 더 편하게 사용 가능
	- [참고](https://developer.apple.com/documentation/foundation/characterset)

### 특정 문자열 검색에서 활용
```swift
name = "hello+world"

if let range = name.rangeOfCharacter(from: .symbols) {
    print(name[range]) // +
}
```


