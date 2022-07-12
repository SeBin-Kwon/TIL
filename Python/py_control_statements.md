# 🕹 제어문(Control Statement)

- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함
- 제어문은 순서도(flow chart)로 표현이 가능

## 조건문

> 조건문은 참 / 거짓을 판단할 수 있는 조건식과 함께 사용

- expression에는 참 / 거짓에 대한 조건식

```python
num = int(input())
if num % 2 == 1:
  print('홀수')
else:
  print('짝수')
```

## 복수 조건문

```python
dust = int(input())
if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```

- **`else`는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능**.

- 조건문에서 `else`는 생략이 가능하다.



## 중첩 조건문

> 조건문은 다른 조건문에 중첩되어 사용될 수 있음

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

## 조건 표현식

> 조건 표현식을 일반적으로

```python
if num >= 0:
    value = num
else:
    value = -num
print(num,value)
```

```python
value = num if num >= 0 else -num
print(num,value)
```

- 복잡한 코드에서는 가독성으로 인해 사용 불가능 하다. elif는 사용할 수 없다.

## 반복문

- while 문
- for 문
- 반복 제어



## While 문

> while 문은 조건식이 참인 경우 반복적으로 코드를 실행

- 조건이 참인 경우 들여쓰기

```python
n = 0
result = 0
user_input = int(input())
while n <= user_input:
    result += n
    n += 1
print(result)
```



실습

총합을 구하시오(0으로 설정)

0 + 0 = 0

0 + 1 = 1

1 + 2 = 3

3 + 3 = 6

종료는 n이 user input보다 커지면 종료

곱을 구하시오(result의 초기값은 1로 설정해야한다.)

참에서 거짓을 변하는 코드를 작성해야한다.

## for 문

> for 문은 시퀀스(string,)를 포함한 순회가능한 객체(iterable)요소를 모두 순회함

```python
for <변수명> in <
```

통에 있는걸 하나씩 다 꺼내서 변수명에 담아준다.



### 문자열 순회

```python
chars = input()
for char in chars:
    print(char)
```

### range 활용

```python
for idx in range(len(chars)):
    print(chars[idx])
```

- **index를 기준으로 순회를 한다.**

### enumerate 순회ㅣ

튜플을 활용한다.

i, member = 0, '민수'



### 딕셔너리 순회

> 딕셔너리는 기본적으로 `key`를 순회하며, `key`를 통해 값을 활용

```python
grages{'john': 80, 'eric': 90}
for name in grades:
print(name, grades[name])
```



## 반복문 제어

- break
  - 반복문을 종료

```python
```



- continue
  - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

```python
for i in range(6):
    if i % 2 == 0
        continue
    print(i)
```



- for - else
  - else 문은 break로 중단되었는지 여부에 따라 실행

```python
for char in 'banana':
    if char == 'b':
```



## 실습 문제 풀이

### 문제 6 최대값 구하기

[0, 20, 100, 40]

0과 20 비교 -> 최대값 20 기록

20과 100 비교 -> 최대값 100 기록

100과 40 비교 -> 최대값 기록 안함

n은 숫자들

for문으로 반복하기

만약 최대값이 n보다 작으면 바꾼다 (참)

주의! 초기값 0인 경우 음수의 최대값을 구할 수 없다.

리스트로 접근 혹은 초기값을 가장 작은 것을 할당(`float("-inf")`)



### 문제 8 두번째로 큰 최대값 구하기

1. 최대값 변수 2. 두번째 최대값 변수

   총 2개 변수 세우기

2. 최대보다는 n이 작지만 두번째 최대값보다는 큰 경우

```python
numbers = [0, 20, 100, 40]
#float("-inf") 문제 조건중 가장 작은 수로 하면 됨.
max_number = numbers[0]
second_number = numbers[0]
#1. 전체 숫자를 반복
for n in numbers:
  # 만약에, n이 최대보다 크다면
  if max_number < n:
     # 최대값이었던 것이 두번째로 큰 수
     second_number = max_number
     max_number = n
 # elif secone_number < n < max_number:
    elif secone_number < n and n < max_number:
    second_number = n
```



나는 왜 40이라는 수가 두번째로 크다고 생각하는가? 고찰하기



