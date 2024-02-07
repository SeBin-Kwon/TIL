# 동시성(Concurrency) 프로그래밍

## 네트워크 통신과 비동기 처리
> 서버에 데이터를 요청하는 일은 부하가 많이 걸리는 일
- 아이폰은 1초에 60번 화면을 다시 그린다. -> 메인 쓰레드 담당
- 비동기 처리를 하지 않으면 이런 메커니즘을 제대로 동작하지 못해서 버벅거리게 됨.

### 왜 동시성 프로그래밍이 필요할까?
> 메인 쓰레드만 사용할 경우 앱이 버벅임
- 특히 메인 쓰레드는 유저의 화면과 관련된 일을 처리하는 쓰레드이기 때문에 일이 많으면 많을 수록 버벅이고 안좋음
	- 메인 쓰레드는 1초에 60번씩 화면을 다시 그려서(60Hz) 앱의 화면이 움직이는 것처럼 보이도록 만드는 아주 중요한 역할을 담당함
	- 그래서 네트워킹 코드와 같이 오래걸리는 일은 메인 쓰레드에서 실행시키면 안됨, 최대한 메인 쓰레드와 분리시켜서 다른 쓰레드에서 처리할 수 있도록 해야함
- 그래서 동시성 프로그래밍은 성능, 반응성, 최적화와 관련이 있음.
	- GCD / Operation

### CPU
#### 코어(Core) / 쓰레드(Thread) / 클럭(Clock) 개념
- 코어: 입
- 쓰레드: 손
- 음식을 먹으려면 입이 필요함
- 손으로 음식을 집어 입에 넣을 수 있음
- 다른 손으로 미리 다른 음식을 집을 수 있음
##### 4코어 8쓰레드
- 하이퍼쓰레딩 기술
- 1코어에 2개의 쓰레드
	- 8개의 코어가 있는 효과
- 8개의 물리적인 계산기가 있음

#### 소프트웨어적인 Thread
> NSThread라는 객체
- 물리적인 Thread(CPU코어의 쓰레드)와 소프트웨어적인 Thread는 얼추 비슷하면서 약간 다름
	- 물리적인 Thread는 실제 물리적인 계산을 실행
	- 소프트웨어적인 Thread는 객체임
- 쓰레드에서 작업들을 처리함
- 여러 쓰레드 객체들을 만들 수 있고 그 중 1번 쓰레드가 메인 쓰레드임

## 앱의 시작 과정과 동작 원리
> 메인쓰레드(1번 쓰레드)의 역할 알아보기
#### Launch Time
1. 앱 아이콘 터치
2. `main()` -> C기반의 언어 main() 함수 존재 / UIKit이 직접 관리(내부에서 알아서 동작함)
3. `UIApplicationMain()` -> 앱을 관리하는 앱 객체를 UIKit이 생성
4. Load main UI file -> 앱 객체가 화면 준비
5. First initialization
6. Restore UI state
7. Final initialization
#### Running
8. Activate the app
9. **Event Loop -> 런루프(runloop)를 생성**
	- 무한 반복문이 이벤트들을 처리

- 앱이 시작될 때 앱을 담당하는 **메인 런루프(반복문)**가 생김
- **이벤트(터치, 핀치줌, 화면 가로로 돌리기 등) 처리를 담당** -> 어떤 함수를 실행시킬 것인지 선택 / 실행
- 함수 등의 실행의 결과를 화면에 보여줘야함 -> **화면 다시 그림**(항상 X, 화면 다시 그리는 일이 필요할 때, 1초에 60번만 그리면 됨) 
	  ->**Thread 1(메인 쓰레드)에서 담당**
	- 직접 그리진 않고 내부적인 메커니즘에 의해 렌더링 프로세스를 가짐
		  (코어애니메이션 -> 렌더서버 -> GPU -> 표시)

오래걸리는 네크워크 작업을 메인 쓰레드가 하게 될 경우 버벅거리게 된다.
- **분산 처리로 해결 -> ==비동기 처리 / 동시성 프로그래밍 -> 성능 / 반응성 / 최적화와 관련==**

