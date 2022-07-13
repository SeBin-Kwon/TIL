# 🔍 함수 (function)

## 함수 기초

> len(), sum(), print()..
>
> Decomposition : 기능을 분해해서 재사용 가능
>
> Abstraction : 추상화, 복잡한 내용을 숨기고 기능에 집중하여 사용할 수 있음 (블랙박스)

- 특정 기능을 하는 코드의 조각(묶음)
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용
- 사용자 함수 (Custom Function)
  - 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능

```python
def function_name(parameter):
    # code block
    return returning_value
```



### 함수를 사용해야 하는 이유

> 1. 코드 중복 방지
>
> 2. 재사용 용이

### 함수 기본 구조

- 선언과 호출 (define & call)
- 입력 (Input)
- 범위 (Scope)
- 결과값 (Output)

### 선언과 호출

```python
def foo():
    return True
foo()

def add(x, y): 
    return x + y
add(2, 3)
```

- 함수의 선언은 `def` 키워드를 활용함
- 들여쓰기를 통해 `Function body` (실행될 코드 블록)를 작성함
  - Docstring은 함수 body 앞에 선택적으로 작성 가능
    - 작성시에는 반드시 첫번째 문장에 문자열 ''' '''
- 함수는 `parameter`를 넘겨줄 수 있음
- 함수는 동작 후에 `return`을 통해 결과값을 전달함
- 함수는 `함수명()`으로 호출
  - `parameter`가 있는 경우, `함수명(값1,값2,...)`로 호출

```python
# 정의
# 1. def
# 2. Input : a, b
def add(a, b):
    # 4. return : 값을 반환
    return a + b
# 호출
print(add(5, 10))

# 내장 함수 호출
print(sum([1, 2, 3]))
```

```python
num1 = 0
num2 = 1
def func1(a, b):
    return a + b
def func2(a, b): return a - b
def func3(a, b):
    return func1(a, 5) + func2(5, b)
result = func3(num1, num2)
print(result)
# 9
```

- 함수는 호출되면 코드를 실행하고 `return` 값을 반환하며 종료된다.



## 함수의 결과값 (Output)

### return

- **함수는 반드시 값을 하나만 `return`한다.**
  - 명시적인 `return`이 없는 경우에도 `None`을 반환한다.
- 함수는 `return`과 동시에 실행이 종료된다.
- 튜플 반환
  - 함수는 x, y인자로 받고 하나의 `tuple`로 반환한다.
  - `print()`는 `None type`이다.

```python
def minus_and_product(x, y):
    return x - y
    return x * y
minus_and_product(4, 5) # x - y만 실행된다.

def minus_and_product(x, y): 
    return x - y, x * y
minus_and_product(4, 5) # (-1, 20) 튜플로 반환됨.
```

```python
def foo():
    return 1, 2

result = foo()
print(result, type(result)) 
# (1, 2) <class 'tuple'> 

def no():
    a = 1

result = no() 
print(result, type(result)) 
# None <class 'NoneType'>


# print 함수는 
# 출력을 해주고, return 값은 없습니다. (None)
a = print('hi')
print(a, type(a)) # None <class 'NoneType'>
```



## 함수의 입력 (Input)

- `Parameter` : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
- `Argument` : 함수를 호출할 때, 넣어주는 값

### argument

- 함수 호출 시 함수의 `parameter`를 통해 전달되는 값
- `Argument`는 소괄호 안에 할당 `func_name(argument)`
- `필수 Argument` : 반드시 전달되어야 하는 argument
- `선택 Argument` : 값을 전달하지 않아도 되는 경우는 기본 값이 전달

#### positional arguments

- 기본적으로 함수 호출 시 `Argument`는 위치에 따라 함수 내에 전달됨

```python
def add(x, y):
  return x + y

add(2, 3)# 2의 위치 x, 3의 위치 y
```

#### keyword arguments

- 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
- `Keyword Argument` 다음에 `Positional Argument`를 활용할 수 없음

```python
def add(x, y):
  return x + y

add(x=2, y=5)
add(2, y=5)
# add(x=2, 5) 안됨
# add(y=5, x=2) 됨
```

#### Defult Arguments Values

- 기본값을 지정하여 함수 호출 시 `argument` 값을 설정하지 않도록 함
  - 정의된 것 보다 더 적은 개수의 `argument`들로 호출 될 수 있음

```python
def add(x, y=0):
  return x + y

add(2)
```

#### 정해지지 않은 개수의 arguments

- 여러 개의 `Positional Argument`를 하나의 필수 `parameter`로 받아서 사용
  - 몇 개의 `Positional Argument`를 받을지 모르는 함수를 정의할 때 유용 
