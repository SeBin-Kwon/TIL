# Entry Point
> 시작하는 지점

프로그램을 실행시키려면 컴퓨터는 어디부터 시작하는지 알아야 실행시킬 수 있다.
CPU는 Entry Point를 통해 시작 지점을 알 수 있고, 이를 통해 실행시킨다.
즉 모든 프로그램은 반드시 Entry Point가 있어야 한다!

## Swift Storyboard의 Entry Point

코드상에서는 아래 `@main`이라는 attribute symbol을 사용하여 Swift의 진입점을 지정한다.
```swift
@main
class AppDelegate: UIResponder, UIApplicationDelegate { ... }
```

스토리보드에서는 `->` 화살표 모양으로 확인할 수 있다.
- 스토리보드 내에서의 시작점으로, **LaunchScreen 이후에 가장 먼저 나올 첫번째 화면을 지정해준다.**
- **Entry Point는 스토리보드마다 있어야 한다.**


## Entry Point가 없으면 어떻게 되나?
- 빌드는 되는데 검은 화면만 뜨면서
`Failed to instantiate the default view controller for UIMainStoryboardFile 'Main' - perhaps the designated entry point is not set?`
라는 에러를 디버그 영역에서 확인할 수 있다.
![](https://velog.velcdn.com/images/sbkwon16/post/619325c9-abc1-4881-9528-c69e5a479c63/image.png)



## Entry Point 설정

Storyboard에서 Entry Point를 설정하는 방법은 2가지 있다.
- `->`모양을 찾아서 뷰컨트롤러에 드래그 앤 드롭

- 뷰컨트롤러 전체 선택 → 인스펙터에서 `Is Initial View Controller`체크

![](https://velog.velcdn.com/images/sbkwon16/post/94f89e2f-ceb0-4b53-a615-d5ec7b1b83b4/image.png)

⚠️ 가끔 Storyboard에서 이것저것하다 **Entry Point를 실수로 지울 수도 있다..!**

그럴땐 당황하지 말고 침착하게 인스펙터 영역에서 `Is Initial View Controller`를 체크하면 다시 생긴다.

## 🚨 네비게이션 컨트롤러 및 엔트리 포인트 이슈
> Entry Point 위치로 인한 이슈

어째서인지 네비게이션이 작동하지 않는 경우가 있을 수 있다.
![](https://velog.velcdn.com/images/sbkwon16/post/85372328-2064-4a75-bb8c-e23bdf95aa91/image.png)
- 잘보면 Entry Point가 네비게이션 컨트롤러가 아닌 그 옆 화면에 있는데,
- 이러면 **네비게이션 컨트롤러가 없는거나 마찬가지이다.**
- 음식을 준비했지만 그릇을 빼고 시작해서 못 담는 것이다.

![](https://velog.velcdn.com/images/sbkwon16/post/efa66f2d-70f5-4e58-95f9-34db668c062a/image.png)
- 이렇게 **Entry Point가 네비게이션 컨트롤러를 가르켜야** 네비게이션이 제대로 작동한다.
- 탭바 컨트롤러도 마찬가지이다.