# 모듈 (module)

> 합, 평균, 표준편차, ... 여러 함수, 기능들
>
> => 다양한 기능을 하나의 파일로 (모듈, module)
>
> => 다양한 파일을 하나의 폴더로 (패키지, package)
>
> => 다양한 패키지를 하나의 묶음으로 (라이브러리, library)
>
> => 패키지, 라이브러리를 관리하는 관리자 (pip)



## 모듈과 패키지

- 모듈
  - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것

### 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 내장 함수

```python
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

```python
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
  # lines = f.readline() 줄단위로 한줄씩 출력
  for line in f:
    print(line, end='')
```



## JSON

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
```

### 프로젝트

### 5번

for a in genre_ids

a => {'id:'28', 'name':...}

if a['id'] == id

g_names.append(a.get)

### 6번

5번 코드 복붙 후 반복문 또 돌리기

for movie in movies

(if문으로 중복제거 연습)