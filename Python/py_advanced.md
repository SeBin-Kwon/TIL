# 💡 파이썬 응용 / 심화

## 추가 문법

### List Comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
  - 복잡해지면 가독성이 떨어짐

```python
[<expression> for <변수> in <iterable>]
[<expression> for <변수> in <iterable> if <조건식>]

even_list = [i**2 for i in range(10) if i % 2 == 0]
print(even_list)
# [0, 4, 16, 36, 64]
```

- 특정한 원소(요소)로 구성된 리스트 만들 때

  ```python
  cubic_list = []
  for number in range(1, 4):
      cubic_list.append(number**3) print(cubic_list)
  
  [number**3 for number in range(1,4)]
  # [1, 8, 27]

<br>

### Dictionary Comprehension

```python
{key: value for <변수> in <iterable>}
{key: value for <변수> in <iterable> if <조건식>}

cubic_dict = {}
for number in range(1, 4):
    cubic_dict[number] = number ** 3
print(cubic_dict)

{number: number**3 for number in range(1, 4)}
# {1: 1, 2: 8, 3: 27}
```

<br>

## lambda

### lambda [parameter] : 표현식

- 람다함수
  - 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
- 특징
  - return문을 가질 수 없음
  - 간편조건문외조건문이나반복문을가질수없음
- 장점
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  - `def`를 사용할 수 없는 곳에서도 사용가능

```python
# map(함수, 반복 가능한 것)
# 반복 가능한 것들의 모든 요소에 함수를 적용시킨 겨로가를
# map object로 반환한다.

# map(int, input().split())
# int 형 변환함수를
# input으로 받은 것을 쪼갠 결과인 리스트에 각각 적용한다.

numbers = [1, 2, 5, 10, 3, 9, 12]

# 기본 반복/조건 코드
result = []
for n in numbers:
    result.append(n*3)
print(result)
# [3, 4, 15, 30, 9, 27, 36]

# 만약에 map으로 쓰고 싶다면?
# 함수를 정의해야 한다.

def multiple_3(n):
    return n * 3
print(list(map(multiple_3, numbers)))
# [3, 4, 15, 30, 9, 27, 36]

# 함수를 정의하지 않고 임시적인 함수를 만들고 싶다. => lambda
print(list(map(lambda n:  n*3, numbers)))
# [3, 4, 15, 30, 9, 27, 36]
```

<br>

## filter

- `filter(function, iterable)`
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과가 `True`인 것들을 `filter object`로 반환

```python
# 3의 배수인 리스트로만 만들기
numbers = [1, 2, 5, 10, 3, 9, 12]

# 기본 반복/조건 코드
result = []
for n in numbers:
    if n % 3 == 0:
        result.append(n)
print(result)

# 람다 활용
print(list(filter(lambda n: n%3==0, numbers)))
# True만 출력

# 함수 활용
def is_3(n):
    return n % 3 == 0
print(list(filter(is_3, numbers)))

# def is_3_1(n):
#     if n % 3 == 0:
#         return True 
#     else: 
#         return False
```

<br>

## 파이썬 버전별 업데이트 3.8

```python
# 동적 타입 언어인 파이썬에서
# 정적 타입으로 바꿔주는 것이 아닌
# 그냥 주석, 메모

# 변수 어노테이션
a: int = 3
print(a)

# 함수 어노테이션
def add(x: int, y: int) -> int:
    return x + y
  
print(add(7,4)) # 11
print(add(hi, hello)) # hi hello

# 함수 어노테이션
def add2(x, y):
    return x + y 
print(add2(7, 4))
```

<br>

## 모듈 심화

### 파이썬 표준 라이브러리 (Python Standard Library, PSL)

- 파이썬에 기본적으로 설치된 모듈과 내장 함수
  - https://docs.python.org/ko/3/library/index.html
  - ex) random.py

<br>

### 파이썬 패키지 관리자(pip)

> PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

### pip 명령어

#### 패키지 설치

- 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음
- 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음
  - `pip install SomePackage`
  - `pip install SomePackage==1.0.5`
  - `pip install 'SomePackage>=1.0.4'`

- 모두 bash, cmd 환경에서 사용되는 명령어

#### 패키지 삭제

- pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌
  - `pip uninstall SomePackage`

#### 패키지 목록 및 특정 패키지 정보

- `pip list`
- `pip show SomePackage`

#### 패키지 freeze

- 설치된 패키지의 비슷한 목록을 만들지만, pip install에서 활용되는 형식으로 출력
- 해당하는 목록을 requirements.txt(관습)으로 만들어 관리함
- `pip freeze`

#### 패키지 관리하기

- 아래의 명령어들을 통해 패키지 목록을 관리[1]하고 설치할 수 있음[2]
- 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함
- `pip freeze > requirements.txt`
- `pip install –r requirements.txt`

<br>

## 가상 환경

>가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리 할 수 있음

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
  - 과거 외주 프로젝트 – django 버전 2.x
  - 신규 회사 프로젝트 – django 버전 3.x
- 프로젝트마다 다른 패키지를 사용할 수 있다.

<br>

### venv

> 가상 환경을 만들고 관리하는데 사용되는 모듈 (Python 버전 3.5부터)

- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
  - 특정 폴더에 가상 환경이 (패키지 집합 폴더 등) 있고
  - 실행 환경(예 – bash)에서 가상환경을 활성화 시켜
  - 해당 폴더에 있는 패키지를 관리/사용함

#### 가상 환경 생성

- 가상환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨
  - `python –m venv <폴더명>`

#### 가상환경 활용

- 가상 환경 활성화/비활성화
  - `source venv/Scripts/activate`

- 각 프로젝트별 가상환경(venv 폴더별로 고유한 프로젝트가 설치됨)
