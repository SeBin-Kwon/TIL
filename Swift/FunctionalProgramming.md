# Swift의 프로그래밍 패러다임

- 객체지향 프로그래밍 - 클래스
- 프로토콜 지향 프로그래밍 - Swift가 유일, 객체지향 프로그래밍의 단점을 보완
- 함수형 프로그래밍 - 클로저를 자유자재로 사용

## FP(Functional Programming)이란?
### 명령형 프로그래밍 (imperitive)

- 변수 지정 / for문 등등 -> 부작용(side-effect)
- **How** - 어떻게 구현해낼까? / 설계 / 알고리즘
```swift
// 배열의 합을 구하는 문제 - 어떻게(how) 구현해낼까?
let numbers = [1, 2, 3]
var sum = 0
for number in numbers {
    sum += number
}
print(sum) // 6
person.name = "홍길동"
```

### 함수형 프로그래밍 / 선언형 (FP)

- 가져다 붙이기만 하면 됨(함수의 조합) / 선언적
- **What** - (어떤 것을) 가져다 붙이면 결과가 나올까?
- 함수를 이용해서(map, filter, reduce 등) 사이드이펙트가 없도록 선언형으로 프로그래밍하는 것
- 함수는 1급 객체 / 모듈화 / 순수함수 / 재귀함수 / 합성 / Currying 등
```swift
배열.map { 클로저 }
   .filter { 클로저 }
   .reduce(0) { 클로저 }

let newNnumbers = [1, 2, 3]
var newSum = 0
// 기존의 함수를 어떻게 조합해서 결과(what)를 만들까?
newSum = newNnumbers.reduce(0) { $0 + $1 }
print(newSum) // 6
```

- 산에 올라가는 방법
	- 산을 걸어서 올라가는 방법 - 명령형
	- 헬리곱터로 정상에서 내리는 방법 - 함수형

개발자는 중간 과정을 신경쓰지 않고, 이미 정의된 함수를 가지고 **"어떻게 조합해서 결과를 만들어 낼까"** 만 신경쓰면 됨. -> 모두가 map/filter/reduce의 쓰는 방법을 알고 있기 때문

- **간결한 코드 작성이 가능해짐**
- SwiftUI에서 사용하는 방식
	- UIKit은 명령형

#### 추가 참고자료
https://youtu.be/jVG5jvOzu9Y   (함수형 프로그래밍이 뭔가요? - 얄팍한 코딩사전)
https://youtu.be/HZkqMiwT-5A   (함수형 프로그래밍이 뭐하는 건가요? - 곰튀김 님)
https://youtu.be/cXi_CmZuBgg   (Functional Reactive Programming 패러다임 - 곰튀김 님)