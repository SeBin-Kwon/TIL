# Result Type

> 에러가 발생하는 경우, 에러를 던지지 않고 리턴 타입 자체를 Result Type으로 리턴
- 함수 실행의 성공과 실패의 정보를 함께 담아서 리턴
- Result 타입은 열거형임
	- case success(연관값)
	- case failure(연관값)
- 실제 Result타입의 내부 구현
	- `enum Result<Success, Failure> where Failure : Error`
	- 제네릭 선언

### 기존 에러 처리
```swift
// 에러 정의 (어떤 에러가 발생할지 경우를 미리 정의)
enum HeightError: Error {    //에러 프로토콜 채택 (약속)
    case maxHeight
    case minHeight
}

// throwing함수
// (에러를 던잘수 있는 함수 타입이다)
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

do {
    let _ = try checkingHeight(height: 200)
    print("놀이기구 타는 것 가능")
} catch {
    print("놀이기구 타는 것 불가능")
}
```

## Result 타입을 활용한 에러 처리
> 에러 처리 코드가 굉장히 깔끔해진다.
```swift
// 에러는 동일하게 정의되어 있다고 가정
// Result타입에는 성공/실패했을 경우에 대한 정보가 다 들어있음
func resultTypeCheckingHeight(height: Int) -> Result<Bool, HeightError> {
    if height > 190 {
        return Result.failure(HeightError.maxHeight)
    } else if height < 130 {
        return Result.failure(HeightError.minHeight)
    } else {
        if height >= 160 {
            return Result.success(true)
        } else {
            return Result.success(false)
        }
    }
}

// 리턴값을 받아서
let result = resultTypeCheckingHeight(height: 200)

// 처리
switch result {
case .success(let data):
    print("결과값은 \(data)입니다.")
case .failure(let error):
    print(error)
}
```
- `throws` 키워드가 필요없음
- `< >`안에 성공했을 때, 실패했을 때의 구체적인 타입 작성
- `throw`가 아닌 `return` 사용
- Result라는 열거형 안에 case값 선택 후, 연관값으로 `HeightError`라는 열거형 안에 case값 작성
- `try` 키워드가 필요없음
- `do-catch`문 필요없이 `switch`문으로 처리 가능
	- `case .success(let data)`으로 연관값 바인딩 가능

### Result 타입의 다양한 활용
> Result 타입에는 여러 메서드가 존재함

##### get()
> 결과값을 `throwing` 함수처럼 변환 가능한 메서드 (Success 밸류를 리턴)
```swift
do {
    let data = try result.get()
    print("결과값은 \(data)입니다.")
} catch {
    print(error)
}

```
- 다시 error를 던지는 함수처럼 바뀌어서 `try`와 `do-catch`문을 사용해야 한다.

### Result 타입을 왜 쓸까?
- 성공 / 실패의 경우를 깔끔하게 처리가 가능한 타입
- 에러 처리에 대한 다양한 처리 방법에 대한 옵션을 제공
	- 기존의 에러처리 패턴을 완전히 대체 목적 X

## 네트워킹 코드에서 Result 타입

### 에러 정의
```swift
enum NetworkError: Error {
    case someError
}
```

### Result 타입 사용 전
```swift
// 튜플타입을 활용, 데이터 전달
func performRequest(with url: String, completion: @escaping (Data?, NetworkError?) -> Void) {
    
    guard let url = URL(string: url) else { return }
    
    URLSession.shared.dataTask(with: url) { (data, response, error) in
        if error != nil {
	        // 에러가 발생했음을 출력
            print(error!)
            // 에러가 발생했으니, nil 전달
            completion(nil, .someError)
            return
        }
        
        guard let safeData = data else {
	        // 안전하게 옵셔널 바인딩을 하지 못했으니, 데이터는 nil 전달
            completion(nil, .someError)
            return
        }
        completion(safeData, nil)
    }.resume()
}

performRequest(with: "주소") { data, error in
    // 데이터를 받아서 처리
    if error != nil {
        print(error!)
    }
    // 데이터 처리 관련 코드
}
```

### Result 타입 사용 후
```swift
func performRequest2(with urlString: String, completion: @escaping (Result<Data,NetworkError>) -> Void) {
    
    guard let url = URL(string: urlString) else { return }
    
    URLSession.shared.dataTask(with: url) { (data, response, error) in
        if error != nil {
	        // 에러가 발생했음을 출력
            print(error!)
            // 실패 케이스 전달
            completion(.failure(.someError))
            return
        }
        
        guard let safeData = data else {
	        // 실패 케이스 전달
            completion(.failure(.someError))
            return
        }
	    // 성공 케이스 전달
        completion(.success(safeData))
    }.resume()
}

performRequest2(with: "주소") { result in
    switch result {
    case .failure(let error):
        print(error)
    case .success(let data):
        // 데이터 처리 관련 코드
        break
    }
}
```
- 이미 열거형 타입이라고 구체적으로 명시를 해줬기 때문에 열거형 앞부분이 생략 가능하다.
- 파라미터를 result로 하나만 받아서 처리할 수 있다.