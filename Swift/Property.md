# Swift의 프로퍼티
## 프로퍼티의 종류

- 인스턴스 / 타입 / 지연 저장 프로퍼티

- 인스턴스 / 타입 연산 프로퍼티

저장 프로퍼티는 말 그대로 값을 저장해주는 프로퍼티이고, 연산 프로퍼티는 값을 저장하고 있지 않고 특정하게 계산한 값을 반환해 주는 프로퍼티이다.

## 정의와 사용

- 연산 프로퍼티는 클래스, 구조체, 열거형 모두에서 사용 가능하다.

- 저장 프로퍼티는 클래스와 구조체에서만 사용 가능하다.

- 열거형 내부에는 **연산 프로퍼티만 구현 가능하다.**

- 연산 프로퍼티는 `var`로만 선언할 수 있다.

- 연산 프로퍼티는 읽기 전용과 읽기, 쓰기 전용은 구현할 수 있지만 **쓰기 전용으로는 구현할 수 없다.**

- 읽기 전용의 `get` 블럭은 생략 가능하다.

- `set` 블럭에서 암시적 매개변수 `newValue`를 사용할 수 있다.


```swift
struct Student {
    
    // 인스턴스 저장 프로퍼티
    var name: String = ""
    var `class`: String = "Swift"
    var koreanAge: Int = 0
    
    // 인스턴스 연산 프로퍼티
    var westernAge: Int {
        get {
            return koreanAge - 1
        }
        
        set(inputValue) {
            koreanAge = inputValue + 1
        }
    }
    
    // 타입 저장 프로퍼티
    static var typeDescription: String = "학생"
    
    /*
    // 인스턴스 메서드
    func selfIntroduce() {
        print("저는 \(self.class)반 \(name)입니다")
    }
     */
    
    // 읽기전용 인스턴스 연산 프로퍼티
    // 간단히 위의 selfIntroduce() 메서드를 대체할 수 있다
    var selfIntroduction: String {
        get {
            return "저는 \(self.class)반 \(name)입니다"
        }
    }
        
    /*
     // 타입 메서드
     static func selfIntroduce() {
     print("학생타입입니다")
     }
     */
    
    // 읽기전용 타입 연산 프로퍼티
    // 읽기전용에서는 get을 생략할 수 있다
    static var selfIntroduction: String {
        return "학생타입입니다"
    }
}

// 타입 연산 프로퍼티 사용
print(Student.selfIntroduction)
// 학생타입입니다

// 인스턴스 생성
var yagom: Student = Student()
yagom.koreanAge = 10

// 인스턴스 저장 프로퍼티 사용
yagom.name = "yagom"
print(yagom.name)
// yagom

// 인스턴스 연산 프로퍼티 사용
print(yagom.selfIntroduction)
// 저는 Swift반 yagom입니다

print("제 한국나이는 \(yagom.koreanAge)살이고, 미국나이는 \(yagom.westernAge)살입니다.")
// 제 한국나이는 10살이고, 미국나이는 9살입니다.
```

### 지연 저장 프로퍼티

> 클래스는 호출했으나 클래스 안 구조체의 값이 할당되기 전에 생성하고 싶다면 사용하면 된다.
> 프로퍼티의 선언 앞에 `lazy` 키워드를 붙이면 된다.

**반드시 변수(`var`)로 선언해야 한다.** 왜냐하면 상수는 초기화가 되기 전에 항상 같은 값을 갖는 프로퍼티인데, 지연 프로퍼티는 처음 사용되기 전에는 값을 갖지 않기 때문이다.

```swift
struct CoordinatePoint {
    var x: Int = 0
    var y: Int = 200
}
 
let SeogunPount: CoordinatePoint = CoordinatePoint(x: 10, y: 20)
 
class Position {
    lazy var point: CoordinatePoint = CoordinatePoint()
    let name: String
    
    init(name: String) {
        self.name = name
    }
}
//lazy 키워드 덕분에 point 프로퍼티를 사용하지 않아 Point객체가 생성되지 않음
let SeogunPositon: Position = Position(name: "서근")
```

위 코드에서 Point 프로퍼티를 사용하지 않았기 때문에 불필요한 성능 저하나 공간 낭비를 줄일 수 있다.