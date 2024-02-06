# 에러 처리 (Error Handling)
- **컴파일 오류:** 코드가 잘못되었음을 알려줌(문법적 오류/에러)
	- 코드의 수정을 통해 해결
- **런타임 오류:** 프로그램이 실행되는 동안 발생 -> 앱이 꺼짐 (크래시)
	- 발생 가능한 에러를 미리 처리하면 강제 종료 되지 않음.

> 앱이 꺼지지 않게 처리
- 에러는 일반적으로 동작. 함수의 처리과정에서 일어남.
- 함수를 정의할 때, 예외적으로 에러가 발생할 수 있는 함수다. 라고 정의하고 처리할 수 있음.

## 에러 처리의 과정 (3단계)
### 1. 에러 정의
> 어떤 에러가 발생할지 경우를 미리 정의

```swift
enum HeightError: Error {  //에러 프로토콜 채택
    case maxHeight
    case minHeight
}
```
- 에러는 **열거형**이다.
- 에러는 **`Error` 프로토콜을 채택**해야 한다.

### 2. 에러가 발생할 수 있는 함수 정의
> 에러를 던질 수 있는 함수 타입을 정의

```swift
func checkingHeight(height: Int) throws -> Bool {
    if height > 190 {
        throw HeightError.maxHeight
    } else if height < 130 {
        throw HeightError.minHeight
    } else {
        if height >= 160 {
            return true
        } else {
            return false
        }
    }
}
```
- `throws` 키워드로 정의
- 함수 내부에선 `throw`를 사용하여 에러 던짐 (`return`키워드와 비슷함)

### 3. 에러가 발생할 수 있는 함수 처리 (실행)
> `try`와 `do-catch`문으로 처리

```swift
do {
    let isChecked = try checkingHeight(height: 200)
    print("놀이기구 타는 것 가능: \(isChecked)")
} catch {
    print("놀이기구 타는 것 불가능")
    
}
```
- 에러가 발생할 수 있는 (`throws` 키워드로 정의한) 함수는 `try` 키워드로 실행해야 한다.
- `try`는 `do` 블럭 안에서 사용할 수 있다.
- 함수가 정상 처리 되면 `do` 블럭에서 처리한다.
- 함수가 에러를 던졌을 경우 `catch` 블럭에서 처리한다.

## 에러 처리 방법
### 1. try
> 에러 정식 처리 방법 -> 일반적으로 사용
```swift
do {
    let isChecked = try checkingHeight(height: 200)
    if isChecked {
        print("청룡열차 가능")
    } else {
        print("후룸라이드 가능")
    }
} catch {
    print("놀이기구 타는 것 불가능")
}
```

### 2. try?
> 옵셔널 try -> 옵셔널 타입으로 리턴
```swift
let isChecked = try? checkingHeight(height: 200) // Bool?
```
- 에러가 발생하면 `nil` 리턴
- 정상적인 경우 옵셔널 타입 -> 벗겨서 사용해야함
### 3. try!
> Forced try -> 에러가 날 수 없는 경우에만 사용
```swift
let isChecked2: Bool = try! checkingHeight(height: 150) // Bool
```
- 에러가 발생하면 런타입 에러
## Catch 블럭 처리법
> `do` 블럭에서 발생한 에러만을 처리하는 블럭
- **반드시 모든 에러를 처리해야함**
### 1. Catch 패턴이 있는 경우
> 모든 에러를 각각 따로 처리 해야함
```swift
do {
    let isChecked = try checkingHeight(height: 100)
    print("놀이기구 타는 것 가능: \(isChecked)")
} catch HeightError.maxHeight  {    
// where절을 추가해서, 매칭시킬 에러패턴에 조건을 추가할 수 있음
    print("키가 커서 놀이기구 타는 것 불가능")
} catch {  // default문과 같음
    print("키가 작아서 놀이기구 타는 것 불가능")
    
}

// 스위프트 5.3 버전 업데이트
do {
    let isChecked = try checkingHeight(height: 100)
    print("놀이기구 타는 것 가능: \(isChecked)")
    
} catch HeightError.maxHeight, HeightError.minHeight {
// 케이스 나열도 가능해짐 switch-case문과 비슷함
    print("놀이기구 타는 것 불가능")
    
}
```

