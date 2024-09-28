# Delegate Pattern

> 객체와 객체간의 커뮤니케이션을 돕는 패턴이다.

#### 텍스트필드 <--> 뷰컨트롤러
두 객체가 의사소통이 되려면 **뷰컨트롤러가 해당 프로토콜을 채택해야한다.**

### 구조
텍스트필드(유저와 상호작용) **---> 동작 전달 --->** 뷰컨트롤러
- 유저의 입력 시점, 입력을 허용할지 말지, 엔터키가 눌렸을 때 다음 동작을 허락할지 말지 등등을 전달함.
	- 선택적으로 메서드 구현 가능함

## 예시
### 프로토콜 정의
> 텍스트필드 프로토콜에 해당한다.
```swift
protocol RemoteControlDelegate {
    func channelUp()
    func channelDown()
}
```

### 클래스 정의
> 리모콘은 텍스트필드를, TV는 뷰컨트롤러 역할을 맡는다.
```swift
// 리모콘 클래스(텍스트필드의 역할 - 직접적으로 유저와 커뮤니케이션)
class RemoteControl {
    var delegate: RemoteControlDelegate?
    func doSomething() {
        print("리모콘의 조작이 일어나고 있음")
    }
    func channelUp() {   // 어떤 기기가 리모콘에 의해 작동되는지 몰라도 됨
        delegate?.channelUp()
    }
    func channelDown() {   // 어떤 기기가 리모콘에 의해 작동되는지 몰라도 됨
        delegate?.channelDown()
    }
}

// TV 클래스(뷰컨트롤러의 역할 - 리모콘과 커뮤니케이션)
class TV: RemoteControlDelegate {
    func channelUp() {
        print("TV의 채널이 올라간다.")
    }
    func channelDown() {
        print("TV의 채널이 내려간다.")
    }

}
```
- 이때 **직접적으로 유저와 커뮤니케이션하는 객체**는 각각의 **프로토콜 옵셔널 타입으로 `delegate` 속성을 갖는다.**
- 또한 리모컨과 커뮤니케이션하는 TV 객체는 해당 프로토콜을 채택해야한다. -> 그래야 해당 프로토콜의 메서드를 구현 및 사용 가능

### 인스턴스 정의 및 메서드 실행
```swift
let remote = RemoteControl()
let samsungTV = TV()

remote.delegate = samsungTV

remote.channelUp()        // 리모콘 실행 ====> delegate?.channelUp()
remote.channelDown()      // 리모콘 실행 ====> delegate?.channelDown()
```
- 리모컨 인스턴스의 `delegate` 속성에는 TV 인스턴스인 `samsungTV`로 설정한다.
	- 해당 인스턴스는 `RemoteControlDelegate` 프로토콜을 채택하고 있으므로 같은 타입이다.
- `remote`의 `channelUp` 함수 실행 -> `delegate`(`samsungTV)`의 `channelUp` 함수 실행

```swift
// SmartPhone 클래스(뷰컨트롤러의 역할 - 리모콘과 커뮤니케이션)
class SmartPhone: RemoteControlDelegate {
    init(remote: RemoteControl) {
        remote.delegate = self       // remote.delegate = smartPhone
    }
    func channelUp() {
        print("스마트폰의 채널이 올라간다.")
    }
    func channelDown() {
        print("스마트폰의 채널이 내려간다.")
    }
}

let smartPhone = SmartPhone(remote: remote)
remote.channelUp()        // 리모콘 실행 ====> delegate?.channelUp()
remote.channelDown()      // 리모콘 실행 ====> delegate?.channelDown()
```
- `init`으로 초기화할 때 미리 설정할 수 있다.
- `remote`의 `delegate` 속성이 `samsungTV`에서 `SmartPhone`으로 바뀌었으므로 메서드도 `SmartPhone`의 메서드가 실행된다.


## 왜 굳이 프로토콜 타입으로 정의해서 대신 전달할까?
- 애플 입장에선 개발자가 어떤 이름의 클래스를 정의할지 알 수 없음
- 보통의 이름을 가진 프로토콜 타입으로 정의해서 채택하여 사용하도록 함
	- 클래스가 어떤 이름을 가져도 채택만 하면 사용 가능해짐
- 텍스트필드의 내부적 구현은 숨겨져있어 직접 전달이 불가능
