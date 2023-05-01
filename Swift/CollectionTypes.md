# Swift의 컬렉션 타입
> Array, Dictionary, Set

## Array
- 순서가 있는 리스트 컬렉션
- 생성할 때 지정했던 타입만 넣을 수 있다.
- 빈 배열을 선언할 때 **반드시 타입을 명시해야 한다.**

```swift
// 다양한 Int 타입의 빈 Array 선언
var integers: Array<Int> = Array<Int>()
var integers2: Array<Int> = [Int]()
var integers3: [Int] = [Int]()
var integers4: [Int] = []
var integers5: Array<Int> = Array()
var integers6: [Int]()
```
- 선언과 동시에 초기화 할 때 값이 있다면 **자동으로 타입을 추론**한다.
```swift
var intNumbers = [1,2,3,4,5]
// 'Int' 요소를 갖는 배열
var strings = ["A","BC","DEF"]
// 'String' 요소를 갖는 배열
```

- `Int` 타입 배열은 연속된 숫자 배열을 쉽게 선언할 수 있다.
```swift
var intArray = Array<Int>(1...10) 
// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

- `let`을 사용하여 Array를 선언하면 불변 Array가 생성된다.
```swift
let immutableArray: [1, 2, 3]

// 변경할 수 없기 때문에 아래의 메소드들은 사용할 수 없다.
immutableArray.append(4)
immutableArray.removeAll()
```

- 한 배열에 여러 자료형을 넣으려면 `Any` 타입으로 지정하면 된다.
```swift
let anyArray: [Any] = [1, 2, "a", "b"]
```

### Array 메소드

`append` : 리스트에 요소 추가하기

```swift
integers.append(1)
integers.append(100)
// [1, 100]

integers.append(101.1)
// 다른 타입은 넣을 수 없다.
```
`contains` : 해당 요소가 들어있는지 확인하기
```swift
integers.contains(100)
// true
integers.contains(99)
// false
```
`remove(at: {idx})` : 리스트에서 해당 인덱스 제거하기
```swift
// 0번 인덱스 제거하기
integers.remove(at: 0)
// [100]
```
`removeLast` : 리스트에서 마지막 요소 제거하기
```swift
integers.removeLast()
// [1]
```
`removeAll` : 리스트에서 모든 요소 제거하기
```swift
integers.removeAll()
// []
```
`count` : 리스트의 요소 개수, 길이
```swift
integers.count
// 0
```

[배열 관련 함수 참고](https://seolhee2750.tistory.com/66)

## Dictionary
- Key와 Value의 쌍으로 이루어진 컬렉션
- 순서가 없다.
- Key는 중복 가능하지만, Value는 중복되면 안된다.
- 모든 Key의 자료형이 같아야 하고, 모든 Value의 자료형도 같아야 한다. 
- Value에 여러 타입을 저장하고 싶다면 `Any`로 선언한다.
- **Key에는 `Any`가 올 수 없다.**
```swift
// Key가 `String` 타입, Value가 `Any`인 빈 Dictionary 선언
var anyDictionary: Dictionary<String, Any> = [String: Any]()

let emptyDictionary: [String: String] = [:]
let initalizedDictionary: [String: String] = ["name": "sebin", "gender": "female"] 
// let으로 선언했으므로 emptyDictionary와 initalizedDictionary는 값을 변경할 수 없다.

// 값 추가하기
anyDictionary["someKey"] = "value"
anyDictionary["anotherKey"] = 100
anyDictionary
// ["someKey": "value", "anotherKey": 100]
```

- `nil`로 값을 제거할 수 있다.

```swift
anyDictionary["anotherKey"] = nil
// ["someKey": "value"]
```

- 딕셔너리 키에 해당하는 값이 있을 수도, 없을 수도 있는 **불확실성 때문에 상수에 할당할 수 없다.**
```swift
let someValue: String = initalizedDictionary["name"]
// error
```

### Dictionary 메소드

`count` : 딕셔너리 개수 확인하기
```swift
anyDictionary.count
// 1
```

`removeValue(forKey: {Key})` : 딕셔너리에서 지정한 키에 해당하는 값 제거하기
```swift
anyDictionary.removeValue(forKey: {someKey})
// [:]
```

`isEmpty` : 딕셔너리 비었는지 확인하기
```swift
anyDictionary.isEmpty
// true
```

[딕셔너리 관련 함수 참고](https://babbab2.tistory.com/113)

## Set
- 각 요소가 유일한, 중복된 값이 없는 컬렉션
- 순서가 없다.
- 합집합, 교집합 등 집합 연산이 가능하다.

```swift
// Set은 축약 문법이 없다.
var integerSet: Set<Int> = Set<Int>()
//Set([])
```

### Set 메소드
`insert` : Set에 요소 추가하기
```swift
integerSet.insert(1)
integerSet.insert(100)
integerSet.insert(99)
integerSet.insert(99)
// {100, 99, 1}
```

`contains` : 해당 요소가 들어있는지 확인하기
```swift
integerSet.contains(1)
// true
integerSet.contains(2)
// false
```

`remove` : 해당 요소 제거하기
```swift
integerSet.remove(100)
// {1, 99}
```

`removeFirst` : 첫번째 요소를 제거하지만 **순서가 없기 때문에 확신할 수 없다.**
```swift
integerSet.removeFirst()
// {99}
```

`count` : Set 개수 확인하기
```swift
integerSet.count
// 1
```

`union({Set})` : 합집합 연산
```swift
let setA: Set<Int> = [1, 2, 3, 4, 5]
let setB: Set<Int> = [3, 4, 5, 6, 7]

let union: Set<Int> = setA.union(setB)
// {2, 4, 5, 6, 7, 3, 1}
```

`intersection({Set})` : 교집합 연산
```swift
let intersection: Set<Int> = setA.intersection(setB)
// {5, 3, 4}
```

`subtracting({Set})` : 차집합 연산
```swift
let subtracting: Set<Int> = setA.subtracting(setB)
// {1, 2}
```

`exclusiveOr({Set})` : 차집합들의 합집합 또는 합집합에서 교집합을 뺌
```swift
let exclusiveOr: Set<Int> = setA.exclusiveOr(setB)
// {1, 6, 2, 7}
```

`sorted` : 정렬, 배열로 변환한다.
```swift
let sortedUnion = [Int] = union.sorted()
// [1, 2, 3, 4, 5, 6, 7]
```

[Set 관련 함수 참고](http://minsone.github.io/mac/ios/swift-set-type)