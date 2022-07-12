# 📘 Python basics

## 컴퓨터 프로그래밍 언어

- 컴퓨터 (**compute**r) : compute 계산하다

  > caculation + Remember 계산하고 기억한다.

- 프로그래밍 (**program**ming)

  > 명령어의 모음(집합)

- 언어

  > 자신의 생각을 나타내고 전달하기 위해 사용하는 체계
  >
  > 문법적으로 맞는 말의 집합
  >
  > 컴퓨터에게 명령하는 말

- 컴퓨터에게 명령하기 위한 약속

  - 선언적 지식(declarative knowledge) : 사실에 대한 내용
- **명령적 지식(imperative knowledge) : "How-to"**

### **프로그래밍 기본 규칙**

> **1. 코드는 위에서부터 아래로 실행**
>
> **2. 오른쪽의 결과를 왼쪽에 할당**



## 파이썬의 특징

- Easy to learn
  - 변수의 별도의 타입 지정이 필요 없음 -> `동적 타이핑 언어`
  - 문법 표현이 매우 간결함
- Expressive Language
  - 간결하게 작성 가능

- 크로스 플랫폼 언어
  - 윈도우 (Windows), macOS, 리눅스(Linux), 유닉스(Unix) 등 다양한 운영체제에서 실행가능

- 인터프리터 언어
  - 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
  - 코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인할 수 있음
- **객체 지향 프로그래밍**
  - 파이썬은 객체지향 언어이며, 모든 것이 `객체`로 구현되어 있음
  - 객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것
    - 물건 / 대상...~ 어떠한 것들

## 기초 문법

**코드 스타일 가이드**를 최대한 지키기, 일관성 있게 작성하기

