# 날짜와 시간 (Date)

### UTC
> 국제적인 표준 시간 - 협정 세계시

- 국제적인 표준 시간의 기준 / 국제 사회가 사용하는 과학적 시간의 표준 / 기존 평균태양시인 그리니치 표준시(GMT)를 대체하여 사용
- 일반적으로 GMT시간과 UTC시간을 혼용해서 사용
- 영국, 런던의 그리니치 천문대의 시간을 기준으로하는 시간
- 우리나라(한국)는 런던을 기준으로 + 9시간 (빠름)

## Date 구조체의 이해
> Swift에서 기본으로 제공해주는 날짜 다루는 Date 구조체 타입
- **지금 현재시점 `Date` 인스턴스 생성**
	- 기준 시간(Reference Date)를 기준으로 몇초 후인지에 대한 시간 정보를 통해 현재 시점(UTC 기준)을 저장
	- 몇 초가 떨어져 있는지 `.timeIntervalSinceReferenceDate`
		- `TimeInterval` 타입 (초단위)
- 암시적인 날짜 + 시간으로 구성
	- 잘 변환해서 사용해야함
- `let yesterday = now - 86400`
	- 지금으로부터 86400초 전은 어제이다.

**Date - 초 기준으로 절대적인 시점을 의미하는 개념일 뿐**
- **Calendar - 달력 및 달력의 요소를 다루는 구조체**
	- 년 / 월 / 일 + 시 / 분 / 초 + 요일
- **DateFormatter - 표시하기 위한 문자열**
	- "형식" 문자열로 변행해 주는 클래스

```swift
// 특정 달력(양력, 음력, ...)이나 타임존에 영향을 받지않는 독립적인 시간
// 날짜와 시간을 다루는 Date 구조체의 인스턴스
// 생성시점의 날짜와 시간을 생성해서 (기준시간으로부터) 초단위 기준값을 가지고 있음
let now = Date()    
print(now) // 그냥 출력하면 항상 UTC기준의 시간으로 출력

// 기준시간(Reference Time)이 있고, 그 시간을 기준, 초단위를 기준으로 저장
// 2001.1.1. 00:00:00 UTC시간을 기준
now.timeIntervalSinceReferenceDate

// 예전에는 1970.1.1. 00:00:00 UTC시간을 기준으로 사용
now.timeIntervalSince1970

let oneSecond = TimeInterval(1.0)    // 1초 간격
//TimeInterval(<#other: #Float#>)

let yesterday = now - 86400
print(yesterday)

// 해당 시점으로부터 차이를 초로 (86,400초 차이)
now.timeIntervalSince(yesterday)
// 지금시점을 기준으로 그 시간까지의 거리를 초로
now.distance(to: yesterday)

// 내일
now.advanced(by: 86400)
now.addingTimeInterval(3600 * 24)
now + 86400

// 스위프트 내부에 미리 정의된 타임존 확인해보기
for localeName in TimeZone.knownTimeZoneIdentifiers {
    print(localeName)
}
TimeZone.current
```
- 3600초 == 1시간
- 86400초 == 하루

## Calendar 구조체의 이해
> Swift에서 기본으로 제공해주는 달력(Calendar) 구조체 타입

```swift
// "절대 시점(Date)"을 연대/연도/날짜/요일과 같은 "달력의 요소"로 변환을 돕는 객체
// 그레고리력 (Gregorian calendar) - 양력 (전세계표준 달력)
var calendar = Calendar.current   // 타입 속성 ==> 현재의 달력(양력) 반환

// 직접 생성하기 (이런 방식으로 잘 사용하지는 않음)
let calendar1 = Calendar(identifier: .gregorian)  
// 유저가 선택한 달력 기준(세계적 서비스를 한다면)
let calendar2 = Calendar.autoupdatingCurrent
```

### 지역 설정
> 나라(지역)마다 날짜와 시간을 표시하는 형식과 언어가 다름

