# Timer

> 타이머 앱 만들기

## Slider 슬라이더

```swift
@IBOutlet weak var slider: UISlider!

slider.setValue(0.5, animated: true)
```
- `slider.value`를 통해 직접 value에 접근할 수 있고
- `setValue`로 value를 바꿀 수도 있다. 0.5면 가운데에 위치하게 된다.
	- `animated`로 애니메이션 여부 결정 가능

## 함수를 매 초 실행시키는 법 (Timer)
### 클로저 활용 방법

```swift
timer?.invalidate() // 타이머 비활성화
timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { [self] _ in
	// 매 초 반복할 코드
	if number > 0 {
		number -= 1
		slider.value = Float(number) / Float(60)
		mainLabel.text = "\(number) 초"
	} else {
		number = 0
		mainLabel.text = "초를 선택하세요"
		timer?.invalidate()
	}
}
```


```swift
... { [weak self] _ in
	 if self?.number ...
	}
```
- `weak self`라면 `self?.number` 이렇게 모든 곳에 옵셔널 체이닝을 해야한다.
  - `weak self` 와 캡처리스트 관련 내용은 [ARC](../Swift/ARC.md)에서 확인
```swift
... { [self] _ in
	 if number ...
	}
```
- `weak`을 빼면 `self?`도 빼도 된다. 
- `[self]`를 빼면 모든 `number` 앞에 `self`를 붙여야한다.

### 클로저에서 왜 `weak` 키워드를 안 붙여도 되는지?
현재 `timer` 변수는 `weak`으로 선언되어 있다.
```swift
weak var timer: Timer?
```

하지만 `weak` 없이 그냥 선언하게 된다면 `timer`는 `Timer`를 강하게 가르키게 된다.
```swift
timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true)
```

이때 `Timer`는 클로저를 가져서 클로저를 강하게 가르킨다.
```swift
timer = Timer.scheduledTimer ... { [self] _ in
	 if number ...
	}
```

그리고 `self`는 인스턴스 즉, `timer`를 의미하므로 클로저가 `timer`를 강하게 가르키면서 강한 참조 사이클이 발생하게 된다.

그러므로 `timer` 변수를 선언할 때 `weak`을 붙이거나, 클로저에서 `weak`을 붙이거나 둘 중 하나만 해도 사이클을 끊을 수 있다.

### 셀렉터 활용 방법
```swift
@IBAction func startButtonTapped(_ sender: UIButton) {
	timer?.invalidate()
	timer = Timer.scheduledTimer(timeInterval: 1.0, target: self, selector: #selector(doSomethingAfter1Second), userInfo: nil, repeats: true)
}

@objc func doSomethingAfter1Second() {
	if number > 0 {
		number -= 1
		slider.value = Float(number) / Float(60)
		mainLabel.text = "\(number) 초"
	} else {
		number = 0
		mainLabel.text = "초를 선택하세요"
		timer?.invalidate()
		AudioServicesPlayAlertSound(SystemSoundID(1322))
	}
}
```
- `@objc` 키워드를 붙인 함수를 따로 선언해서 해당 함수를 실행하도록 시킨 것이다. 위 클로저 방식과 동일하게 작동한다.
## 시스템 소리 나게 하는 법
> How to play system sound in swift

```swift
import AVFoundation
AudioServicesPlayAlertSound(SystemSoundID(1322))
```