# 고급연산자 (Advanced Operators)

## 숫자 리터럴
- `0b` - 2진법
- `0o` - 8진법
- `0x` - 16진법
```swift
//스위프트의 숫자 리터럴을 표기하는 방법
var num: Int = 25 // 10진법

// 2진법/8진법/16진법의 수도 직접 써 넣을 수 있음
num = 0b00011001
num = 0o31
num = 0x19

// 큰숫자는 읽기 쉽게하기위해 언더바를 붙이는 것도 가능
// 컴퓨터는 언더바를 읽지않음
num = 1_000_000
num = 10_000_000
num = 10000_0000
```

## 스위프트 정수 타입과 범위
> 지금은 대부분 64비트이다. 8바이트의 메모리 공간을 사용
- 플랫폼 사양에 따르는 타입 : Int, UInt
-  8-bit : Int8, UInt8
- 16-bit : Int16, UInt16
- 32-bit : Int32, UInt32
- 64-bit : Int64, UInt64

```swift
MemoryLayout<Int8>.size   // 1바이트
Int8.max      //  127    ( 2^7승 -1)
Int8.min      // -128    (-2^7승)

MemoryLayout<UInt8>.size     // 1바이트
UInt8.max     //  255     ( 2^8승 -1)
UInt8.min     //    0

MemoryLayout<Int>.size     // 8바이트
Int.max       //  9223372036854775807   ( 2^63승 -1)
Int.min       // -9223372036854775808   (-2^63승 )
```

## 오버플로우 (overflow)
> 스위프트에서는 오버플로우를 기본적으로 허락하지 않음 => 에러발생(크래시)
- C언어나 Objective-C언어의 산술연산자에서는 값이 넘침(overflow)을 허락함(8비트 값을 담을 수 있는 숫자에서 255를 넘어가면 다시 0으로 순환) 
- 오버플로우의 방향은 양(positive)의 방향, 음(nagative)의 방향을 모두 의미
- 특정한 경우에, 특정패턴을 구현하기 위해 오버플로우를 허용하는 경우가 필요한데, 이런 경우 활용을 위해 "오버플로우 연산자"를 마련해 놓았음
```swift
UInt8.max // UInt8(8비트의 값을 담을 수 있음)의 최대값 255
UInt8.min // UInt8(8비트의 값을 담을 수 있음)의 최소값 0
let num: UInt8 = 300 // 에러 발생
```
### 오버플로우 연산자
- `&+` : 오버플로우 더하기 연산자
- `&-` : 오버플로우 빼기 연산자
- `&*` : 오버플로우 곱하기 연산자

## 논리 연산자와 단락 평가 (Short-circuit Evaluation)
> 논리 평가식에서 결과도출에 필요한 최소한의 논리식만 평가
- ex) 참을 찾을때 까지만 실행하고, 참을 찾으면 나머지 표현식은 평가하지 않음
	- `&&` 먼저 확인, 그 다음 `||` 확인
```swift
false && true // false만 확인 (항상 false)
true || false // true만 확인 (항상 true)
```
### 단락 평가로 인한 주의
> **사이드 이펙트 발생 시는 반드시 주의**
- 일부 변수가 표현식의 평가 결과로 값이 변경되는 것
- 논리평가식에서 사이드 이펙트가 발생하는 경우, 단락평가로 인해 함수 등의 실행횟수의 차이로 인해 의도치 않은 결과가 도출될 수 있음
	- 사이드 이펙트: 함수 스코프에서 외부 변수의 값을 변경시키는 것
```swift
var num = 0

func checking() -> Bool {
    print(#function)
    num += 1
    return true
}

// if문의 조건식에서 함수를 호출하는 경우
if checking() || checking() {
             
}
num // ||인 경우 1, &&인 경우 2
```

### 해결 방법
> 미리 표현식을 실행시킨다.
```swift
var num = 0

func checking() -> Bool {
    print(#function)
    num += 1
    return true
}

let checkingResult1 = checking()
let checkingResult2 = checking()

// if문의 조건식에서 함수를 호출하는 경우
if checkingResult1 || checkingResult2 {
             
}
num // 2
```


## 비트 연산자 (Bitwise Operators)
> 메모리 비트(bit) 단위로 직접적인 논리 연산을 하거나, 비트 단위 이동시에 사용하는 연산자
- 주로, 어떤 하드웨어적인 처리(예, 장치 드라이버 생성)나 그래픽 프로그래밍과 임베디드 프로그래밍, 암호화처리, 게임 등 아주 한정적으로 쓰이는 이론적인 내용
- 연산속도가 빠름 - 직접적으로 메모리의 실제 비트를 컨트롤
- 짧은 코드로 복잡한 로직을 구현 가능한 경우가 있음

