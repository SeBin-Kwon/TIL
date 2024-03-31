# Never 타입과 검증 함수

## Never 타입
> 절대 CPU 실행의 제어권을 돌려주지 않음
- 함수의 return의 의미
	- 1.값을 리턴
	- 2. 함수 내부로 전달했던 CPU 실행의 제어권을 다시 돌려줌(리턴)
- **CPU 실행의 제어권을 돌려주지 않아 의도적으로 에러를 발생해 앱을 종료시킴**
- 임시적인 타입
	- 내부가 빈 열거형으로 선언
	- 인스턴스를 생성할 수 없음 (Uninhabited Type)

```swift
func crashAndBurn() -> Never {
    fatalError("앱의 해킹이 발견됨")
}

print("1")
crashAndBurn()
print("2") // 절대 실행되지 않음
```

### Nonreturning(논리터닝) 함수
> Never 타입을 리턴 타입으로 갖는 함수
- 제어권을 전달하지 않음 (함수를 호출했던 코드로 다시 제어권을 전달하지 않음)
- 함수 내부에서 프로그램을 종료시켜야 함 (ex: fatalError())
- 항상 에러를 던져서 catch문에서 처리하도록 해야 함 (제어권을 catch문으로)
```swift
// 1) 에러 정의
enum SomeError: Error {
    case aError
    case bError
}

// 2) 에러를 던지는 함수의 정의
func someThrowingErrorFuncion() throws -> Never {
    if true {
        throw SomeError.aError
    } else {
        throw SomeError.bError
    }
}

// 3) 에러를 던지는 함수의 실행
do {
    try someThrowingErrorFuncion()
} catch {
    print(error)
}
```

#### 왜 사용할까?
- 런타임에 발생할 수 있는 에러를 미리 발견하고, 검증/테스트 하기 위함
- 경우에 따라 가벼운 에러라면 실제 앱을 출시(release)시에는 해당 코드를 삭제하여야함
	- 삭제하지 않으면 앱이 꺼질 수 있어서 사용성이 안좋은 앱으로 평가받을 수 있음

## 디버깅 (검증) 함수
> 디버깅 (테스트/검증)을 위해 일부러 앱을 중지 시키는 함수
### fatalError()
- 리턴형: Never 타입
- 디버그 모드, 릴리즈 모드, 베타 테스터 모드 다 동작함
	- 잘 안씀
### assert()
> 디버그 모드에서만 동작
- 실제 앱을 출시 시, 일부러 앱을 종료시킬 정도의 상황은 아니지만 디버그 모드에서 검증해야 할 때 사용
- `assertionFailure()`는 무조건 false일 때 동작
```swift
func enterWrongValue1() {
    let someWrongInput = -1
    assert(someWrongInput > 0, "유저가 값을 잘못 입력")
}
//enterWrongValue1()

func enterWrongValue2() {
    let someWrongInput = -1
    
    if someWrongInput > 0 {
        // 정상적으로 처리하는 코드
        
    } else {
        assertionFailure("유저가 값을 잘못 입력")
    }
}
//enterWrongValue2()
```
### precondition()
> 디버그 모드, 릴리즈 모드 둘 다 동작함
- 실제 앱을 출시 시에도 앱을 의도적으로 종료시켜야 하는 상황일 때 사용
- `preconditionFailure()`는 무조건 false일 때 동작
```swift
func appUpdateCheck1() {
    let update = false
    precondition(update, "앱을 업데이트 하지 않음")
}
//appUpdateCheck1()

func appUpdateCheck2() {
    let update = false
    
    if update {
        // 앱을 업데이트 했을때, 정상적으로 실행할 코드
        
    } else {
        preconditionFailure("앱을 업데이트 하지 않음")
    }
}
//appUpdateCheck2()
```