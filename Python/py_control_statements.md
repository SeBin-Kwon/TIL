# 🕹 제어문(Control Statement)

- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함
- 제어문은 순서도(flow chart)로 표현이 가능



## 조건문 (Conditional Statement)

### 조건문 기본

> 조건문은 참 / 거짓을 판단할 수 있는 조건식과 함께 사용

#### 기본 형식 

```python
if < expression >:
    # Run this Code block
else:
# Run this Code block
```

- expression에는 참 / 거짓에 대한 조건식
  - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭을 실행
  - 이외의 경우 `else` 이후 들여쓰기 되어있는 코드 블럭을 실행
    - `else`는 선택적으로 활용 가능함

- **`else`는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능**.
- 조건문에서 `else`는 생략이 가능하다.

```python
# 1. num은 input으로 사용자에게 입력을 받으세요.
num = int(input())
print(num, type(num))
# 2. 조건문을 통해서 홀수/짝수 여부를 출력하세요.
# 숫자로서의 num!
if num % 2 == 1:
    print('홀수')
else:
    print('짝수')
```



## 복수 조건문

- 복수의 조건식을 활용할 경우 `elif`를 활용하여 표현함
- 조건식을 동시에 검사하는 것이 아니라 순차적으로 비교

```python
 if <expression>: # Code block
elif <expression>:
    # Code block
elif <expression>:
    # Code block
else:
# Code block
```

```python
dust = 100
# dust가 150보다 크면, 매우 나쁨
if dust > 150:
    print('매우 나쁨')
# 80보다 크면, 나쁨
elif dust > 80:
    print('나쁨')
# 30보다 크면, 보통
elif dust > 30:
    print('보통')
# 좋음
# else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능
# 조건문에서 else는 생략이 가능하다.
else:
    print('좋음')
```



## 중첩 조건문

- 조건문은 다른 조건문에 중첩되어 사용될 수 있음
  - 들여쓰기를 유의하여 작성할 것

```python
if <expression>:
    # Code block
if <expression>:
# Code block
else:
# Code block
```

```python
dust = int(input())
if dust > 150:
    if dust > 300:
        print('실외활동을 자제하세요.')
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust < 0:
        print('음수 값입니다.')
    else:
        print('좋음')
```



## 조건 표현식 (Conditional Expression)

>  조건 표현식을 일반적으로 조건에 따라 값을 할당 할 때 활용

```python
<true인 경우 값> if <expression> else <false인 경우 값>
```

```python
num = -10

## 조건문 코드
# 1. 양수면 그대로
if num >= 0:
    value = num
# 2. 음수면 -붙여서
else:
    value = -num 
print(num, value)

# 조건 표현식 코드, 절대값을 저장하기 위한 코드
value = num if num >= 0 else -num 
```

- 복잡한 코드에서는 가독성으로 인해 사용 불가능 하다. elif는 사용할 수 없다.



## 반복문 (Loop Statement)

> 특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장

### 반복문의 종류

- while 문
  - 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
- for 문
  - 반복가능한 객체를 모두 순회하면 종료 (별도의 종료조건이 필요 없음)
- 반복 제어
  - break, continue, for-else



## While 문

> while 문은 조건식이 참인 경우 반복적으로 코드를 실행

```python
 while <expression>: # 종료 조건
      # Code block
```

- 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행 됨
- 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
- **while문은 무한 루프를 하지 않도록 종료조건이 반드시 필요**
  - 참에서 거짓을 변하는 코드를 작성해야한다.


```python
# 처음 시작 값, 값 초기화
n = 0
# 0부터 더하기 위해서
result = 0
# user_input 값
user_input = int(input())

# 1
while n < user_input:
    print(f'n: {n}, result: {result}')
    n += 1
    result += n
print(result)
```

- 종료는 n이 user input보다 커지면 종료

- 곱을 구할 땐 result의 초기값을 1로 설정해야 한다.



## for 문

> for 문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)요소를 모두 순회함

```python
for <변수명> in <iterable>:
    # Code block
```

- 통에 있는걸 하나씩 다 꺼내서 변수명에 담아준다.
- 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음

### For문 일반 형식

- `Iterable`
  - 순회할 수 있는 자료형(str,list, dict 등)
  - 순회형 함수(range, enumerate)

### 문자열 순회

- 사용자가 입력한 문자를 한 글자씩 세로로 출력하시오.

```python
chars = input()
for char in chars:
    print(char)
```

#### range 활용

```python
for idx in range(len(chars)):
    print(chars[idx])
```

- **index를 기준으로 순회를 한다.**

### enumerate 순회

- `enumerate()`
  - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
    - (index, value) 형태의 tuple로 구성된 열거 객체를 반환

```python
# range 활용
members = ['민수', '영희', '철수']
for i in range(len(members)):
    print(f’{i} {members[i]}')
          
# enumerate 순회          
for i, member in enumerate(members):
    print(i, member) # i, member = 0, '민수'
          
enumerate(members)
# <enumerate at 0x105d3e100>
          
list(enumerate(members)) # 숫자와 값의 tuple
# [(0, '민수'), (1, '영희'), (2, '철수')]
          
list(enumerate(members, start=1))
# [(1, '민수'), (2, '영희'), (3, '철수')]
# 기본값 0, start를 지정하면 해당 값부터 순차적으로 증가
```

### 딕셔너리 순회

> 딕셔너리는 기본적으로 `key`를 순회하며, `key`를 통해 값을 활용

```python
grages{'john': 80, 'eric': 90}
for name in grades:
    print(name, grades[name])
    # john 80 eric 90
```



## 반복문 제어

- `break`
  - 반복문을 종료

```python
n=0
while True:
    if n == 3:
        break
print(n) n += 1
# 0 1 2

for i in range(10):
    if i > 1:
print('0과 1만 필요해!')
break
# 0 1 0과 1만 필요해!
```

- `continue`
  - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
    - continue를 만나면, 이후 코드인 `print(i)`가 실행되지 않고 바로 다음 반복을 시행

```python
for i in range(6):
    if i % 2 == 0
        continue
    print(i) # 1 3 5
```

- `for - else`
  - 끝까지 반복문을 실행한 이후에 else문 실행
  - else 문은 break로 중단되었는지 여부에 따라 실행
    - break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음
  

```python
word = 'banana'
for char in word:
    if char == 'b':
        print('b!')
        break
    else:
        print(char)
else:
    print('b가 없습니다.')
# b!
```
