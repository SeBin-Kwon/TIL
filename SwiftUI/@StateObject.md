# @StateObject

> 뷰에서 데이터를 관리할 때, `@State`를 사용하는데 그것과 비슷한 개념이다.

`ObservableObject` 프로토콜로 선언된 값을(보통 뷰모델) **처음에 한 번 메모리에 올리기 위해선 `@StateObject`**를 사용해야 한다.

iOS 13에서는 `@ObservedObject`를 사용했지만 버그가 일어날 수 있다.

```swift
import SwiftUI

@main
struct TodoBinyApp: App {
    
    @StateObject var todoViewModel = TodoViewModel()
    
    var body: some Scene {
        WindowGroup {
            NavigationView {
                ContentView()
            }
            .environmentObject(todoViewModel)
        }
    }
}
```

그 후 이 StateObject를 **다른 곳으로 넘기고 싶다면 `.environmentObject(StateObject 변수)`**를 사용한다.

위 코드는 NavigationView의 안 ContentView로 `StateObject`인 `todoViewModel`를 넘겼다.

## 다른 View에서 StateObject 받기

위 코드에서 ContentView로 넘겼다고 해서 ContentView에서만 사용할 수 있는건 아니다.
**ContentView의 하위 뷰라면 `@EnvironmentObject` 선언을 통해 어디서든 `StateObject`를 사용할 수 있다.
**

```swift
struct ContentView: View {
    @State private var selectedTab = 0
    @State private var title = "Do"
    var body: some View {
        TabView(selection: $selectedTab) {
            DoView()
                .tag(0)
                .tabItem {
                    Label("Do", systemImage: "circle.dashed")
                }
                
            DoneView()
                .tag(1)
                .tabItem {
                    Label("Done", systemImage: "checkmark.circle.fill")
                }
            ...
```
```swift
import SwiftUI

struct DoView: View {
    @EnvironmentObject var todoViewModel: TodoViewModel
    @State private var isAdd = false

    var body: some View {
        List {
            ForEach(todoViewModel.items, id:\.self){
                item in
                if !item.isCompleted {
                    ListRowView(item: item)
                }
            }
            .onDelete(perform: todoViewModel.deleteItem)
            .onMove(perform: todoViewModel.moveItem)
        }
        ...
```

이로써 뷰모델을 어느 View에서든지 사용할 수 있게 된다!