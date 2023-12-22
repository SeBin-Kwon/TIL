# iOS에서 서버와의 통신과 처리

TCP(전송제어 프로토콜)/IP(인터넷 프로토콜) 프로토콜 - HTTP, IP, TCP 등등..
> 인터넷에 관련된 다양한 프로토콜의 집합의 총칭

HTML: HyperText Markup Language

**HTTP: HyperText Transfer Protocol**
하이퍼 문서를 전송하는 것에서 시작, 모든 형태의 데이터 전송가능
인터넷의 모든 것은 HTTP로 이루어져있다.
HTTP 1.1 여전히 현재도 사용

#### APP
애플리케이션: HTTP -> 리퀘스트
> 편지지 작성, 편지지에는 양식이 정해짐, 앱 단에서 이루어짐, 그 후 iOS에 던져줌
> 데이터를 어떻게 주고 받을지에 대한 약속(요청/응답)
#### OS
트랜스포트: TCP -> 조각/ PORT(항구) 붙임
> 편지지를 조각내거나 PORT를 붙임, 멜론, 카카오톡 등등 각각 포트 번호가 있음, 편지지 봉투에 넣어둠
> 주고 받을 상태 확인 및 검증 / PORT (어떤 앱과 통신하는지)

인터넷: IP
> 편지지 봉투에 주소 작성
> 주고 받는 주소 (경로)

#### LAN
링크: 네트워크 -> MAC 주소 추가
> 랜카드에 고유의 번호들이 있음, 택배상자로 또 포장, 이후 다른 컴퓨터로 보냄


HTTP 보안 과정 필요함

클라이언트 Request(요청) - **query** ->
 <- Response(응답) 서버 - **data**

## HTTP 프로토콜 요청 메소드
- **GET** - 조회 (게시글 읽어오기)
- **POST** - 등록 (게시글 작성, 댓글 달기)
- **PUT** - 데이터 대체 / 없으면 생성 (게시글 수정, 데이터 전부 대체)
- **PATCH** - 부분 변경 (PUT에서 필요한 부분, 인스타 좋아요 누르기)
- **DELETE** - 삭제 (게시글 삭제)

### 응답 상태 코드
- 200번대 - 정상
- 300번대 - Redirection 리퀘스트를 완료하기 위해서 추가 동작 필요
- 400번대 - 클라이언트 에러, 잘못된 요청
- 500번대 - 서버 내부의 문제

## API
> Application Programming Interface

- 서버와 통신하는 api
- 애플이 미리 만들어둔 print함수 같은 것

쿼리 파라미터 
- api 주소에 ? 뒤에 붙는 것, 좀 더 구체적인 사항 요구 가능, GET 메소드에 주로 붙임
- key = value 형태
- ?로 시작, &로 추가 가능

==쿼리 파라미터를 통한 데이터 전송 - GET==
==메세지 바디를 통한 데이터 전송 - POST/PUT/PATCH

응답 데이터의 형태 -> JSON


## REST API
> RESTful하게 작성했나?

사이트주소/1 -> 상영중 영화목록 요청 GET 
이렇게 API 막 만들면 다른 개발자와 소통이 어려움

사이트주소/movielists -> 상영중 영화목록 요청 GET 

---

## iOS의 네트워킹

#### iOS 데이터 요청의 4단계
1. URL
2. URLSession - 브라우저 키고, 브라우저와 통신
3. dataTask - url 입력
4. 시작(resume) - 엔터

```swift
let movieURL = "www.naver.com" // API -> 이 문자열을 구조체로 만들기
let structUrl = URL(string: movieURL)! // URL 구조체

// 아래 두 가지 방식을 주로 사용함
let session = URLSession(configuration: .default)
let session = URLSession.shared // 싱클톤, 더 많이씀

// completionHandler -> 콜백 함수 -> 클로저
// URL 구조체로 네트워크 통신을 한 뒤에, 그 결과를 데이터나 응답, 에러로 줌
session.dataTask(with: structUrl) { data, response, error in
	if error != nil {
		print(error!)
		return
	}
	if let safeData = data {
		print(String(decoding: safeData, as: UTF8.self))
	}
}.resume() // 엔터 역할
```

- **세션**: 브라우저에서 서버와 연결된 탭, 연결된 상태
- 위 코드는 비동기적으로 동작하므로, 함수로 만들 때 콜백 함수 형태로 설계해야 한다.
  - `func performRequest(with urlString: String, completion: @escaping([Movie]?) -> Void)`




## JSON Parsing

> https://app.quicktype.io/

위 사이트에서 알아서 JSON 데이터를 Swift 코드로 변환해준다. 그 코드를 그냥 복붙해서 사용하면 된다. -> 서버에서 받아온 데이터

```swift
struct MovieData: Codable {
    let boxOfficeResult: BoxOfficeResult
}

// MARK: - BoxOfficeResult
struct BoxOfficeResult: Codable {
    let dailyBoxOfficeList: [DailyBoxOfficeList]
}

// MARK: - DailyBoxOfficeList
struct DailyBoxOfficeList: Codable {
    let rank: String
    let movieNm: String
    let audiCnt: String
    let audiAcc: String
    let openDt: String
}
```



위와 같은 서버에서 받아온 데이터를 **쓰기 좋게 변환하는 과정이 필요하다.**

```swift
func parseJSON1(_ movieData: Data) -> [DailyBoxOfficeList]? {
    do {
        let decoder = JSONDecoder()
        let decodedData = try decoder.decode(MovieData.self, from: movieData)
        return decodedData.boxOfficeResult.dailyBoxOfficeList
    } catch {
        return nil
    }
}
```

- `JSONDecoder()` : JSON 데이터를 분석하고 코드로 변형해준다.
- MovieData 형식으로 decode 한 후, dailyBoxOfficeList를 리턴한다.
- decoder의 `decode` 메소드는 에러를 내보낼 수 있기 때문에 앞에 `try`를 붙여야 하고 `try`를 캐치하기 위해선 `do-catch` 블록을 사용해야한다.



### Codable

> Decodable 프로토콜과 Encodable 프로토콜 둘 다 채택하고 있는 프로토콜이다.

JSONDecoder를 사용하려면 Decodable 프로토콜을 채택해야한다.



이제 `parseJSON1` 함수를 `session.dataTask(with: structUrl)` 안에서 사용해주면 된다.

```swift
guard let safeData = data else {
  return
}
var movieArray = parseJSON1(safeData)
dump(movieArray!)
// print보다 더 보기 좋게, 자세히 출력해준다.
```

`print(#function)` -> 함수 이름을 출력해준다.

