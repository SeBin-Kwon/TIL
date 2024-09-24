# 오토 레이아웃 (Auto Layout)
> `constraint(equalTo:  , constant:)`를 기본적으로 사용한다.

## 코드 미리보기
```swift
emailTextFieldView.translatesAutoresizingMaskIntoConstraints = false
        emailTextFieldView.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 30).isActive = true
        emailTextFieldView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -30).isActive = true
        emailTextFieldView.topAnchor.constraint(equalTo: view.topAnchor, constant: 200).isActive = true
        emailTextFieldView.heightAnchor.constraint(equalToConstant: 40).isActive = true
```

## 기본적으로 반드시 써야할 코드
> 자동으로 오토레이아웃 잡아주던걸 **수동으로 잡기 위해 false로 꺼줘야 한다.**
```swift
emailTextFieldView.translatesAutoresizingMaskIntoConstraints = false
```

### 왼쪽 앵커
```swift
emailTextFieldView.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 30).isActive = true
```
- `leadingAnchor` 왼쪽 `.constraint` 제약
- `equalTo: ` 어떤 뷰를 기준으로 띄울 것인지? -> `view.leadingAnchor` 맨 왼쪽 기본 뷰 기준
- `constant: ` 몇을 띄울 것인지? -> 30
- `.isActive` 활성화 할지말지 -> `true`로 설정

이건 외울 수 밖에 없다.

### 오른쪽 앵커
```swift
emailTextFieldView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -30).isActive = true
```
- 뒤쪽에서 맞출땐 `-30`으로 해준다.

### 위쪽 앵커
```swift
emailTextFieldView.topAnchor.constraint(equalTo: view.topAnchor, constant: 200).isActive = true
```

### 높이 앵커
> **높이는 기준이 없다 -> `constraint(equalToConstant: )`를 선택해준다.**
```swift
emailTextFieldView.heightAnchor.constraint(equalToConstant: 40).isActive = true
```

### 아래쪽 앵커
```swift
emailTextFieldView.bottomAnchor
```

### 가운데 앵커
```swift
emailTextFieldView.centerYAnchor
```

## isActive가 너무 반복되는데? `NSLayoutConstraint` 사용하기

### 기존 코드
```swift
func makeUI() {
	view.addSubview(emailTextFieldView)
	
	emailInfoLabel.translatesAutoresizingMaskIntoConstraints = false
	
	emailInfoLabel.leadingAnchor.constraint(equalTo: emailTextFieldView.leadingAnchor, constant: 8).isActive = true
	emailInfoLabel.trailingAnchor.constraint(equalTo: emailTextFieldView.trailingAnchor, constant: 8).isActive = true
	emailInfoLabel.centerYAnchor.constraint(equalTo: emailTextFieldView.centerYAnchor).isActive = true
	
	emailTextField.translatesAutoresizingMaskIntoConstraints = false
	
	emailTextField.leadingAnchor.constraint(equalTo: emailTextFieldView.leadingAnchor, constant: 8).isActive = true
	emailTextField.trailingAnchor.constraint(equalTo: emailTextFieldView.trailingAnchor, constant: 8).isActive = true
	emailTextField.topAnchor.constraint(equalTo: emailTextFieldView.topAnchor, constant: 15).isActive = true
	emailTextField.bottomAnchor.constraint(equalTo: emailTextFieldView.bottomAnchor, constant: 2).isActive = true
}
```

### 배열 형태로 변경
> 좀 더 코드가 깔끔해진다.
```swift
func makeUI() {
	view.addSubview(emailTextFieldView)
	
	emailInfoLabel.translatesAutoresizingMaskIntoConstraints = false
	emailTextField.translatesAutoresizingMaskIntoConstraints = false
	
	NSLayoutConstraint.activate([
		emailInfoLabel.leadingAnchor.constraint(equalTo: emailTextFieldView.leadingAnchor, constant: 8),
		emailInfoLabel.trailingAnchor.constraint(equalTo: emailTextFieldView.trailingAnchor, constant: 8),
		emailInfoLabel.centerYAnchor.constraint(equalTo: emailTextFieldView.centerYAnchor),
		emailTextField.leadingAnchor.constraint(equalTo: emailTextFieldView.leadingAnchor, constant: 8),
		emailTextField.trailingAnchor.constraint(equalTo: emailTextFieldView.trailingAnchor, constant: 8),
		emailTextField.topAnchor.constraint(equalTo: emailTextFieldView.topAnchor, constant: 15),
		emailTextField.bottomAnchor.constraint(equalTo: emailTextFieldView.bottomAnchor, constant: 2)
	])
}
```
- 기존 코드에서 `isActive = true` 이 부분을 모두 삭제하고 `NSLayoutConstraint`에 `activate` 메서드를 사용하여 배열로 제약들을 모두 넘겨준다.