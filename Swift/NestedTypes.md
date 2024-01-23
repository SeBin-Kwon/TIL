# 중첩 타입 (Nested Types)

> 말 그대로 타입이 중첩 됨.

```swift
class Aclass {
    struct Bstruct {
        enum Cenum {
            case aCase   // 열거형에는 케이스 필요
            case bCase
            struct Dstruct {
                
            }
        }
        var name: Cenum
    }
}

// 타입 선언과 인스턴스의 생성

let aClass: Aclass = Aclass()
let bStruct: Aclass.Bstruct = Aclass.Bstruct(name: .bCase)
let cEnum: Aclass.Bstruct.Cenum = Aclass.Bstruct.Cenum.aCase // 열거형은 케이스선택
let dStruct: Aclass.Bstruct.Cenum.Dstruct = Aclass.Bstruct.Cenum.Dstruct()
```
- 중첩 타입에서 타입을 명시적으로 쓰려면 풀네임 다 써야함.
- 열거형은 앞 부분 생략 가능
### 왜 사용하나?
- 특정 타입 내에서만 사용하기 위함
- 타입 간의 관계가 명확해짐
- 내부 구조 디테일하게 설계 가능



## 예시

```swift
struct K {
    static let appName = "MySuperApp"
    static let cellIdentifier = "ReusableCell"
    static let cellNibName = "MessageCell"
    struct BrandColors {
        static let purple = "BrandPurple"
        static let lightPurple = "BrandLightPurple"
    }
    struct FStore {
        static let collectionName = "messages"
        static let senderField = "sender"
    }
}

// 문자열 대신에 아래처럼 사용할 수 있음 (문자열 실수는 치명적인 에러를 발생시킴)
let app = K.appName      // "MySuperApp"
let color = K.BrandColors.purple    // "BrandPurple"
```