### 비트 논리 연산자
```swift
// ~  : Bitwise NOT Operator(비트와이즈 낫 연산자) 
// 기존의 메모리의 비트를 반전 시킴
let a1: UInt8 = 0b0000_1111    // 15
let b1 = ~a1  // 0b1111_0000   // 240

// &  : Bitwise AND Operator(비트와이즈 앤드 연산자)
// 두개의 메모리의 비트가 둘 다 1일때만 1로 설정
let a2: UInt8 = 0b1111_1100   // 252
let b2: UInt8 = 0b0011_1111   // 63
let c2 = a2 & b2  // 0b0011_1100      // 60

// |  : Bitwise OR Operator(비트와이즈 오어 연산자)
// 두개의 메모리의 비트 중 하나라도 1이면 1을 반환
let a3: UInt8 = 0b1011_0010   // 178
let b3: UInt8 = 0b0101_1110   // 94
let c3 = a3 | b3  // 0b1111_1110      // 254

// ^  : Bitwise XOR Operator(비트와이즈 엑스오어 연산자)
// 두개의 메모리의 비트 중 서로 다르면 1을 반환, 서로 같으면 0을 반환
let a4: UInt8 = 0b0001_0100    // 20
let b4: UInt8 = 0b0000_0101    // 5
let c4 = a4 ^ b4  // 0b0001_0001    // 17
```

### 비트 이동 연산자
> 부호가 있을 때만 주의
- 모든 비트를 정해진 값만큼 왼쪽이나 오른쪽으로 이동
- 비트를 이동하는 것은 2를 곱하거나, 나누는 효과를 가짐
	- 정수 비트를 왼쪽으로 1칸 이동하면 값이 2배가 됨

```swift
// << : Bitwise Left Shift Operator(비트와이즈 레프트 시프트 연산자)
// 부호가 없는 경우
let leftShiftBits: UInt8 = 4   // 0b0000_0100   //   4
leftShiftBits << 1             // 0b0000_1000   //   8 (곱하기 2)
leftShiftBits << 2             // 0b0001_0000   //  16 (곱하기 2^2승 => 곱하기 4)
leftShiftBits << 5             // 0b1000_0000   // 128 (곱하기 2^5승 => 곱하기 32)

// 부호가 있는 경우
let shiftBits: Int8 = 4    // 0b0000_0100   //   4
shiftBits << 1             // 0b0000_1000   //   8 (곱하기 2)
shiftBits << 2             // 0b0001_0000   //  16 (곱하기 4)

shiftBits << 5             // 0b1000_0000   //-128 (곱하기 2^5승, 다만 여기선 범위초과로 오버플로우)

// >> : Bitwise Right Shift Operator(비트와이즈 라이트 시프트 연산자)
// 부호가 없는 경우
let rightShiftBits: UInt8 = 32  // 0b0010_0000   //  32
rightShiftBits >> 1             // 0b0001_0000   //  16 (나누기 2)
rightShiftBits >> 2             // 0b0000_1000   //   8 (나누기 4)
rightShiftBits >> 5             // 0b0000_0001   //   1 (나누기 2^5승)

// 부호가 있는 경우
let shiftSignedBits: Int8 = -2   // 0b1111_1110   //  -2
shiftSignedBits >> 1             // 0b1111_1111   //  -1 (나누기 2) 몫
shiftSignedBits >> 2             // 0b1111_1111   //  -1 (나누기 4) 몫

shiftSignedBits >> 5             // 0b1111_1111   //  -1 (나누기 2^5승) 몫
```

## 연산자 메서드의 직접 구현
> 연산자: `타입.함수이름(파라미터: 타입)` 형태로 실행하지 않는 특별한 형태의 **타입 메서드**
- 커스텀 타입에도 메서드의 형태로 연산자(+,-,== 등)를 구현 가능
- 문자열 더하기 - `static func + (lhs: String, rhs: String) -> String`
- 문자열 복합할당 연산자 - `static func += (lhs: inout String, rhs: String)`

