# 뷰의 생명주기 View’s Life Cycle

- HIG에 따라서 많이 쓰이는 여백 수치가 8, 16, 24, 44, 48
- 아무것도 설정하지 않은 높이가 보통 44임 → 애플이 정한 것
- 폰트는 보통 12 ~ 15에서 벗어나는 일이 그렇게 많지 않음
- 탭바 아이콘 이름 대충 11 ~ 12, 13? 정도임

viewDidLoad - 뷰가 뜨기 직전

viewWillAppear - 뷰가 생길 것 같음

viewDidAppear - 뷰가 완벽하게 뜸

- **손으로 잡고있으면 안뜸**

viewWillDisappear - 뷰가 사라질 것 같음

- **손으로 잡고있으면 안뜸**

viewDidDisappear - 뷰가 완벽하게 사라짐

```swift
<SecondWeek.ShowViewController: 0x154f06700> viewDidLoad()
<SecondWeek.PracticeViewController: 0x155c08620> viewWillDisappear(_:)
<SecondWeek.ShowViewController: 0x154f06700> viewWillAppear(_:)
<SecondWeek.PracticeViewController: 0x155c08620> viewDidDisappear(_:)
<SecondWeek.ShowViewController: 0x154f06700> viewDidAppear(_:)
```

### A 화면 → B modal 화면

- A 화면은 사라지지 않음
- 아직 조금 화면이 보임
- viewWillDisappear / viewDidDisappear 호출되지 않음

### A 화면 → B show 화면

- A 화면이 완벽하게 사라짐
- viewWillDisappear / viewDidDisappear 실행됨

### 모달 sheet 방식, 풀스크린 방식

- sheet
  - 원래 버전
- fullScreen
  - 세그웨이 선택 후 - 인스펙터 - 프레젠테이션 - fullScreen
  - **완벽하게 화면을 가림**
  - **viewWillDisappear / viewDidDisappear 실행됨**
  - **show랑 똑같이 동작함**

### fullScreen 뒤로 가기 unwind

- 스토리보드에서 연결하는게 아니라, 코드로 직접 타이핑해야함
- 모달 화면이 아니라 **루트 화면에 작성해야함 (B 화면이 아니라 A 화면임)**

```swift
@IBAction func unwindToPracticeViewController(_ sender: UIStoryboardSegue) {
    print(#function)
}
```

- modal 화면의 버튼을 오른쪽 드래그 → 위 3개점 중 오른쪽 Exit → unwind 연결
- unwind는 뒤로 돌아올 수 있게 터널을 만들어 줌
- 어디서든지 다 써줄 수 있음
  - show 화면의 백버튼 말고도 unwind 버튼 만들어서 뒤로갈 수 있음
- A → B → C 화면 중 C 화면에서 unwind로 뒤로가며 A 화면으로 한번에 넘어감
- B는 자동으로 메모리에서 해제 되지만 코드마다 다를 듯

### A 화면 → 탭바 B 화면

- A 화면이 완벽하게 사라짐
- viewWillDisappear / viewDidDisappear 실행됨
- **show랑 똑같이 동작함**

## viewDidLoad

- 쇼나 모달
  - 화면 왔다갔다 하다보면 가끔 실행됨
  - 필요 없다면 메모리 싹 지웠다가 다시 뷰디드로드로 그림
- 탭바는 최초 한번만 실행됨
  - 루트뷰컨트롤러로서 계속 탭바에 존재하기 때문에 지울 이유가 없음
- 클릭을 안하면 메모리를 차지하고 있지 않음, 클릭을 하면 그 때 차지함

### 만약 두번째 탭에 MapKit을 두면?

- 탭바에서는 사라지지 않기 때문에 한번 두번째 탭에 들어가게 되면 메모리를 영원히 엄청나게 잡아먹게됨..
- **메모리를 많이 사용하는 건 탭바에 두지 않기!**
- Show에 두면 들어갔을 때 잠깐 많이 사용하다가 뒤로 갔을 때 화면이 사라지면서 메모리도 지워지게 됨.

### 설정 화면에서 닉네임 Show로 들어가서 수정

- 만약 설정화면 닉네임 세팅 코드가 viewDidLoad에 있다면
- 닉네임 수정을 해도 뒤로갔을때 화면이 반영되지 않음
- 왜냐하면 viewDidLoad가 호출되지 않기 때문에 다른 곳에다 해야함

### 쇼, 모달의 루트화면 배경색 바꾸기

- viewWillAppear에다 색 바꾸는 코드
- **변경될 일이 없는 것만 viewDidLoad에 쓰기**

### viewWillAppear 에다가? 아님 viewDidAppear?

- viewWillAppear에다가 하면 손으로 붙잡고 왔다갔다 할때마다 호출됨
- 화면이 완벽하게 나왔을 때만 색 바꾸고 싶다면 viewDidAppear

### ❓ viewIsAppearing

- 작년 WWDC에 나옴 - iOS 13버전부터 사용가능
- https://zeddios.tistory.com/1390
- viewWillAppear와 viewDidAppear 사이에서 호출됨
- 애플피셜 **view가 보일 때(appear) UI를 업데이트 하기 위한 최적의 장소**
- transition의 첫 프레임부터 사용자에게 보여짐