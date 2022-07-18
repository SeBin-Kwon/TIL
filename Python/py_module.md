# 📋 모듈 (module)

### 모듈

> 다양한 기능을 하나의 파일로 (모듈, module)

### 패키지

> 다양한 파일을 하나의 폴더로 (패키지, package)

### 라이브러리

> 다양한 패키지를 하나의 묶음으로 (라이브러리, library)

### pip

> 패키지, 라이브러리를 관리하는 관리자 (pip)



## 모듈과 패키지

- 모듈
  - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- 패키지
  - 특정 기능과 관련된 여러 모듈의 집합
  - 패키지 안에는 또 다른 서브 패키지를 포함


### 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 내장 함수

```python
import datetime

now = datetime.datetime123.now()
print(now, type(now))

# from datetime import datetime123
# now = datetime.now() 

import random

random.sample([1, 2, 3],2)
print(numbers, type(numbers))
# [1,2] <class 'list'>

random.sample(range(1,46,6)
number.sort() # 정렬하기
print(numbers, type(numbers))
# [2, 5, 13, 20, 29, 33] <class 'list'>
              
n = int(input('얼마쓸래?'))
for i in range(n):
	  random.sample(range(1,46,6)
	  number.sort() # 정렬하기
	  print(numbers, type(numbers))              
```



## 파일 입출력

- `'r'` : read (읽기 전용)

- `'w'` : write (쓰기 전용 - 덮어씀)

- `'a'` : append (쓰는데 파일 있으면 이어서 씀)

```python
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Happy Hacking!\n')
    for i in range(1, 6):
        f.write(f'{i} 번째!\n')

# 파일명, 어떤 모드로 열지,
# 인코딩을 설정
with open('students.txt', 'r', encoding='utf-8') as f:
  text = f.read()
  print(text, type(text)) # <class 'str'>
  names = text.split() # 공백과 개행은 같은 취급이라 쪼개짐, <class 'list'>
  cnt = 0
  for name in names:
    # name: 첫번째 시행 - 김세환
    # 언제? 김씨?
    if name.startswith('김'):
    # if name[0] == '김':
      cnt += 1
  print(cnt)
```

```python
with open('students.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
    # lines = f.readline()
    # print(lines, type(lines))

with open('students.txt', 'r', encoding='utf-8') as f:
  # lines = f.readline() 줄단위로 한줄씩 출력
  for line in f:
    print(line, end='')
```



## JSON

> - JavaScript Object Notation라는 의미의 축약어로 데이터를 저장하거나 전송할 때 많이 사용되는 **경량의 DATA 교환 형식**

```python
import json
# 파일을 열고,
f = open('stocks.json', 'r', encoding= 'utf-8')
# JSON을 파이썬 객체 형식으로 한다!
kospi = json.load(f)
samsung = kospi['stocks'][0]
print(samsung, type(samsung))

pprint # 딕셔너리를 좀더 보기 편하게 출력해줌, 알파벳 순으로

# StokcName 정보랑 ,closePrice 정보만 가진 딕셔너리를 만들고 싶어요!
result = {
  'stockName': samsung.get('stockName'),
  'closePrice': 
}
print(result)

from pprint import pprint

samsung = {
        "stockEndType": "stock",
        "itemCode": "005930",
        "reutersCode": "005930",
        "stockName": "삼성전자",
        "sosok": "0",
        "closePrice": "58,800",
        "compareToPreviousClosePrice": "1,300",
        "compareToPreviousPrice": {
          "code": "2",
          "text": "상승",
          "name": "RISING"
        }}
pprint(samsung)
print(samsung)
```