### 2. Catch 패턴 없이 처리
```swift
do {
    let isChecked = try checkingHeight(height: 100)
    print("놀이기구 타는 것 가능: \(isChecked)")
    
} catch {    // error 상수를 제공 (모든 에러가 넘어옴)
    print(error.localizedDescription)
    
    if let error = error as? HeightError {    
// 실제 우리가 정의한 구체적인 에러 타입이 아니고, 에러 타입(프로토콜)이 넘어올 뿐
        switch error {
        case .maxHeight:
            print("키가 커서 놀이기구 타는 것 불가능")
        case .minHeight:
            print("키가 작아서 놀이기구 타는 것 불가능")
        }
    }
}
```

## 에러를 던지는 함수를 처리하는 함수
> 에러를 다시 던질 수 있다.

```swift
// 에러정의
enum SomeError: Error {
    case aError
}

// 에러를 던지는 함수 정의 (무조건 에러를 던진다고 가정)
func throwingFunc() throws {
    throw SomeError.aError
}

// 일반적인 함수로 처리
func handleError() {
    do {
        try throwingFunc()
    } catch {
        print(error)
    }
}

handleError()
```

#### 1. throwing 함수로 에러 다시 던지기
> 함수 내에서 에러를 직접 처리하지 못하면, 에러를 다시 던질 수 있음.

```swift
func handleError1() throws {
    //do {
    try throwingFunc()
    //}                     
}

do {
    try handleError1()   // 에러를 받아서 처리 가능
} catch {
    print(error)
}
```
- **catch블럭이 없어도 에러를 밖으로 던질 수 있음**

#### 2. rethrowing 함수로 에러 다시 던지기 (rethrows 키워드)
>에러를 던지는 **throwing함수를 파라미터로 받는 경우**, 내부에서 다시 에러를 던지기 가능
>`rethrows` 키워드 필요 (`Rethrowing` 메서드)

```swift
// 다시 에러를 던지는 함수(방법1)
func someFunction1(callback: () throws -> Void) rethrows {
    try callback()             // 에러를 다시 던짐(직접 던지지 못함)
    // throw (X)
}


// 다시 에러를 던지는 함수(방법2) - 에러변환
func someFunction2(callback: () throws -> Void) rethrows {
    enum ChangedError: Error {
        case cError
    }
    do {
        try callback()
    } catch {   // catch구문에서는 throw (O)
        throw ChangedError.cError    // 에러를 변환해서 다시 던짐
    }
}

// 실제 에러를 다시던지는(rethrowing)함수를 처리하는 부분
do {
    try someFunction1(callback: throwingFunc)
} catch {
    print(error)
}

do {
    try someFunction2(callback: throwingFunc)
} catch {
    print(error)
}
```

## 메서드 / 생성자
> 메서드 / 생성자에 `throw` 키워드 적용
- 에러는 Throwing 함수 뿐만아니라, 메서드와 생성자에도 적용 가능
- 에러를 던질 수 있는 메서드 -> `Throwing` 메서드
- 에러를 던질 수 있는 생성자 -> `Throwing` 생성자

```swift
// 에러 정의
enum NameError: Error {
    case noName
}
// 생성자와 메서드에도 적용 가능
class Course {
    var name: String
    
    init(name: String) throws {
        if name == "" {
            throw NameError.noName
        } else {
            self.name = name
            print("수업을 올바르게 생성")
        }
    }   
}
// 에러 처리 (생성자에 대한)
do {
    let _ = try Course(name: "스위프트5")
} catch NameError.noName {
    print("이름이 없어 수업이 생성 실패하였습니다.")
}
```

#### 생성자와 메서드의 재정의
```swift
class NewCourse: Course {
    override init(name: String) throws {
        try super.init(name: name)
        
    }
}
```
- `Throwing` 메서드/생성자 -> `Throwing`메서드/생성자 재정의 가능
- `Throwing` 메서드/생성자 -> 일반 메서드/생성자 재정의 **불가능**
- 일반 메서드/생성자 -> 재정의 `Throwing` 메서드/생성자 가능
- `Throwing` 메서드/생성자 -> `Rethrosing` 메서드/생성자 재정의 가능
- `Rethrosing` 메서드/생성자 -> `Throwing` 메서드/생성자 재정의 **불가능**