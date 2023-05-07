# Swift의 구조체

> 구조체란 인스턴스의 값(프로퍼티)을 저장하거나 기능(메소드)을 제공하고 이를 캡슐화할 수 있는 스위프트가 제공하는 타입(named type)

- 스위프트 대부분 타입은 구조체로 이루어져 있다.
- 구조체는 값(value) 타입이다.
- 타입 이름은 대문자 카멜케이스를 사용하여 정의한다.

클래스`class`와 비슷하지만 클래스는 상속이 가능하고 구조체는 불가능하다.
또한 클래스는 참조`Reference`를 하고 구조체는 복사`Copy`를 한다.

```swift
struct 이름 {
	// 구현부
}
```
**클래스 변수**(Static)
- 클래스 내에 Static 키워드로 선언된 변수
- 처음 실행되어 클래스가 메모리에 올라갈 때 ~ 프로그램이 종료될 때까지 유지
- 클래스가 여러 번 생성되어도 Static 변수는 처음 딱 한 번만 생성됨
- 동일한 클래스의 모든 객체들에 의해서 공유됨
- 한 클래스의 모든 인스턴스들이 공통적인 값을 가져야할 때 클래스 변수로 선언한다.

**인스턴스 변수**(Non-static)
- 클래스 내에 선언된 변수
- 프로퍼티는 인스턴스 변수, 속성이다.
- 객체 생성 시마다 매번 새로운 변수가 생성됨
- 클래스 변수와 달리 공유되지 않음

```swift
struct Sample {
	// 인스턴스 프로퍼티
    // 가변 프로퍼티(값 변경 가능)
    var mutableProperty: Int = 100 
    
    // 불변 프로퍼티(값 변경 불가능)
    let immutableProperty: Int = 100 
    
    // 타입 프로퍼티(static 키워드 사용 : 타입 자체가 사용하는 프로퍼티)
    static var typeProperty: Int = 100 
    
    // 인스턴스 메서드(인스턴스가 사용하는 메서드)
    func instanceMethod() {
        print("instance method")
    }
    
    // 타입 메서드(static 키워드 사용 : 타입 자체가 사용하는 메서드)
    static func typeMethod() {
        print("type method")
    }
}
```

```swift
// 가변 인스턴스 생성
var mutable: Sample = Sample()

mutable.mutableProperty = 200

// 불변 프로퍼티는 인스턴스 생성 후 수정할 수 없다.
// 컴파일 오류 발생
//mutable.immutableProperty = 200

// 불변 인스턴스
let immutable: Sample = Sample()

// 불변 인스턴스는 아무리 가변 프로퍼티라도 인스턴스 생성 후에 수정할 수 없다.
// 컴파일 오류 발생
//immutable.mutableProperty = 200
//immutable.immutableProperty = 200


// 타입 프로퍼티 및 메서드
Sample.typeProperty = 300
Sample.typeMethod() // type method

// 인스턴스에서는 타입 프로퍼티나 타입 메서드를 사용할 수 없다.
// 컴파일 오류 발생
//mutable.typeProperty = 400
//mutable.typeMethod()
```

```swift
struct Student {
	// 가변 프로퍼티
    var name: String = "unknown"

    // 키워드도 `로 묶어주면 이름으로 사용할 수 있다.
    var `class`: String = "Swift"
    
    // 타입 메서드
    static func selfIntroduce() {
        print("학생타입입니다")
    }
    
    // 인스턴스 메서드
    // self는 인스턴스 자신을 지칭하며, 몇몇 경우를 제외하고 사용은 선택사항.
    func selfIntroduce() {
        print("저는 \(self.class)반 \(name)입니다")
    }
}

// 타입 메서드 사용
Student.selfIntroduce() // 학생타입입니다

// 가변 인스턴스 생성
var yagom: Student = Student()
yagom.name = "yagom"
yagom.class = "스위프트"
yagom.selfIntroduce()   // 저는 스위프트반 yagom입니다

// 불변 인스턴스 생성
let jina: Student = Student()

// 불변 인스턴스이므로 프로퍼티 값 변경 불가
// 컴파일 오류 발생
//jina.name = "jina"
jina.selfIntroduce() // 저는 Swift반 unknown입니다
```

### 값 타입을 사용하는 경우

1. 연관된 몇몇의 값들을 모아서 하나의 데이터 타입으로 표현하고 싶은 경우

2. 다른 객체 또는 함수 등으로 전달될 때 참조가 아니라 복사(값 복사) 할 경우

3. 자신을 상속할 필요가 없거나, 다른 타입을 상속 받을 필요가 없는 경우