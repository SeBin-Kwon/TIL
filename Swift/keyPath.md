# 키패스 (keyPath)와 셀럭터 (selector)
## keyPath
> 문자열 방식을 통해 속성에 **간접적으로 접근**하는 기술

- `person.name`은 직접적으로 접근하는 것
- 속성의 값이 바뀌면 객체 외부에서 그것을 관찰하여 알림을 받고 싶을 때 -> `Key Value Observing`
- `\Person.name` 이렇게 사용해서 인스턴스 속성에 간접적으로 접근함 
- **키패스는 경로임**
- 예전에 비해 제네릭으로 타입이 바뀌어서 훨씬 편리해짐.

```swift
let person1 = Person(name: "홍길동")
let smallSchool1 = SmallSchool(classMember: person1)
let school1 = School(name: "슈퍼고", affiliate: smallSchool1)

// School에서 Person.name까지 직접 접근하려면 너무 길어짐
let gildogsName = school1.affiliate.classMember.name

// 미리 경로를 지정 (keyPath)
let namePath = \School.affiliate.classMember.name

// 딕셔너리방식(서브스크립트)로 접근
school1[keyPath: namePath]
```
- 대괄호를 통해 간편하게 간접적으로 접근 가능
- `.appending(path: )`를 통해 경로 추가 가능

### selector
> 메모리 주소를 간접적으로 뽑아낼 수 있는 기술