- [PEP8](https://www.python.org/dev/peps/pep-0008/)
- [Google Style guide](https://google.github.io/styleguide/pyguide.html)



### 들여쓰기(Identation)

- Space Sensitive

  - 문장을구분할때,들여쓰기(indentation)를사용

  - 들여쓰기를 할 때는 4칸(space키 4번) 혹은 1탭(Tab키 1번)을 입력

  - 주의! 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용, 혼용하면안됨

    - Tab으로 들여쓰면 계속 탭으로 들여써야 함

    - 원칙적으로는 공백 (빈칸, space) 사용을 권장* PEP8 권장사항


### 변수 (Variable)

> 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름 ex) a = 8

- 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에, 즉, 참조하는 객체가 바뀔수 있기 때문에 `변수`라고 불림
- 변수는 할당 연산자(=)를 통해 값을 `할당`(assignment)
- type()
  - 변수에 할당된 값의 타입
- id()
  - 변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값이며, 메모리주소

### 변수 할당

- 같은 값을 동시에 할당할 수 있음

  ```python
  x = y = 1004
  print(x, y)
  ```

- 다른 값을 동시에 할당 할 수 있음(multiple assignment)

  ```python
  x, y = 1, 2
  print(x, y)
  ```



### 식별자 (Identifiers)

> 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름(name)

- 규칙
  - 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
  - 첫글자에숫자가올수없음
  - 길이제한이 없고, 대소문자를 구별
  - 다음의 키워드(keywords)는 예약어(reserved words)로 사용할 수 없음
    - ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
  - 내장함수나 모듈 등의 이름으로도 만들면 안됨
    - 기존의이름에다른값을할당하게되므로더이상동작하지않음



### 사용자 입력

>  imput([prompt])

- 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수

- 대괄호 부분에 문자열을 넣으면 입력 시, 해당 문자열을 출력할 수있음

- **반환값은 항상 문자열의 형태로 반환**

  ```python
  name = input('이름을 입력해주세요 : ') print(name)
  # 이름을 입력해주세요 : 파이썬 type(name)
  # str
  ```



### 주석

- 코드에 대한 설명
  - 중요한 점이나 다시 확인하여야 하는 부분을 표시
  - 컴퓨터는 주석을 인식하지 않음 사용자만을 위한 것
- 가장 중요한 습관
  - 개발자에게 주석을 작성하는 습관은 매우 중요
  - 쉬운 이해와 코드의 분석 및 수정이 용이
    - 주석은 코드 실행에 영향을 미치지 않을 뿐만 아니라
    - 프로그램의 속도를 느리게 하지 않으며, 용량을 늘리지 않음
- 한 줄 주석
  - 주석으로 처리될 내용 앞에 `#` 입력



## 파이썬 기본 자료형 (Python Datatype)

### 자료형 분류

- 불린형(Boolean Type) : True / False

- 수치형(Numeric Type)

  - int (정수, integer)
  - float (부동소수점, 실수, floating point number)
  - complex (복소수,complex number)

- 문자열(String Type)

- None

  - 파이썬 자료형 중 하나

  - 값이 없음을 표현한다.
  - 일반적으로 반환 값이 없는 함수에서 사용하기도 함.




## 불린형(Boolean Type)

### 불린(Boolean)

- `True / False` 값을 가진 타입은 `bool`
- 비교/논리 연산을 수행함에 있어서 활용됨
- 다음은 모두 `False`로 변환
  -  0, 0.0, (), [], {}, '', None
-  `bool()` 함수
  - 특정 데이터가 True인지 False인지 검증



### 논리 연산자(Logical Operator)

> 논리식을 판단하여 참(True)와 거짓(False)를 반환함

| 연산자  |              내용              |
| :-----: | :----------------------------: |
| A and B |    A와 B 모두 True시, True     |
| A or B  |   A와 B 모두 False시, False    |
|   Not   | True를 False로, False를 True로 |

- `and` : 모두 참인 경우 참, 그렇지 않으면 거짓
- `or` : 둘 중 하나만 참이라도 참, 그렇지 않으면 거짓
- `not` : 참 거짓의 반대의 결과



## 수치형 (Numeric Type)

### 정수(Int)

- **모든 정수의 타입은 `int` 타입** 
- 매우 큰 수를 나타낼 때, 오버플로우가 발생하지 않음
  - 오버플로우(overflow) : 데이터 타입별로 사용할 수 있는 메모리의 크기를 넘어서는 상황


### 실수(Float)

- 정수가 아닌 모든 실수는 `float` 타입
- 부동소수점
  - 실수를 컴퓨터가 표현하는 방법 -> 2진수(비트)로 숫자를 표현
    - 이 과정에서 `floating point rounding error`가 발생
    - 부동소수점에서 실수 연산 과정에서 발생 가능
    - **값 비교하는 과정에서 정수가 아닌 실수인 경우 주의 할 것**


- 알고리즘에서는 실수는 잘 안다룸, 보통 확률처리에서 사용

### 복소수(Complex)

- 실수부와 허수부로 구성된 복소수는 모두 `complex` 타입
- 허수부를 `j`로 표현



### 산술 연산자(Arithmetic Operator)

- 기본적인 사칙연산 및 수식 계산

| 연산자 |             내용              |
| :----: | :---------------------------: |
|   +    |             덧셈              |
|   -    |             뺄셈              |
|   *    |             곱셈              |
| **% ** | **나머지 (중요! ex : 홀,짝)** |
| **/**  |          **나눗셈**           |
| **//** |            **몫**             |
| ****** |         **거듭제곱**          |

### 복합 연산자(In-place Operator)

- 연산과 할당이 함께 이뤄짐

| 연산자  |    내용    |
| :-----: | :--------: |
| a += b  |   a=a+b    |
| a -= b  |   a=a-b    |
| a *= b  |  a =a * b  |
| a /= b  |  a =a / b  |
| a //= b | a = a // b |
| a %= b  |   a=a%b    |
| a **= b | a = a ** b |

### 비교 연산자(Comparison Operator)

- 값을 비교하며, True / False 값을 리턴함

| 연산자 |            내용             |
| :----: | :-------------------------: |
|   <    |            미만             |
|   <=   |            이하             |
|   >    |            초과             |
|   >=   |            이상             |
|   ==   |            같음             |
|   !=   |          같지 않음          |
|   is   |    객체 아이덴티티(OOP)     |
| is not | 객체 아이덴티티가 아닌 경우 |



## 문자열 (String Type)

### 문자열(String Type)

- 모든 문자는 `str` 타입
- 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기
  - 문자열을 묶을 때 동일한 문장부호를 활용
  - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함

### 중첩 따옴표 (Nested Quotes)

- 따옴표 안에 따옴표를 표현할 경우
  - 작은 따옴표가 들어있는 경우는 큰 따옴표로 문자열 생성
  - 큰 따옴표가 들어있는 경우는 작은 따옴표로 문자열 생성

### 삼중 따옴표 (Triple Quotes)

- 작은 따옴표나 큰 따옴표를 삼중으로 사용

  - 따옴표 안에 따옴표를 넣을 때

  - 여러줄을 나눠 입력할 때 편리

    ```python
     print('''문자열 안에 '작은 따옴표'나 "큰 따옴표"를 
     사용할 수 있고 여러 줄을 사용할 때도 편리하다.''')
    ```

### 문자열(String Type) 연산자

### 인덱싱

- 인덱스를 통해 특정 값에 접근할 수 있음
- **컴퓨터에서는 숫자를 0부터 센다.**

### 문자열 슬라이싱(Slicing) 예제

> [a, b, c, d, e, f, g, h, i]
>
> 0  1  2  3  4  5  6  7  8

- s[1] ⇒ ‘b’

- s[2:5] ⇒ 'cde' 
  - 2이상, 5미만

- s[2:5:2] ⇒ 'ce'
  - step

- s[5:2:-1] ⇒ 'fed' 
  - 음수는 역순으로

- s[:3] ⇒ 'abc' 
  - 처음부터 3미만

- s[5:] ⇒ 'fghi' 
  - 마지막부터 5이상

- s[::] ⇒ 'abcdefghi’ 
  - 처음부터 끝까지 1씩, 그대로
    - s[0:len(s):1]과 동일

- s[::-1] ⇒ 'ihgfedcba’
  - 마지막부터 처음까지, 거꾸로
    - s[-1:-(len(s)+1):-1]과 동일

>`len` 함수 : 길이를 알려줌
>
>마지막 값 구하기 : 길이 빼기 -1

### 기타

- 결합 (Concatenation)

  ```python
  'hello, ' + 'python!' # 'hello, python!'
  ```

- 반복 (Repetition)

  ```python
  'hi!' * 3
  # 'hi!hi!hi!'
  ```

- **포함 (Membership)**

  ```python
  'a' in 'apple' # True
  'app' in 'apple' # True
  'b' in 'apple'
  # False
  ```

### 문자열(String Type) 활용

### Escape sequence

- 문자열 내에서 특정 문자나 조작을 위해서 `\` (역슬래쉬) 활용하여 구분

  - 개행(엔터, 줄 바꿈) : `\n`

  - 역슬래쉬를 표현할 땐 : `\\`

  - 따옴표 : `\'\'`
  - 탭 : `\t`
  - 널(Null) : `\0`
  - 캐리지리턴 : `\r`

### String Interpolation

- 문자열 안에 변수 넣기, 문자열을 변수를 활용하여 만드는 법

  - %-formatting

    ```python
     name = 'Kim' score = 4.5
    print('Hello, %s' % name) print('내 성적은 %d' % score) print('내 성적은 %f' % score)
    # Hello, Kim
    # 내 성적은 4
    # 내 성적은 4.500000
    ```

  - f-string

    - 앞에 소문자 f를 붙이고 변수를 {}로 감싼다.

    ```python
     name = 'Kim'
    score = 4.5
    print(f'Hello, {name}! 성적은 {score}') 
    # Hello, Kim! 성적은 4.5
    pi = 3.141592
    print(f'원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*2*2}') # '원주율은 3.14. 반지름이 2일때 원의 넓이는 12.566368'
    ```

- **문자열과 숫자를 더할 수 없다. 같은 타입끼리 더할 수 있다.**

### 문자열 특징

- Immutable : 변경 불가능함
- Iterable : 반복 가능함

## 형 변환(Typecasting)

> 파이썬에서 데이터 형태로 서로 변환할 수 있음

- 암시적 형 변환 (Implicit)
  - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환 하는 경우
    - bool
    - Numeric type (int, float, complex)

- 명시적 형 변환 (Explicit)
  - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환 하는 경우
    - int
      str,float ⇒ int
    - float
      str,int ⇒ float
    - str
      int, float, list, tuple, dict ⇒ str

  - 2를 '2'로, 숫자를 문자로 변환 할 수 있다.
  - 문자는 숫자로 변환 할 수 없다. (*형식에 맞는 문자열만 가능*)




## 컨테이너 (Container)

>여러 개의 값을 담을 수 있는 것(객체)으로, 서로 다른 자료형을 저장할 수 있음
>
>ex) List,tuple

### 컨테이너 분류

- 순서가 있는 데이터 (Ordered) vs. 순서가 없는 데이터 (Unordered)
  - 순서가 있다 != 정렬되어 있다.

- 시퀀스 : 순서가 있다. <- 인덱스로 접근

  - 문자열 (immutable) : 문자들의 나열
- 리스트 (mutable) : 변경 가능한 값들의 나열
  - 튜플 (immutable) : 변경 불가능한 값들의 나열
- 레인지 (immutable) : 숫자의 나열
- 컬렉션 / 비시퀀스 : 순서가 없다.
  - 세트 (mutable) : 유일한 값들의모음
  - 딕셔너리 (mutable) : 키-값들의 모음


## 시퀀스형 컨테이너 (Sequence Container)

### 시퀀스형 주요 공통 연산자

|       연산       |                            결과                            |
| :--------------: | :--------------------------------------------------------: |
|       s[i]       |             s 의 i 번째 항목, 0에서 시작합니다             |
|      s[i:j]      |               s 의 i 에서 j 까지의 슬라이스                |
|     s[i:j:k]     |           s 의 i 에서 j 까지 스텝 k 의 슬라이스            |
|       s+t        |                   s 와 t 의 이어 붙이기                    |
| s * n 또는 n * s |               s 를 그 자신에 n 번 더하는 것                |
|      x in s      | s 의 항목 중 하나가 x 와 같으면 True, 그 렇지 않으면 False |
|    x not in s    | s 의 항목 중 하나가 x 와 같으면 False, 그 렇지 않으면 True |
|      len(s)      |                         s 의 길이                          |
|      min(s)      |                    s 의 가장 작은 항목                     |
|      max(s)      |                     s 의 가장 큰 항목                      |

### 리스트 (List)

값들의 나열

인덱스 순서로 접근

students = ['동현', '효근', '수경', '나영', '다겸', '예지']

print(students[0]) # 동현

print(students[-1]) # 예지



students_1 = ['동현', '효근']

students_2 = ['수경', '나영']

students_3 = ['다겸', '예지']

students = [['동현', '효근'], ['수경', '나영'], ['다겸', '예지']]



딕셔너리

키와 값의 쌍으로 이뤄짐

키로 접근함

```python
students = {
	'1회차' : ['동현', '효근']
	'2회차' : ['수경', '나영']
	'3회차' : ['다겸', '예지']
}
print(['1회차'])
```



numbers = [1, 100, 20, 50]

print(numbers[1]) 100

print(numbers[2:3]) 20

print(numbers[0:3:-1]) 없음 그냥 머릿속에서 지우기 <- <0 1 2> 3

print([1,2] + [3]) [1, 2, 3] 리스트를 합쳐줌

print(len(numbers)) 4

print(sum(numbers)) 171

print(max(numbers)) 100

print(min(numbers)) 1



리스트(List)

- 변경 가능한 값들의 나열된 자료형
- 변경 가능하며()값을 바꿔치기 가능함

인덱스가 0에 해당하는 값을 -1로 바꾼다.

[-1,1]

### 리스트 값 추가 / 삭제

.append()

.pop()



### 튜플(Tuple)

- **변경 불가능하며**

리스트랑 다 똑같은데 변경만 안됨



### 레인지(Range)

range(3) -> 0, 1, 2

range(1,4) - > 1, 2, 3 / 1이상, 4미만

range (1, 5, 2) -> 1, 3

## 비시퀀스

### 세트(Set)집합

- **유일한 값들의 모음**
- 순서가 없고 중복된 값이 없음
  - {3, 1, 2, 3} -> {3,1,2}

셋 활용

아래의 리스트에서 고유한 지역의 개수는?

locations = [서울,,]

print(set(locations))

print(len(set(locations))) -> 6



### 딕셔너리

**키 - 값**

리스트를 키로 할 수는 없다.

.pop()은 값을 안없애지만 키를 삭제함

키가 없으니 해당 값 출력은 오류가 뜸

input은 모두 string으로 저장된다. 따라서, 숫자로 활용하기 위해서는 항상 int로 변환해야 한다.

a = '1 2 3'

print(a.split())

-> ['1', '2', '3']

문자열을 특정 단위로 쪼개줌, 리스트로

sep(seperator)를 작성하면 값 사이에 해당 문자르 넣어준다.