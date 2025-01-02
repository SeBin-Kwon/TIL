![](https://velog.velcdn.com/images/sbkwon16/post/0c98779a-ba7a-4c9f-bd13-ed5b194c604e/image.jpg)

사람들은 Swift 5.0에서 가장 중요한 점이 ABI Stability라고 하는데요,
말 그대로 ABI라는게 안정화 되었다는 건데 이게 뭐길래 그럴까요?

## ABI

> **A**pplication **B**inary **I**nterface의 약자

흔히 들어본 **API**는 Application Programming Interface의 약자로 프로그래밍시 코드에서 사용하는 인터페이스입니다. 
**ABI**는 Application Binary Interface의 약자로 **바이너리 간 인터페이스**입니다

즉, 이진값 0101을 이용해서 라이브러리 혹은 OS(Operating System)와 사용자에 의해서 실행되는 프로그램(App) 사이에 필요한 저수준 인터페이스를 정의합니다.

![](https://velog.velcdn.com/images/sbkwon16/post/b8bd0c96-b7e0-496f-b5f4-f1d420151f7c/image.png)

함수를 어떻게 호출할지, 메모리에 데이터를 어떻게 표현할지 등을 정의한게 ABI라고 할 수 있습니다.

### 그동안의 불편했던 점
- Swift 5.0 미만에서는 새로운 Swift버전이 나왔을 때 개발자는 새 버전으로 마이그레이션을 해야 컴파일이 가능했습니다.
- 예를 들면 Xcode에서 Swift버전을 4.1에서 4.2로 바꾸는 순간 소스코드의 Swift버전과 컴파일러의 Swift버전이 맞지 않으면서 컴파일 되지 않았습니다.
  - 그래서 각 바이너리 번들에는 고유의 Swift 동적 라이브러리(.dylib 파일)를 갖고 있고 이 라이브러리는 바이너리간 상호 작용을 위해 사용합니다.


# **ABI Stability**
이러한 ABI가 안정화 되었다는 것은 Swift 5.0과 그 이후의 버전이라면 **컴파일된 앱과 라이브러리가 서로 다른 버전이어도 바이너리간 호환이 가능하다**는 것입니다.

![](https://velog.velcdn.com/images/sbkwon16/post/c5295533-5747-4d9e-af83-ab6a74937384/image.png)

- 그래서 이제 앱마다 dylib를 패키징 할 필요가 없어졌습니다. 그만큼 앱 번들 크기가 줄어들어서 앱 용량을 줄일 수 있습니다.
- 소스 호환성 덕분에 Swift 새 버전이 나와도 마이그레이션 할 필요가 없어졌습니다.
- 바이너리로 된 프레임워크 역시 다양한 Swift버전으로 배포할 수 있게 되었습니다.

앞으로 이러한 ABI stability를 보장하기 위해서 Swift 표준 라이브러리에 새로운 타입이나 프로토콜, 함수 등을 추가하는 것이 제안된다고 합니다.


#### 참고
https://jusung.github.io/ABI-Stability/
https://sujinnaljin.medium.com/swift-abi%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-7b861d29ace6