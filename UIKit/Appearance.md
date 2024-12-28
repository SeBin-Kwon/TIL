## 스토리보드로 네비게이션바 위에 백그라운드 색상을 채우고 싶다면?

네비게이션바의 백그라운드 색상을 넣고싶은데 
그냥 단순히 Navigation bar - View - Background에서 색상을 바꾸면 딱 네비게이션바 영역만 색이 채워지고 그 위에는 채워지지 않는다.

**이때 Navigation bar 선택 후 인스펙터 영역에서 맨 위를 보면 Appearance 속성이 있을 것이다.**

### Appearance
- **iOS 14 버전 이상에서** **Appearanc** 속성을 사용할 수 있다.
- 네비게이션 컨트롤러 뿐만 아니라 탭바 컨트롤러에도 있다.
- 대표적으로 **Standard**와 **Scroll Edge**가 있다.


## Standard와 Scroll Edge의 차이
![](https://velog.velcdn.com/images/sbkwon16/post/b899b861-8f83-43cf-9c47-0f61618d50ab/image.png)
- 스크롤 되는 환경에서 **맨 위와 맨 맽 Edge 부분은 Scroll Edge가 적용** 된다.
- **스크롤 중간은 모두 Standard가 적용** 된다.

- 둘 다 적용하면 아래와 같이 된다.
  - **Scroll Edge (파랑)**
    - 더이상 내려갈 곳이 없는 맨 밑바닥 혹은 맨 위 상태에서 활성화 됨
  - **Standard (노랑)**
    - 스크롤 되는 중간중간은 모두 Standard임
      
| 맨 위                                                        | 중간                                                         | 맨 밑                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![](https://velog.velcdn.com/images/sbkwon16/post/74d97ce5-fa97-44b2-8e6b-bc3a0ac00dae/image.png) | ![](https://velog.velcdn.com/images/sbkwon16/post/fb30abd0-c730-42d7-aadd-030a08f19d6a/image.png) | ![](https://velog.velcdn.com/images/sbkwon16/post/cc48acb3-29c0-4f36-ab84-ba04b1b373c9/image.png) |