## 동시성 처리
> iOS에서의 동시성을 처리하는 방법
- **작업(Task)** 을 **"대기행렬(Queue)"** 에 보내기만 하면, **iOS(운영체제시스템)** 가 알아서 **여러 쓰레드**로 나눠서 **분산처리(동시적 처리)** 를 한다.
### Queue(대기열)
> 대기열의 개념을 이용해서 분산처리
- 먼저 작업을 큐로 보냄
- 큐는 해당 작업을 보고 그에 맞게 쓰레드 객체 생성
- 그 즉시 큐는 다른 쓰레드에 작업을 배치(선입선출)
##### 1. DispatchQueue (GCD - Grand Central DispatchQueue)
- 주로 사용
- 직접적으로 쓰레드를 관리하는 개념이 아닌, 대기열(Queue)의 개념을 이용해서 작업을 분산 처리하고 OS에서 알아서 쓰레드 숫자(갯수)를 관리
- 메인 쓰레드(1번)가 아닌 다른 쓰레드에서 오래걸리는 작업(네트워크 처리 등)들이 쉽게 비동기적으로 동작하도록 함.
##### 2. OperationQueue
- 잘 안씀
### 병렬(Parallel) vs 동시성(Concurrency)
- 물리적인 Thread 1개가 소프트웨어적인 Thread 여러개를 동작시킬 수 있음
	- 물리적인 Thread와 소프트웨어적인 Thread는 1대1 매칭이 아님
	- 모두 OS 영역(Thread Pool, NSThread 객체의 모음)에서 관리함
- 소프트웨어적인 Thread가 동시 처리해도 물리적인 Thread는 병렬적인 처리를 하고 있지 않을 수 있음
#### 병렬(Parallel)
> 물리적인 쓰레드에서 실제 동시에 일을 하는 개념
- 내부적으로 알아서 동작하기 때문에 개발자가 신경 쓸 필요가 없는 영역
#### 동시성(Concurrency)
> 메인 쓰레드가 아닌 다른 소프트웨어적인 쓰레드에서 동시에 일을 하는 개념
- 개발자가 신경 써야 하는 영역
- 물리적인 쓰레드를 알아서 switching하면서 엄청 빠르게 일을 처리
- 2개의 쓰레드에서 일을 해도 내부에 물리적인 쓰레드는 1개만 동작하고 있을 수도 있음

---
## 동기(Sync) vs 비동기(Async)
### 비동기(Async)
> 작업을 다른 쓰레드에서 하도록 시킨 후, 그 작업이 끝나길 **"기다리지 않고"** 다음일을 진행한다.
- 안 기다려도 다음 작업을 생성할 수 있다.
- 작업을 보내고 즉시 리턴 시킴
### 동기(Sync)
> 작업을 다른 쓰레드에서 하도록 시킨 후, 그 작업이 끝나길 **"기다리고"** 다음일을 진행한다.
- 기다렸다가 다음 작업을 생성할 수 있다.
- 작업을 보내고 끝날 때 까지 `block`하여 다른 일처리를 못하게 막고 리턴 될 때 까지 기다린다.

### Blocking과 Non-Blocking
> Swift에서 **동기는 Blocking의 개념으로, 비동기는 Non-Blocking의 개념**으로만 사용

- **CPU 제어권과 관련된 개념(제어권 여부)**
	- Blocking
		- 제어권 바로 반환하지 않음
	- Non-Blocking
		- 제어권 바로 반환
- **결과값과 순서에 관련된 개념(return 값)**
	- 동기(sync)
		- 결과값을 기다리고, 순차적 실행
	- 비동기(async)
		- 결과값을 기다리지 않고, 비순차적 실행

## 직렬(Serial) vs 동시(Concurrent)
### 직렬(Serial) 큐
> (보통 메인에서) 분산처리 시킨 작업을 **"다른 한 개의 쓰레드에서"** 처리하는 큐
- **순서가 중요한 작업을 처리**할 때 사용
### 동시(Concurrent) 큐
> (보통 메인에서) 분산처리 시킨 작업을 **"다른 여러 개의 쓰레드에서"** 처리하는 큐
- 몇 개의 쓰레드로 분산할 지는 시스템이 알아서 결정
- 각자 **독립적이지만 유사한(중요도나 작업의 성격 등) 여러 개의 작업을 처리**할 때 사용

#### 비동기(Async)와 동시(Concurrent)는 같은 말인가?
- 비동기는 작업을 보내는 쓰레드(메인 쓰레드)와 관련이 있음.
	- 작업을 보내고 **그 작업이 완료되길 기다릴 것인가? 안 기다릴 것인가?**
- 동기는 작업을 받은 쓰레드(메인 쓰레드를 제외한 다른 쓰레드들)와 관련이 있음.
	- 작업을 받은 쓰레드가 **한 개냐? 여러 개냐?**