```swift
calendar.locale    // 달력의 지역 (영어/한국어) (달력 표기 방법과 관련된 개념)
calendar.timeZone  // 타임존 ==> Asia/Seoul (UTC 시간관련된 개념)

// 필요할때 찾아서 쓰면됨
calendar.locale = Locale(identifier: "ko_KR")
calendar.timeZone = TimeZone(identifier: "Asia/Seoul")
```
- [지역설정 문자열 (700여개)](https://gist.github.com/xta/6e9b63db1fa662bb3910b680f9ebd458) 
- [타임존 문자열 (440여개)](https://gist.github.com/mhijack/2b63b84d96802ccc719291474ac9df72 )

### Date의 년/월/일/시/분/초 확인하는 방법
> `.component`: 원하는 요소로 요소화 시키는 메서드(타입 알려주면 그것을 정수로 반환)

```swift
// 1) 날짜 - 년 / 월 / 일
let year: Int = calendar.component(.year, from: now)
let month: Int = calendar.component(.month, from: now)
let day: Int = calendar.component(.day, from: now)

// 2) 시간 - 시 / 분 / 초
let timeHour: Int = calendar.component(.hour, from: now)
let timeMinute: Int = calendar.component(.minute, from: now)
let timeSecond: Int = calendar.component(.second, from: now)

// 3) 요일
let weekday: Int = calendar.component(.weekday, from: now)
// 일요일 - 1
// 월요일 - 2
// 화요일 - 3
// ...
// 토요일 - 7

print("\(year)년 \(month)월 \(day)일")
```

> `.dateComponents` : 여러개로 요소화시키는 메서드

```swift
let myCal = Calendar.current


var myDateCom = myCal.dateComponents([.year, .month, .day], from: now)
//myCal.dateComponents(<#components: Set<Calendar.Component>, from: Date#>)

myDateCom.year
myDateCom.month
myDateCom.day

print("\(myDateCom.year!)년 \(myDateCom.month!)월 \(myDateCom.day!)일")
```

## 실제 프로젝트에서 활용 방식
```swift
// 달력을 기준으로 나이 계산 하기
class Dog {
    var name: String
    var yearOfBirth: Int
    
    init(name: String, year: Int) {
        self.name = name
        self.yearOfBirth = year
    }
    
    // 나이를 계산하는 계산 속성
    var age: Int {
        get {
            let now = Date()
            let year = Calendar.current.component(.year, from: now)
            return year - yearOfBirth
        }
    }
}

let choco = Dog(name: "초코", year: 2015)
choco.age // 6

// 열거형으로 요일을 만들고, 오늘의 요일을 계산하기
// (원시값)열거형으로 선언된 요일
enum Weekday: Int {
    case sunday = 1, monday, tuesday, wednesday, thursday, friday, saturday
    
    // ⭐️ 타입 계산속성
    static var today: Weekday {
        let weekday: Int = Calendar.current.component(.weekday, from: Date())  // 요일을 나타내는 정수
        return Weekday(rawValue: weekday)!
    }
}

// 오늘이 무슨요일인지
let today = Weekday.today

// 두 날짜 사이의 일 수 계산하기
let startDate = Date()
let endDate = startDate.addingTimeInterval(3600 * 24 * 60)

let calendar2 = Calendar.current
let someDays = calendar2.dateComponents([.day], from: startDate, to: endDate).day!

print("\(someDays)일 후")
```
- 열거형의 원시값을 이용해 생성할 수 있다.

## DateFormatter
> 날짜와 시간을 원하는 형식의 문자열(String)으로 변환하는 방법을 제공하는 클래스
- RFC 3339 표준으로 작성 (HTTP 프로토콜)
- Date를 특정 형식의 문자열로 변환하려면 여러가지 설정해야한다.
	1. 지역 설정
	2. 시간대 설정
	3. 날짜 형식
	4. 시간 형식

```swift
// 날짜 + 시간  <======>  String
let formatter = DateFormatter()

// 1. 지역 설정
formatter.locale = Locale(identifier: "ko_KR")
// "2021년 5월 8일 토요일 오후 11시 44분 24초 대한민국 표준시"
formatter.locale = Locale(identifier: "en_US")
// "Saturday, May 8, 2021 at 11:45:51 PM Korean Standard Time"

// 2. 시간대 설정
formatter.timeZone = TimeZone.current
```

### 표시하려는 날짜와 시간 설정
#### 애플이 미리 만들어 놓은 기존 형식으로 생성
```swift
// (1) 날짜 형식 선택
formatter.dateStyle = .full           // "Tuesday, April 13, 2021"
//formatter.dateStyle = .long         // "April 13, 2021"
//formatter.dateStyle = .medium       // "Apr 13, 2021"
//formatter.dateStyle = .none         // (날짜 없어짐)
//formatter.dateStyle = .short        // "4/13/21"


// (2) 시간 형식 선택
formatter.timeStyle = .full           // "2:53:12 PM Korean Standard Time"
//formatter.timeStyle = .long         // "2:54:52 PM GMT+9"
//formatter.timeStyle = .medium       // "2:55:12 PM"
//formatter.timeStyle = .none         // (시간 없어짐)
//formatter.timeStyle = .short        // "2:55 PM"


// 실제 변환하기 (날짜 + 시간) ===> 원하는 형식
let someString1 = formatter.string(from: Date())
print(someString1)
```
- 클래스 인스턴스 생성 후 날짜 및 시간 설정
- `.string` 메서드로 문자열로 변환
#### 커스텀 형식으로 생성
```swift
formatter.locale = Locale(identifier: "ko_KR")
//formatter.dateFormat = "yyyy/MM/dd"
formatter.dateFormat = "yyyy년 MMMM d일 (E)"
// 2024년 2월 12일 (월)

let someString2 = formatter.string(from: Date())
print(someString2)

// 문자열로 만드는 메서드
//formatter.string(from: <#Date#>)
```
- [날짜/시간 형식 (유니코드에서 지정)](http://www.unicode.org/reports/tr35/tr35-25.html#Date_Format_Patterns)

### 문자열에서 Date로 변환 가능
```swift
let newFormatter = DateFormatter()
newFormatter.dateFormat = "yyyy/MM/dd"

let someDate = newFormatter.date(from: "2021/07/12")!
print(someDate)
```
- `.dateFormat`으로 문자열 형식 지정
- 그 후 `.date(from: "String")`으로 Date 구조체로 변환 가능

#### 두 날짜 범위 출력 코드 구현
```swift
let start = Date()
let end = start.addingTimeInterval(3600 * 24 * 60)


let formatter2 = DateFormatter()
formatter2.locale = Locale(identifier: "ko_KR")
formatter2.timeZone = TimeZone.current
//formatter2.timeZone = TimeZone(identifier: "Asia/Seoul")

formatter2.dateStyle = .long
formatter2.timeStyle = .none


print("기간: \(formatter2.string(from: start)) - \(formatter2.string(from: end))")
// 2021년 7월 13일 - 2021년 9월 11일
```

## 실제 프로젝트에서 활용 방식
```swift
struct InstagramPost {
    let title: String = "제목"
    let description: String = "내용설명"
	
	// 게시물 생성을 현재날짜로
    private let date: Date = Date()
    
    // 날짜를 문자열 형태로 바꿔서 리턴하는 계산 속성
    var dateString: String {
        get { // 생략 가능
            let formatter = DateFormatter()
            formatter.locale = Locale(identifier: "ko_KR")
            // formatter.locale = Locale(identifier: Locale.autoupdatingCurrent.identifier)
            
            // 애플이 만들어 놓은
            formatter.dateStyle = .medium
            formatter.timeStyle = .full
            
            // 개발자가 직접 설정한
            //formatter.dateFormat = "yyyy/MM/dd"
            
            return formatter.string(from: date)
        }
    }
}

let post1 = InstagramPost()
print(post1.dateString)
```
- `get` 블럭만 있는 경우 생략 가능하다.

### DateComponents
> `DateComponents`를 활용해 원하는 특정 날짜/시간 생성하기
- 날짜와 시간의 요소들을 다룰 수 있는 구조체
- 원하는 날짜/시간으로 절대적 시점(초 기준 )의 인스턴스를 만들 수 있다.

```swift
// 구조체 (날짜/시간의 요소들을 다룰 수 있는)
var components = DateComponents()
components.year = 2021
components.month = 1
components.day = 1

components.hour = 12
components.minute = 30
components.second = 0

let specifiedDate: Date = Calendar.current.date(from: components)!
print(specifiedDate)
// 2021-01-01 03:30:00 +0000
```

#### 좀 더 세련된 방식
> 구조체의 확장을 이용해서 Date에 생성자 구현
```swift
extension Date {
    // 구조체 실패가능 생성자로 구현
    init?(y year: Int, m month: Int, d day: Int) {
        
        var components = DateComponents()
        components.year = year
        components.month = month
        components.day = day
        
        guard let date = Calendar.current.date(from: components) else {
            // 날짜 생성할 수 없다면 nil리턴
            return nil  
        }
        //구조체이기 때문에, self에 새로운 인스턴스를 할당하는 방식으로 초기화가능
        self = date      
    }
}

// 특정날짜(시점) 객체 생성
let someDate = Date(y: 2021, m: 1, d: 1)
let someDate2 = Date(y: 2021, m: 7, d: 10)
```
- `self = date` 문법은 클래스에서 사용할 수 없다. [[Self 키워드]]
	- 구조체에서는 자주 사용한다.