# API

> Application Programming Interface
>
> 응용 프로그램 인터페이스

- 컴퓨터나 컴퓨터 프로그램 사이의 연결

- 주소(Url, http)로 요청하면 문서(JSON)로 응답한다.

**API 활용시 확인 사항**

- 요청하는 방식에 대한 이해
  - 인증 방식
  - URL 생성
    - 기본 주소
    - 원하는 기능에 대한 추가 경로
    - 요청 변수 (필수와 선택)
- 응답 결과에 대한 이해
  - 응답 결과 타입 (JSON)
  - 응답 결과 구조



```python
# pip install requests
import requests
# URL로 요청을 보내서
order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'<url>'
# 응답 받은 값을 가져온다.
response = requests.get(URL)
print(response) # <Response [200]>

# 속성 예시
print(response.status_code)
# 200
print(response.text, type(response.text))
# 문자열

# 메서드 예시
#.json() 텍스트 형식의 JSON 파일을 파이선 데이터 타입으로 변경
print(response.json(), type(reponse.json()))
# <class 'dict>

data = response.json()
# data는 딕셔너리 => key로 접근
print(data.keys())
# dict_keys(['status','data'])
print(data.get('data').get('closing_price'))
```

```python
coins = response.get('data')

# coins : 딕셔너리
# key : coin 이름
# value : 딕셔너리(코인의 정보)
for coin in coins:
    # coin.get(coin) <= 코인의 정보인 딕셔너리
    # 그 딕셔너리의 closing price
    if coin == 'date':
        continue
        # 숨어있는 문자열 제외
    print(coin, coin.get(coin).get('closing_price'))
```

<br>

## TMDB API 활용 예시

```python
path
# 상세 경로
params = {
  'api_key': ''
  :'language' : 'ko-KR'
}

response = requests.get(BASE_URL+path, params=params).json()

# {movie_id} 변수처럼 사용해라, f스트링 느낌
```

<br>

## Lotto

```python
import requests

# 랜덤 하나 번호 고르고
# 실제로 내가 1024회 동안 해당 번호로 샀으면 얼마를 벌었을까?
# 1 ~ 5등

for n in range(1,10):
    URL = f'<url{n}>'
    response = requests.get(URL).json()
    print(response)
    
```

**모르면 반드시 Requests 사이트 문서 읽기**

1. url을 어떻게 만들어나갈지?

2. 어떤 응답의 형태들을 보는지?

<br>

```python
 cast=data.get("cast")
    crew=data.get("crew")
    return_data={"cast":[],"crew":[]}
    
    for baewoo in cast:
        if baewoo.get('cast_id')<10:
        return_data["cast"].append((baewoo.get('name')))
    for staff in crew:
        if staff.get('department')== "Directing":
            return_data["crew"].append(staff.get('name'))
    return(return_data)
```

> 리스트가 밸류인 딕셔너리 생성 후 반복문 값을 딕셔너리안 리스트의 밸류에 할당