# 코드로 보는 동시성 프로그래밍
#### 네트워킹 같이 오래 걸리는 작업 같은 경우
```swift
// 오래 걸리는 작업들
func task6() {
    print("Task 6 시작")
    sleep(2)
    print("Task 6 완료★")
}
func task7() {
    print("Task 7 시작")
    sleep(2)
    print("Task 7 완료★")
}
func task8() {
    print("Task 8 시작")
    sleep(2)
    print("Task 8 완료★")
}

// 비동기 처리를 하지 않으면 6초 이상 걸림
task6()
task7()
task8()
// Task 6 시작
// Task 6 완료★
// Task 7 시작
// Task 7 완료★
// Task 8 시작
// Task 8 완료★
```
#### 이를 비동기 처리 한다면
> 큐로 보내면 다른 쓰레드로 배치함.
```swift
// "디폴트 글로벌큐 생성","비동기적으로"
print("1")
DispatchQueue.global().async {
    task6() // 다른 쓰레드로 보낼 작업을 배치
}
DispatchQueue.global().async {
    task7()
}
DispatchQueue.global().async {
    task8()
}
print("2")

// 2초면 모든 작업 완료. 대신 순서는 알 수 없다.
task6()
task7()
task8()
// 1
// 2
// Task 6 시작
// Task 7 시작
// Task 8 시작
// Task 8 완료★
// Task 6 완료★
// Task 7 완료★
```
- `global`큐는 그냥 공통적으로 사용하는 큐로 일반적으로 가장 많이 사용함
	- 애플이 미리 만들어 놓은 동시큐
- `global().sync`로 동기적으로 시킬 수 있지만 거의 사용할 일이 없음
	- 작업을 시키고 기다리기 때문에 메인 쓰레드가 버벅임
	- 대부분 `async`만 사용함
#### 클로저는 작업을 하나로 묶음
> 전체가 하나의 작업 -> **내부적으로는 ==동기적으로 동작==**

```swift
DispatchQueue.global().async {
    print("Task1 시작")
    print("Task1-1")
    print("Task1-2")
    print("Task1 종료")
}
// Task1 시작
// Task1-1
// Task1-2
// Task1 종료

DispatchQueue.global().async {
    print("Task2 시작")
}
DispatchQueue.global().async {
    print("Task2-1")
}
DispatchQueue.global().async {
    print("Task2-2")
}
DispatchQueue.global().async {
    print("Task2 종료")
}
// Task2 시작
// Task2 종료
// Task2-2
// Task2-1
```
- 위와 아래 코드는 전혀 다른 코드임. 아래는 순서를 보장 할 수 없음.
- 아래 코드는 작업이 4개로 분할된 개념

### 코드 레벨에서의 동기(sync) vs 비동기(aync)
```swift
// 동기적인 함수의 정의
func task1() {
    print("Task 1 시작")
    sleep(2)
    print("Task 1 완료★")
}
func task2() {
    print("Task 2 시작")
    sleep(2)
    print("Task 2 완료★")
}

// 비동기적인 함수의 정의
func task3() {
    DispatchQueue.global().async {
        print("Task 3 시작")
        sleep(2)
        print("Task 3 완료★")
    }
}
func task4() {
    DispatchQueue.global().async {
        print("Task 4 시작")
        sleep(2)
        print("Task 4 완료★")
    }
}
```
#### 동기적인 작업의 진행
> 일이 끝나야 다음줄로 이동 (내부 동기)
```swift
task1() 
task2()
// Task 1 시작
// Task 1 완료★
// Task 2 시작
// Task 2 완료★
```
#### 비동기적인 작업의 진행
> 일이 끝나지 않아도 다음줄로 이동 (내부 비동기)
```swift
// 내부적으로 비동기처리가 되어있는 함수들
task3()
task4()
// Task 3 시작
// Task 4 시작
// Task 4 완료★
// Task 3 완료★
```

### 코드 레벨에서의 직렬(Serial)큐 vs 동시(Concurrent)큐
#### Serial 직렬큐
```swift
let serialQueue = DispatchQueue(label: "com.inflearn.serial")
serialQueue.async {
    task1()
}
serialQueue.async {
    task2()
}
// Task 1 시작
// Task 1 완료★
// Task 2 시작
// Task 2 완료★
```
- `label`에는 마음대로 쓰면 된다.
- `label`로 만든 큐는 직렬큐이다.
- 직렬큐이기 때문에 비동기적으로 보낸다 하더라도 순차적으로 실행된다.
#### Concurrent 동시큐
```swift
let concurrentQueue = DispatchQueue.global()
concurrentQueue.async {
    task1()
}
concurrentQueue.async {
    task2()
}
// Task 1 시작
// Task 2 시작
// Task 2 완료★
// Task 1 완료★
```
- 일을 다 시켜버리고 어떤게 끝날지 알 수 없다.