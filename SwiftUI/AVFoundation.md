# AVFoundation
![](https://blog.kakaocdn.net/dn/dgjyAm/btsnE9grRYs/funkyYlvSpfHUi2TZJZHZ1/img.png)

### 주요 특징

1. **미디어** **재생**: 오디오 및 비디오 파일을 재생할 수 있습니다. AVPlayer 및 AVPlayerItem 클래스를 사용하여 미디어 재생을 제어할 수 있습니다.
2. **미디어** **녹화**: 카메라 및 마이크로폰을 사용하여 오디오 및 비디오를 녹화할 수 있습니다. AVCaptureSession, AVCaptureDevice, AVCaptureInput, AVCaptureOutput 클래스 등을 사용합니다.
3. **미디어** **편집**: AVAsset 및 AVAssetTrack 클래스를 사용하여 미디어 파일을 자르고, 병합하고, 트랙을 수정할 수 있습니다.
4. **미디어** **스트리밍**: AVFoundation을 사용하여 네트워크를 통해 미디어를 스트리밍할 수 있습니다.
5. **메타데이터** **관리**: 미디어 파일의 메타데이터(예: 제목, 아티스트, 앨범, 커버 아트 등)를 읽고 쓸 수 있습니다.

![](https://blog.kakaocdn.net/dn/ljm6P/btsnEWhjxYf/hqlT2MCDhsAdYmdQfYMxJ0/img.png)

**AVFoundation**은 저수준의 미디어 처리 프레임워크로, 오디오와 비디오의 캡처, 편집, 처리, 재생 등을 세밀하게 제어할 수 있는 강력한 기능을 제공합니다. UIKit 너머의 Core 프레임워크와 맞닿아 있는 프레임워크입니다

## AVAsset

![](https://blog.kakaocdn.net/dn/djX9SB/btsnOsrWBmH/x8hAsZAKH60bXk671WreM0/img.png)

- 시간이 지정된 시청각 미디어를 모델링하는 객체
- 해당 객체는 파일 기반의 미디어 데이터를 모델링하며, HLS(HTTP Live Streaming)을 사용해 스트리밍된 데이터도 마찬가지로 모델링합니다.

## AVPlayer

![](https://blog.kakaocdn.net/dn/bmFjMx/btsnOslaAU3/krZ9hkv2kwqk9syD2iPuZk/img.png)

- 플레이어의 이동 동작을 제어하는 인터페이스를 제공하는 객체
- Player는 미디어 에셋의 재생 및 시간을 관리하는 컨트롤러 객체입니다.
- AVPlayer 인스턴스를 사용하여 로컬 및 원격의 파일 기반 미디어 및 HTTP 라이브 스트리밍을 사용하여 제공되는 시청각 미디어를 재생할 수 있습니다.
- Player를 사용하여 한 번에 하나의 미디어 에셋을 재생합니다.
- Player 인스턴스를 재사용하여 `replaceCurrentItem(with:)`메서드를 사용하여 추가 미디어 자산을 재생할 수 있지만, 한 번에 하나의 미디어 자산만 재생이 가능합니다.
- 또한 프레임워크는 순차적으로 재생되는 미디어 자산의 대기열을 생성하고 관리하는 데 사용하는 `AVQueuePlayer`라는 클래스의 서브클래스를 제공합니다.
- `AVAsset`은 미디어의 시간 및 생성 날짜같은 정적 데이터만 모델링되어 있기 때문에, 그 자체로는 AVPlayer의 재생 대상이 되기에 적합하지 않습니다. (재생 시간과 같은 값은 동적으로 변동되기 때문)
- 에셋을 재생하려면 `AVPlayerItem`에서 찾을 수 있는 동적 부분이 필요합니다.
- AVPlayer는 상태가 지속적으로 변경되는 동적 객체입니다. 상태 변화 관찰을 위해서는 주로 KVO가 사용됩니다.
- 다만 `AVPlayer` 및 `AVPlayerItem` 둘 모두 비시각적 객체입니다. 따라서 그들만으로는 콘텐츠를 화면에 표시할 수 없습니다. 화면에 콘텐츠를 표시하기 위해서는 주로 2가지 방법이 사용됩니다.

## AVPlayerItem

![](https://blog.kakaocdn.net/dn/cnIxQ3/btsnD7jma0x/413f7oK6WjtlJlkGI2ZTNk/img.png)

- 에셋이 재생 상태일 때 해당 에셋의 타이밍과 프레젠테이션 상태를 모델링하는 객체
- player item은 재생할 미디어를 나타내는 `AVAsset` 객체에 대한 참조를 보유합니다.
- 재생을 위해 대기열에 넣기 전에 에셋을 검사해야 하는 경우, `load(_:)`메서드를 호출하여 하나 이상의 프로퍼티 값을 검색합니다.
- 또는 player item에 필요한 프로퍼티를 `init(asset:automaticallyLoadedAssetKeys:)` 이니셜라이저에 전달하여 자동으로 로드하도록 지시할 수도 있습니다.

![](https://blog.kakaocdn.net/dn/bpnOWI/btsnF55Hqji/f79A8YOAPfkPg4s0VR1aZK/img.png)

- AVPlayer 객체가 AVPlayerItem을 사용하고, AVPlayerItem이 AVAsset을 사용하는 구조입니다.

## AVPlayerLayer

![](https://blog.kakaocdn.net/dn/bmac1q/btsnEL1f4l1/dmrKGUFhIQlJ1qUb2YkVu0/img.png)

- Player 객체의 시각적 콘텐츠를 표시하는 객체
- CALayer의 서브클래스

## AVKit

**AVKit**은 AVFoundation 위에 구축된 고수준의 프레임워크로, 주로 미디어 재생을 쉽게 구현할 수 있도록 도와줍니다. AVKit은 미디어 재생을 위한 기본 사용자 인터페이스와 간단한 API를 제공하여 개발자가 복잡한 미디어 처리 로직을 직접 구현하지 않고도 손쉽게 재생 기능을 추가할 수 있습니다.

1. **미디어 재생 UI 컴포넌트**:
   
    - `AVPlayerViewController`: 미디어 재생을 위한 완전한 사용자 인터페이스 제공 (재생/일시정지 버튼, 재생 바, 전체 화면 전환 등 기본 기능 포함).
    - `AVRoutePickerView`: AirPlay 등 외부 장치로의 미디어 전송 기능 제공.
2. **간편한 미디어 재생**:
   
    - AVPlayer와 연동하여 비디오 및 오디오를 재생.
    - 최소한의 코드로 고품질의 재생 기능 구현 가능.
3. **기본적인 미디어 제어**:
   
    - 재생, 일시정지, 탐색, 볼륨 조절 등 기본적인 미디어 제어 기능 제공.

**사용 예시**:

- 간단한 비디오 재생 기능을 앱에 추가할 때.
- 미디어 재생을 위한 기본 UI가 필요한 경우.
- 빠르게 미디어 재생 기능을 구현하고자 할 때.

### **비교 요약**

| **특징**         | **AVFoundation**                                 | **AVKit**                                      |
| ---------------- | ------------------------------------------------ | ---------------------------------------------- |
| **레벨**         | 저수준 (Low-level)                               | 고수준 (High-level)                            |
| **주요 기능**    | 미디어 캡처, 편집, 처리, 맞춤형 재생 등          | 미디어 재생을 위한 기본 UI 및 간편한 재생 기능 |
| **사용 복잡성**  | 복잡하고 세밀한 제어 필요                        | 간단하고 빠른 구현 가능                        |
| **사용 사례**    | 비디오 편집기, 스트리밍 애플리케이션 등          | 간단한 비디오 플레이어, 기본 재생 기능 추가    |
| **UI 제공 여부** | 미디어 처리에 집중, UI는 개발자가 직접 구현 필요 | 기본적인 재생 UI 컴포넌트 제공                 |
| **의존성**       | 독립적으로 사용 가능                             | AVFoundation 위에 구축됨                       |

### **언제 어떤 프레임워크를 선택할까?**

- **AVFoundation**을 선택해야 할 때:
  
    - 고도화된 미디어 편집 기능이 필요할 때.
    - 미디어 데이터를 직접 처리하거나, 맞춤형 재생 로직을 구현해야 할 때.
    - 미디어 캡처, 변환, 합성 등 복잡한 작업이 요구될 때.
- **AVKit**을 선택해야 할 때:
  
    - 단순히 비디오나 오디오를 재생하는 기능이 필요할 때.
    - 빠르고 간편하게 미디어 재생 UI를 구현하고자 할 때.
    - 기본적인 재생 기능으로 충분할 때.

### 미디어 재생
```swift
import SwiftUI
import AVKit

struct ContentView: View {
    var body: some View {
        VStack {
            VideoPlayer(player: AVPlayer(url: Bundle.main.url(forResource: "1",                          withExtension: "MOV")!))
        }
        .padding()
    }
}
```