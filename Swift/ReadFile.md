# 파일 읽기

```swift
let fileName = "test"
let fileType = "txt"
guard let logFilePath = Bundle.main.path(forResource: fileName, ofType: fileType) else {
	print("logFilePath 파일을 읽을 수 없습니다.")
	print("번들 내 파일 목록:")
		if let resources = Bundle.main.urls(forResourcesWithExtension: nil, subdirectory: nil) {
			resources.forEach { print($0.lastPathComponent) }
		}
	return
}
guard let contents = try? String(contentsOfFile: logFilePath) else {
	print("파일을 읽을 수 없습니다.")
	return
}
```
- 파일을 읽을 수 없을 때, 번들 내 파일 목록을 확인해볼 수 있다.

```swift
let path = "/Users/sebinkwon/Desktop/test.txt"
guard let contents = try? String(contentsOfFile: path) else {
	print("파일을 읽을 수 없습니다.")
	return
}
```
- 절대 경로를 이용하는 방법도 있다.