```swift
struct Vector2D {
    var x = 0.0
    var y = 0.0
}

// 1) 산술 더하기 연산자의 구현 (infix 연산자)
//infix operator + : AdditionPrecedence // 연산자 선언
extension Vector2D { 
    static func + (lhs: Vector2D, rhs: Vector2D) -> Vector2D {
	    // infix 키워드 생략해야함
        return Vector2D(x: lhs.x + rhs.x, y: lhs.y + rhs.y)
    }
}

let vector = Vector2D(x: 3.0, y: 1.0)
let anotherVector = Vector2D(x: 2.0, y: 4.0)
let combinedVector = vector + anotherVector
print(combinedVector) // Vector2D(x: 5.0, y: 5.0)

// 2) 단항 prefix 연산자의 구현 (전치연산자)
extension Vector2D {
    static prefix func - (vector: Vector2D) -> Vector2D {
        return Vector2D(x: -vector.x, y: -vector.y)
    }
}

let positive = Vector2D(x: 3.0, y: 4.0)
let negative = -positive
print(negative) // Vector2D(x: -3.0, y: -4.0)
let alsoPositive = -negative
print(alsoPositive) // Vector2D(x: 3.0, y: 4.0)

// 3) 복합할당 연산자의 구현
extension Vector2D {
    static func += (left: inout Vector2D, right: Vector2D) {
        left = left + right
    }
}
```
- 서로 다른 인스턴스들을 계산하는 메서들을 만들 때 타입 메서드로 만들자

### 비교 연산자
> 반드시 프로토콜을 채택해야함
- 동일성 비교 - `Equatable` 프로토콜
- 크기, 순서 비교 - `Comparable` 프로토콜
- `Comparable` 프로토콜은 `Equatable` 프로토콜을 상속
	- 동일성 비교가 가능해야, 크기도 비교 가능

#### `Equatable` 프로토콜을 채택 하기만 하면
> 아래 경우에 해당되면 컴파일러가 알아서 구현해줌
- 열거형 - 연관값이 있으면서, 모든 연관값이 Equatable 프로토콜을 준수하는 경우
- 구조체 - '저장속성'만 가지며, 저장속성의 타입이 Equatable 프로토콜을 준수하는 경우
- `==` (Equal to operator)를 구현하면 `!=` (Not equal to operator) 자동으로 구현해줌

```swift
let vector1 = Vector2D(x: 1.0, y: 2.0)
let vector2 = Vector2D(x: 2.0, y: 3.0)

extension Vector2D: Equatable {
    // 직접구현
    static func ==(lhs: Vector2D, rhs: Vector2D) -> Bool {
        return (lhs.x == rhs.x) && (lhs.y == rhs.y)
    }
//    static func !=(lhs: Vector2D, rhs: Vector2D) -> Bool {
//        return (lhs.x != rhs.x) || (lhs.y != rhs.y)
//    }
}
vector1 == vector2 // false
vector1 != vector2 // true
```
- 열거형의 경우, 연관값이 없으면 원래부터 동일성 비교 가능
	- 연관값이 전혀 없는 열거형은 굳이 `Equatable` 프로토콜을 채택하지 않아도, `==` 메서드 자동 채택/구현
- `Comparable` 프로토콜 경우 `<` 만 구현해도 나머지 `>`, `<=`, `>=` 3개는 구현 안해도 됨.

## 사용자 정의 연산자의 구현
> 연산자 선언 -> 메서드 구현
- 선언을 먼저 해주고 타입 메서드를 구현해야 한다.
```swift
// 후치 연산자 선언
postfix operator ++

// 구현
extension Int {
	static postfix func ++(num: inout Int) {
	num = num + 1
	}
}
```

### 연산의 우선순위 그룹
> **중위연산자(`infix`)인 경우 우선 순위 그룹을 지정 해줘야 한다.** (+보다 먼저 계산 해야하는지 등)
```swift
// higherThan 또는 lowerThan 둘중에 하나는 반드시 지정해야함
precedencegroup MyPrecedence {
	// ~보다 높은(higherThan): 지정하려는 그룹보다 순위가 낮은 그룹
    higherThan: AdditionPrecedence
    // ~보다 낮은(lowerThan): 지정하려는 그룹보다 순위가 높은 그룹
    lowerThan: MultiplicationPrecedence
    associativity: left // 결합성 => left / right / none
}

infix operator +-: MyPrecedence

extension Vector2D {
    static func +- (left: Vector2D, right: Vector2D) -> Vector2D {
        return Vector2D(x: left.x + right.x, y: left.y - right.y)
    }
}
```
- 결합성은 왼쪽으로 계산할건지, 오른쪽으로 계산할건지 방향
	- 사칙연산은 왼쪽, 할당은 오른쪽임
- 우선순위 그룹을 지정하지 않으면 "DefaultPrecedence"라는 기본 그룹에 속하게 됨
	- 삼항연산자보다 한단계 높은 우선순위가 되며, 결합성은 none설정되어 다른 연산자와 결합 사용은 불가능