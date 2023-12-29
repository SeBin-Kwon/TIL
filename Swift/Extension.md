# Extension

> Swift의 익스텐션은 구조체, 클래스, 열거형 등 타입에 **새로운 기능을 추가** 할 수 있는 기능이다.

- 모든 타입에 확장이 가능한 형태이다. (Int, Array, Class 등)
- **타입 이름만 알고 있다면 확장이 가능하다. (타입의 자세한 구현부는 몰라도 된다.)**
- 새로운 기능을 추가하는 건 가능하지만, **기존에 있던 기능들을 재정의 하는 것은 불가능하다.**
- **메서드 형태만 가능**, 저장 속성은 확장 불가능하다.

```swift
extension 확장할 타입 이름 {
	// 타입에 추가될 새로운 기능 구현
}
```

- 추가적으로 다른 프로토콜을 채택할 수 있도록 확장할 수 있다.

```swift
extension 확장할 타입 이름: 프로토콜1, 프로토콜2... {
	// 프로토콜 요구사항 구현
}
```

`Int` 형을 확장시켜 `isEven`, `isOdd`라는 연산 프로퍼티를 추가할 수 있다.
그 후, 자유롭게 `Int` 형의 어떤 인스턴스에도 해당 프로퍼티를 사용할 수 있다.


```swift
extension Int {
	var isEven: Bool {
    	return self % 2 == 0
    }
	var isOdd: Bool {
		return self % 2 == 1
    }
}

print(1.isEven) // false
print(2.isEven) // true
print(1.isOdd) // true
print(2.isOdd) // false
```

메서드 및 이니셜라이저도 확장이 자유롭게 가능하다.

```swift
extension Int {
	func multiply(by n: Int) -> Int {
    	return self * n
    }
}

print(3.multiply(by: 2)) // 6
print(4.multiply(by: 5)) // 20
```

ContentView가 너무 길어져서 코드 관리가 쉽지 않을 때, ContentView 안에 서브 뷰로 따로 빼주거나 **익스텐션을 만들어서 빼줄 수 있다.**

```swift
struct ContentView: View {
	var body: some View {
	    // 타이틀 뷰
    	titleView 
    }
}

extension ContentView {
	// 타이틀 뷰
    var titleView: some View {
    	HStack {
        	Text("오늘 할 일")
        }
    }
}
```

