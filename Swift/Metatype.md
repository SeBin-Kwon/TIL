# Metatype (메타 타입)
> 타입의 타입
- 데이터 영역의 타입 인스턴스를 저장할 때의 타입이 메타 타입임.
- 타입 속성은 타입 인스턴스의 속성을 의미함. -> 이 타입 인스턴스의 타입이 메타 타입

```swift
class Dog {
    static let species = "Dog"
    var name: String = ""
    var weight: Double = 0.0
}

      // ⬇︎ 붕어빵틀의 타입
let dog: Dog.Type = Dog.self
                    // ⬆︎ 붕어빵틀

class Person {
    static let species = "인간"
    var name: String = ""
}

// 인스턴스의 타입과 인스턴스
let person1: Person = Person()
person1.name = "홍길동"


// 인스턴스의 타입과 인스턴스
let person2: Person = Person()
person2.name = "임꺽정"

let pSelf1: Person.Type = Person.self
pSelf1.species  // "인간"
pSelf2.species  // "인간"
Person.species  // "인간"
Person.self.species // "인간"
```

## 메타 타입을 사용하는 API

```swift
// 테이블뷰셀을 등록하는 경우에 메타타입을 사용
tableView.register(<#cellClass: AnyClass?#>, forCellReuseIdentifier: <#String#>)

// JSONDecoder 객체를 사용해서 디코드메서드 사용시
try? decoder.decode(<#type: Decodable.Protocol#>, from: <#Data#>)
```
- 구체적인 인스턴스가 필요한 메서드들이 아니고 어떤 타입 자체로 뭔가를 하겠다는 거임.