# BMI 계산기

- UI 만들고 컨트롤 누르고 코드 연결
- **텍스트필드 -> 델리게이트 패턴**
	- [TextField (두번째 앱)](TextField.md)
	- [델리게이트 패턴 (Delegate Pattern)](DelegatePattern.md)

## 1. ViewController를 확장해서 UITextFieldDelegate 프로토콜 채택하기
> **TextField를 사용하려면 뷰 컨트롤러에서 `UITextFieldDelegate` 프로토콜을 채택해야한다.**

```swift
extension ViewController: UITextFieldDelegate {
}
```

```swift
override func viewDidLoad() {
	super.viewDidLoad()
	heightTextField.delegate = self
}
```
- TextField 속성의 delegate를 self로 설정
- 텍스트필드의 대리자를 뷰 컨트롤러로 지정해주는 코드 입력
	- 유저에게 입력받는 텍스트필드 -> 결과값 -> 뷰컨트롤러에 전달
	- 뷰컨트롤러가 대리자가 되도록 설정해줘야함.


## 2. UI 설정하기
```swift
func makeUI() {
	heightTextField.delegate = self
	weightTextField.delegate = self
	mainLabel.text = "키와 몸무게를 입력해주세요"
	calculateButton.clipsToBounds = true
	calculateButton.layer.cornerRadius = 5
	calculateButton.setTitle("BMI 계산하기", for: .normal)
	heightTextField.placeholder = "cm단위로 입력해주세요"
	weightTextField.placeholder = "kg단위로 입력해주세요"
}
```

### 버튼 모서리 둥글게 깎기
```swift
calculateButton.`clipsToBounds` = true
calculateButton.layer.cornerRadius = 5
```
- 반드시 `clipsToBounds`를 `true`로 하는걸 빼놓지 않기



## 3. 두번째 화면 코드 연결하기
- Cocoa Touch Class 파일 생성 -> 파일명 `SecondViewController`
- 스토리보드 가서 두번째 화면 클릭
- 오른쪽 패널 네번째 `Coustom Class` 부분에서 `SecondViewController` 입력 및 엔터