# Swift의 열거형

> 같은 주제로 연관된 데이터들을 멤버로 구성하여 나타내는 자료형

**공통된 주제**에 대해서 **이미 정해좋은 입력 값만** 선택해서 받고 싶을 때 사용한다.

- `enum` 자체가 하나의 데이터 타입으로, 대문자 카멜케이스를 사용하여 이름을 정의한다.
- 각 case는 소문자 카멜케이스로 정의한다.
- 각 case는 그 자체가 고유의 값이다.(각 case에 자동으로 정수값이 할당되지 않음)
- 각 case는 한 줄에 개별로도, 한 줄에 여러개도 정의할 수 있다.

```swift
enum Weekday {
    case mon
    case tue
    case wed
    case thu, fri, sat, sun
}

var day: Weekday = Weekday.mon

// 타입이 명확하다면 .케이스 처럼 표현해도 된다.
day = .tue
print(day) // tue
```

- switch문의 비교값에 열거형 타입이 위치하고, **모든 열거형 케이스를 포함한다면** `default`를 작성할 필요 없다.
- 모든 열거형 케이스를 포함하지 않으면 꼭 `default`문을 작성하자

```swift
switch day {
case .mon, .tue, .wed, .thu:
    print("평일입니다")
case Weekday.fri:
    print("불금 파티!!")
case .sat, .sun:
    print("신나는 주말!!")
}
```

## 원시값이 있는 열거형

> case에 원시값(Raw Value)을 지정해줄 수 있다. C 언어의 enum처럼 정수값을 가질 수도 있다.

원시값이 될 수 있는 자료형은 총 3가지이다.

1. Number Type

2. Character Type

3. String Type

Hashable 프로토콜을 따르는 모든 타입이 원시값의 타입으로 지정될 수 있다.

- 위와 같은 원시 값을 가지고 싶다면, **enum 선언 시 이름 옆에 Type을 꼭 명시해야 한다.**

- 케이스별로 각각 다른 값을 가져야한다.

- 원시 값은 필수가 아니다.

- 자동으로 1씩 증가된 값이 할당 된다.
**Raw Value가 없는 case는, 바로 이전 case의 Raw Value에서 +1한 값이 할당됨.**
`Int`형이 아닌 자료형으로 지정했을 경우, **모든 case에 대해 값을 지정해주는 것이 아니면 에러가 발생함.(1이란 정수값을 더하기 때문)**

- 원시 값 타입이 `string`이고 지정되지 않았다면 케이스의 이름이 원시 값으로 사용된다.

```swift
enum Fruit: Int {
    case apple = 0
    case grape = 10
    case peach
    // case mango = 0
}
// mango와 apple의 원시값이 같으므로 mango 케이스의 원시값을 0으로 정의할 수 없다
// peach는 자동으로 11이 할당 된다.

print("Fruit.peach.rawValue == \(Fruit.peach.rawValue)")
// Fruit.peach.rawValue == 11
```

### 원시값 접근

> `rawValue`라는 속성을 이용해 접근한다.

```swift
var user1: Fruit = .apple
var user2: Fruit = .grape
var user3: Fruit = .peach

print(user1) // apple
print(user2.rawValue) // 10
print(user3.rawValue) // 11
```

### 원시값을 통한 초기화

- **원시값 통해 초기화 한 열거형 값은 `옵셔널` 타입**이므로 `Fruit` 타입이 아니다.
원시값이 케이스에 해당하지 않을 수 있기 때문이다.

```swift
//let apple: Fruit = Fruit(rawValue: 0)
let apple: Fruit? = Fruit(rawValue: 0)

// if let 구문을 사용하면 rawValue에 해당하는 케이스를 곧바로 사용할 수 있습니다
if let orange: Fruit = Fruit(rawValue: 5) {
    print("rawValue 5에 해당하는 케이스는 \(orange)입니다")
} else {
    print("rawValue 5에 해당하는 케이스가 없습니다")
} // rawValue 5에 해당하는 케이스가 없습니다
```

### 열거형 생성

> 원시값이 있는 열거형의 경우, `열거형WithRawValue.init(rawValue: "case")` 를 통해서 열거형을 생성할 수 있다.

```swift
var user4 = FruitWithRawValue.init(rawValue: "apple")
// 0
var user5 = FruitWithRawValue.init(rawValue: "lemon")
// nil
```