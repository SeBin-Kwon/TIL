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

# 옵셔널 체이닝 (Optional Chaining)

> 어떤 배열이 `nil`이 아니면서 **빈 배열인지 확인**할 때, 유용하게 쓸 수 있다.

```swift
let array: [String]? = []
var isEmptyArray = false

// 배열이 있으면서(true), 비어있을 때(true)
if let array = array, array.isEmpty {
  isEmptyArray = true
} else {
  isEmptyArray = false
}

isEmptyArray
```

위 코드를 옵셔널 체이닝을 사용하면 더 간결하게 쓸 수 있다.

```swift
let isEmptyArray = array?.isEmpty == true
```
- array가 `nil`인 경우
`array?`까지만 실행되고 `nil`을 반환

- array가 빈 배열인 경우
`array?.isEmpty`가 실행되고 `true`를 반환

- array에 요소가 있는 경우
`array?.isEmpty`가 실행되고 `false`를 반환

옵셔널 체이닝으로 인해 `Bool?`을 반환하도록 바뀌어서 값이 `nil`, `true`, `false`가 결과로 나올 수 있게 된다.
값이 실제로 `true` 인지를 확인하려면 `== true`를 해줘야 한다.