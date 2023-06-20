# Swift의 상속

> 상속이란 한 클래스가 가지고 있는 프로퍼티와 메소드를 다른 클래스에게 그대로 승계해주는 것

- Swift의 상속은 **클래스, 프로토콜** 에서만 가능하다.
- **`enum`(열거형), 구조체는 상속이 불가능하다.**
- Swift는 **단일 상속만 가능**하다.
	단 하나의 클래스만 상속이 가능하지만 프로토콜은 여러개 채택 가능
- 상속 받은 클래스도 새로운 자식 클래스에게 상속이 가능하다.

### 클래스 선언 및 인스턴스의 메서드, 프로퍼티 접근 방법
```swift
class Vehicle {
    // 가변 저장 프로퍼티
    var currentSpeed = 0.0
    
    // 연산 프로퍼티
    var description: String {
        return "traveling at \(currentSpeed) miles per hour"
    }
    
    func makeNoise() {
        // do nothing
    }
}

// Vehicle 타입의 인스턴스 생성
let car = Vehicle()
print("Vehicle: \(car.description)")
// Vehicle: traveling at 0.0 miles per hour
```

## 상속 방법

```swift
class 새로운 클래스 이름: 상속하는 부모 클래스 이름 {
    /* 구현부 */
}
```
```swift
class Bicycle: Vehicle {
    var hasBasket = false
}
```
Bicycle 클래스는 `currentSpeed`와 `description`과 `makeNoise` 메소드까지 모두 얻게 된다.

```swift
let bicycle = Bicycle()

bicycle.hasBasket = true
bicycle.currentSpeed = 15.0

print("Bicycle: \(bicycle.description)")
// Bicycle: traveling at 15.0 miles per hour
```
Bicycle 클래스가 가지고 있는 `hasBasket`이라는 저장 프로퍼티 뿐만 아니라 Vehicle 클래스에만 있던 프로퍼티와 메소드에도 접근이 가능하다.

## Override

> 부모(상위) 클래스에서 자식(하위) 클래스로 물려준 인스턴스나 메소드를 본인 클래스에 맞게 재정의 하는 것

```swift
override func 메소드명 () {

}
```
새로 정의하고 싶은 메소드명을 적고, 구현하고 싶은 내용을 작성한다. **메소드명은 부모 클래스와 동일해야 한다.**

```swift
class Vehicle {
    var currentSpeed = 0.0
    
    var description: String {
        return "traveling at \(currentSpeed) miles per hour"
    }
    
    func makeNoise() {
        print("뛰뛰")
    }
}

class Train: Vehicle {
    override func makeNoise() {
        print("빵빵")
    }
}

let vehicle = Vehicle()
vehicle.makeNoise()
// 뛰뛰
let train = Train()
train.makeNoise()
// 빵빵
```

## Super

> super.(메소드이름)을 호출하면 부모 클래스의 메소드를 가져올 수 있다.

```swift
class Vehicle {
    var currentSpeed = 0.0
    
    var description: String {
        return "traveling at \(currentSpeed) miles per hour"
    }
    
    func makeNoise() {
        print("뛰뛰")
    }
}

class Car: Vehicle {
    override func makeNoise() {
        super.makeNoise()
        print("빵빵뿡뿡")
    }
}

let car = Car()
car.makeNoise()
// 뛰뛰
// 빵빵뿡뿡
```
`super.makeNoise`를 통해 부모 클래스의 메서드를 가져와서 추가로 메서드를 재정의 한 결과 위와 같이 출력된다.

## Final

> 자식 쪽에서 재정의되면 안될 내용의 메서드나 프로퍼티가 있는 경우 final를 통해 막을 수 있다.

```swift
class Vehicle {
    final var currentSpeed = 0.0
}

class AutomaticCar: Car {
    override var currentSpeed: Double {
        didSet {
        	print(oldValue)
            gear = Int(currentSpeed / 10.0) + 1
        }
    } // 에러 발생
}
```

위와 같은 상황은 `currentSpeed`가 `final`로 정의되었기 때문에 재정의가 불가능하다.