- `Argument`들은 튜플로 묶여 처리되며, `parameter`에 `*`를 붙여 표현

```python
def add(*args):
  for args in args:
    print(arg)
    
add(2)
add(2, 3, 4, 5) # tuple type
```

#### 정해지지 않은 개수의 keyword arguments

- 함수가 임의의 개수 `Argument`를 `Keyword Argument`로 호출될 수 있도록 지정
- `Argument`들은 딕셔너리로 묶여 처리되며, `parameter`에 `**`를 붙여 표현

```python
def family(**kwargs):
  for key, value in kwargs:
    print(key, ":", value)
    
family(father='John', mother='Jane', me='Jone Jr.')
```

```python
# 기본값이 sep는 ' '으로 정의가 되어 있음.
print('hi', 'hello') # hi hello
# 키워드로 sep를 바꿔서 호출할 수 있음
print('hi', 'hello', sep='-') # hi-hello
print(1, 2, 3, 4, 5, 6, 7, 8)

# 정해지지 않은 갯수의 인자
def my_add(*numbers):
    # 내부적으로 numbers가 tuple
    return numbers 

result = my_add(1, 2, 3)
print(result, type(result)) # (1, 2, 3) <class 'tuple'>

def my_func(**kwargs):
    return kwargs

result = my_func(name='홍길동', age='100', gender='M')
print(result, type(result)) # {'name': '홍길동', 'age': '100', 'gender': 'M'} <class 'dict'>
```



## 함수의 범위 (Scope)

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수

```python
def foo():
    a = 1 # local scope
foo()
print(a) # global scope
# NameError : name 'a' is not defined
# 함수 안에는 변수 a가 있지만 글로벌 공간에는 없어서 변수 a는 정의되지 않았다고 나옴
```

### 객체 수명주기

- 객체는 각자의 수명주기(lifecycle)가 존재
- built-inscope
  - 파이썬이 실행된 이후부터 영원히 유지
    - `print, sum, len...`
- globalscope
  - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    - `a = 3`
- local scope
  - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
    - `def ... a = 1`

### 이름 검색 규칙 (Name Resolution)

- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
  - `Local scope` : 함수
  - `Enclosed scope` : 특정 함수의 상위 함수
  - `Global scope` : 함수 밖의 변수, Import 모듈
  - `Built-inscope` : 파이썬 안에 내장되어 있는 함수 또는 속성
- 즉, 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음

```python
print(sum)
print(sum(range(2)))
sum = 5
print(sum)
print(sum(range(2)))

# TypeError TraceBack(most recent call last)
# 3 sum = 5
# 4 print(sum)---->
# 5 print(sum(range(2)))
# TypeError: 'int' object is not callable

sum = 5
print(sum([1, 2, 3]))

# sum이 지금은 5가 되어버림...
# Built-in scope에 sum 함수가 있었음.
# Global scope에 sum이름의 변수를 만들었음.
# 제가 찾으니까 L->E->G->B
```

- 변수 함수에 넣고싶으면 함수 내부적으로 넣거나 아예 인자를 만들기

## 함수 응용

### 내장 함수 응용

- 파이썬 인터프리터에는 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음

### map

- map(function, iterable)

  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과를 map object로 반환

  - 특정한 함수를 반복적으로 적용 하고 싶을 때 사용

```python
numbers = ['1', '2', '3']
new_numbers_2 = map(int, numbers)
print(new_numbers_2, type(new_numbers_2)) 
# <map object at 0x0000023BE69A2C70> : 이미 함수가 모두 적용됨
print(list(new_numbers_2)) 
#[1, 2, 3] 리스트 형변환을 통해 결과 직접 확인 가능

```

```python
n, m = map(int, input().split())
print(n*m)
#int() = 내장 함수
#input() = 타입 : 항상 string(문자열)
#문자열.split() = 타입 : 항상 list(리스트) 내가 구분값을 기준으로 쪼개겠다.
#문자열로 받을 것은 각각을 공백을 기준으로 리스트로 쪼갰다! -> 리스트! ['10', '20']

#map() = 어떤 함수를 반복가능한 것들의 요소에 모두 적용시킨 결과!

#int 함수를 input().split() 리스트의 모든 요소에 적용한 결과 -> map object [10, 20]
#n, m = [10, 20]
```

### end =

- `print()`는 기본 `end = '\n'`이므로 print 출력이 된 이후 뒤에 뭐를 붙이고 싶을 때, 개행을 없애고 싶을 때 (`end = ''`)



## 참고 자료

[파이썬 자습서](https://docs.python.org/ko/3/tutorial/index.html)

[파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html)