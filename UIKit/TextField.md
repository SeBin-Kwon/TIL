# TextField(텍스트필드) 사용법
```swift
textField.keyboardType = .emailAddress // 키보드 스타일
textField.placeholder = "이메일 입력" // 플레이스홀더
textField.borderStyle = .roundedRect // 선 스타일
textField.clearButtonMode = .always // 텍스트 다 지워주는 엑스 버튼
textField.returnKeyType = .next // 키보드 return 버튼 변경
```

| textField.clearButtonMode = .always                          | textField.returnKeyType = .next                              | textField.returnKeyType = .go                                | textField.returnKeyType = .google                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![[simulator_screenshot_504F209C-85BE-45A6-AB72-2484ABD59375.png\|200]] | ![[simulator_screenshot_D1936122-8457-4420-81E7-F1E8C15CD22E.png\|200]] | ![[simulator_screenshot_1DA998E7-FA38-4B5A-845C-D896851DEFDF.png\|200]] | ![[Simulator Screenshot - iPhone 15 - 2024-08-01 at 00.11.36.png\|200]] |
## UITextFieldDelegate 프로토콜
> **TextField를 사용하려면 먼저 뷰 컨트롤러에서 `UITextFieldDelegate` 프로토콜을 채택해야한다.**

```swift
class ViewController: UIViewController, UITextFieldDelegate {
    @IBOutlet weak var textField: UITextField!
```

그리고 **TextField 속성에 delegate가 있는데 이것을 self로 설정해준다.**
```swift
override func viewDidLoad() {
	super.viewDidLoad()
	textField.delegate = self
	setup()
}
```
- 텍스트필드와 뷰 컨트롤러는 따로 존재하는데, 위 코드는 텍스트필드의 대리자를 뷰 컨트롤러로 지정해주는 코드이다.

### 델리게이트 패턴
> 텍스트필드는 유저와 상호작용해야 하기 때문에 뷰 컨트롤러와는 따로 존재한다. 
> **-> 직접적인 동작은 텍스트필드가 하고 델리게이트는 이 동작을 뷰 컨트롤러에 전달해준다.**

[[델리게이트 패턴 (Delegate Pattern)]]

## UITextFieldDelegate 프로토콜 관련 메서드
> `UITextFieldDelegate` 프로토콜을 채택하면 선택적으로 구현 가능한 메서드들이다.
### 1. 텍스트필드의 입력을 시작할 때 호출되는 메서드 (시작할지 말지의 여부 허락하는 것)
```swift
func textFieldShouldBeginEditing(_ textField: UITextField) -> Bool {
	return true
}
```

### 2. 텍스트 입력을 시작한 시점을 알려주는 메서드
> 반환 타입이 `Bool` 타입이 아님 -> 보통 시점을 알려주는 메서드임
```swift
func textFieldDidBeginEditing(_ textField: UITextField) {
	print("유저가 텍스트필드의 입력을 시작함.")
}
```

### 3. 클리어 버튼이 동작할지 말지 허락 여부 메서드
```swift
func textFieldShouldClear(_ textField: UITextField) -> Bool {
        return true
    }
```

### 4. 텍스트필드 내용이 한글자 한글자 입력되거나 지워질 때 호출되는 메서드 (허락)
```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        print(string)
        return true
    }
```
- 입력된 string이 하나하나 출력됨
- false하면 입력되지 않음

#### 4-1. 텍스트필드 최대 입력 글자 제한하기 (10글자)
```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
	if (textField.text?.count)! + string.count > 10 {
		return false
	} else {
		return true
	}
}
```
#### 4-2. 텍스트필드 최대 입력 제한  + 숫자 입력 막기
```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
	if Int(string) != nil {
		return false
	} else {
		guard let text = textField.text else { return true }
		let newLength = text.count + string.count - range.length
		return newLength <= 10
	}
}
```

### 5. 엔터키가 눌러지면 다음 동작을 허락할지 말지하는 메서드
```swift
func textFieldShouldReturn(_ textField: UITextField) -> Bool {
	return true
}
```
#### 5) 예시
```swift
func textFieldShouldReturn(_ textField: UITextField) -> Bool {
	print(#function)
	if textField.text == "" {
		textField.placeholder = "Type Something!"
		return false
	} else {
		return true
	}
}
```
- 텍스트필드가 비어있는채로 엔터키를 눌렀을 때, 뭔가를 입력하라고 플레이스홀더의 텍스트를 변경할 수 있다.

### 6. 텍스트필드의 입력이 끝날 때 호출되는 메서드 (끝날지 말지를 허락)
```swift
func textFieldShouldEndEditing(_ textField: UITextField) -> Bool {
	return true
}
```

### 7. 텍스트필드 입력이 실제 끝났을 때의 시점을 알려주는 메서드
```swift
func textFieldDidEndEditing(_ textField: UITextField) {
	print("유저가 텍스트필드의 입력을 끝냄.")
}
```

## 참고) 함수 이름 출력하기
```swift
func textFieldShouldBeginEditing(_ textField: UITextField) -> Bool {
	print(#function)
	return true
}
```
- print()에 `#function`을 넣으면 해당 함수의 이름이 출력된다.

## Responder (응답자 / 응답 객체)
**`UIWindow` : 앱의 화면, 실제 터치 등 화면의 입력을 받아들이는 객체**
- First 응답 객체를 지정 해줌 (화면에서 가장 먼저 반응할 객체)
- **텍스트필드가 First 응답 객체가 된다면? -> 바로 키보드가 올라옴**
	- 유저한테 먼저 반응할 것을 포커스 시켜줌

### 화면에서 키보드가 바로 올라오게 하기
```swift
textField.becomeFirstResponder()
```
- 텍스트필드를 First Responder로 설정하는 메서드
### Done 버튼 누르면 키보드 내려가게 하기
```swift
textField.resignFirstResponder()
```
- First Resoponder에서 사임하는 메서드

### 빈 공간을 터치하면 키보드 내려가게 하기
> 화면의 탭을 감지하는 메서드
```swift
override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
	self.view.endEditing(true)
	// textField.resignFirstResponder()
}
```
- `touchesBegan`이라는 메서드는 이미 상위의 뷰컨트롤러에 정의되어 있지만, `override`로 재정의하고 있다.
- `self.view.endEditing(true)`는 뷰 전체를 완전히 끝내겠다는 의미
- `textField.resignFirstResponder()`와 동일하게 동작하지만 얘는 텍스트필드만 끝냄

### 백그라운드 컬러 바꾸는 법

```swift
override func viewDidLoad() {
	super.viewDidLoad()
	setup()
}

func setup() {
	view.backgroundColor = UIColor.gray // 원하는 컬러로 바꾸기
}
```

- `view`는 뷰컨트롤러(`ViewController`) 내부에 있는 뷰를 의미