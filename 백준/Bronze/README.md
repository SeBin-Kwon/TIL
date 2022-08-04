# 백준 Python 문제 풀이 Bronze

## 1000번 A+B

### 정답

```python
A, B = input().split()	# 입력되는 문자를 input()함수로 입력받고 split()함수로 나누어 A,B 변수에 저장

print(int(A)+int(B))	# int() 함수로 A와 B를 정수로 변환 하고 두수의 합을 출력
```

```python
a, b = map(int, input().split())
print(a+b)
```

### 풀이

```python
A, B = input().split()	# 입력되는 문자를 input()함수로 입력받고 split()함수로 나누어 A,B 변수에 저장
```

>  **`input()` 함수** : 사용자로부터 문자열을 입력받을 때 사용하게 된다.

1. `변수 = input()` 이렇게 작성하면 입력받은 문자를 변수에 선언할 수 있게 된다.

2. **문자열 형태로 입력**받으므로, 숫자 1과 2를 입력받는 게 아니라 '1 2'라는 숫자 두 개 사이에 공백이 있는 하나의 문자열을 입력받는다.

   

> **`split()` 함수** : 입력받는 문자를 나눌 때 사용하는 함수이다.

3. 문제를 보면 숫자 두 개를 한 줄에 입력받는데 두 개의 숫자 사이에는 공백으로 구분되어 있다. 이런 경우 공백을 기준으로 숫자를 나누면 된다. 

4. 문자열 뒤에 점을 붙이고 `split( )`을 써주면 된다.

   - `input( ). split( )`은 입력받는 문자가 아직 정해지지 않았으나 어떤 문자이건 공백을 기준으로 나누겠다는 의미이다.

   - 괄호 안에 아무것도 넣지 않으면 공백(띄어쓰기, 탭 등)을 기준으로 문자열을 나눈다. 

5. `A, B = input( ). split( )` 문장에서 = 왼쪽에 A, B 두 개로 구분한 것은 `튜플(tuple)` 자료형의 성질을 이용한 것이다. 

   - `=` 우측에서 입력받은 문자를 공백을 기준으로 나누게 되면 두 개의 문자로 나누어지게 된다. 그 두 개의 문자를 각각 A, B 변수에 저장하겠다는 의미이다.

     

```python
print(int(A)+int(B))	# int() 함수로 A와 B를 정수로 변환 하고 두수의 합을 출력
```

> **`int()` 함수** : 문자형을 숫자형으로 변형할 수 있다. int는 숫자 중에서도 정수를 의미한다. 

6. 문제에서 요구하는 것은 두 개의 정수를 + 연산자로 더하는 것이다. 문자열에서도 + 연산자를 사용할 수 있으나 그러면 '1'과 '2'를 더해서 '12'가 된다.
7. `int()` 를 사용하여 숫자로 변환하면 출력했을 때 두 수를 더한 값이 출력된다.

`map()` 함수를 이용해 `int`로 변환하는 동시에 `input().split()` 함수를 적용할 수도 있다.



---



## 10430번 나머지

### 정답

```python
A,B,C = map(int,input().split())
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')
```

### 풀이

`%`: 나머지 연산자. 

`sep`: 구분자라고 한다. 값 사이에 공백이 아닌 문자를 넣고 싶을 때 사용해 분리하여 출력한다. 다만 분리할 



---



## 2753번 윤년

### 정답

```python
year = int(input())
if ((year%4 == 0)and (year%100 != 0) or (year%400 == 0)):
    print('1')
else:
    print('0')
```

### 풀이

1. `input` 함수로 입력받는 숫자는 문자열로 받으므로 `int` 함수를 통해 정수로 변환한다.
2. 나머지 연산자 `%`를 이용해 배수를 표현한다. 입력받은 수를 4로 나누었을 때, 나머지가 0인 값이 배수다.
3. 4의 배수와 100의 배수가 아닌 두 가지 조건을 모두 만족시켜야 하므로, 두 조건 이 True 일 때 참인 값을 나타내는 연산자 `and`를 통해 표현한다.
4. '또는'을 기준으로 앞, 뒤 중 하나만 True인 값을 나타내는 연산자 `or`를 사용한다.



---

## 2577번 숫자의 개수

```python
d = list(str(a*b*c))
for i in range(10):
    print(d.count(str(i)))
```

1. 입력값 문자열, 리스트로 변형

2. 10번 반복해서 프린트 하는데 

3. `.count()`로 리스트안에 ()값이 있으면 그 개수를 셈

<br>

## 2908번 상수

```python
a, b = input().split()
print(max(int(a[::-1]),int(b[::-1])))

#print(max(int(''.join(reversed(a))), int(''.join(reversed(b)))))
```

문자열로 입력값을 받고 인덱싱으로 거꾸로해서 정수 변환 후 최대값 구하기

<br>

## 8958번  OX 퀴즈

```python
T = int(input())
O = 'O' # 변수명에 저장하면 오타났을 때 금방 알 수 있음
X = 'X'

for i in range(T):
    ox = input()
    count_o = 0 # 연속된 0의 개수
    sum_ = 0 # 점수의 총합
  
  for answer in ox:
      if answer == O:
          count_o += 1 
          # 연속된 0의 개수 1 증가
          sum_ count_o + sum_
      if answer == X:
      # else: # O or X
          count_o = 0 
          # 연속된 0의 개수를 초기화
    print(sum_)
```

<br>

## 2846번 오르막길

```python
# N : 리스트 길이
# 높이 리스트 입력
list_ = list(map(int,input().split()))
# 누적합 저장 변수
sum_ = 0
# 누적합들을 저장할 리스트
sum_list = []

# 오르막길을 찾기 위해서 인덱싱
for i in range(1,len(list_)):
    # 오르막길을 현재 값 > 이전 값
    if list_[i] > list_[i-1]:
        # 오르막길의 전체 길이는 부분 오르막길 길이의 누적합
        sum_ += list[i] - list[i-1] # 누적합
        # 기존 가장 긴 길이와 현재 길이를 비교해서 긴 길이를 저장
        max_sum = max(max_sum,sum_)
        
        # 오르막길일 때마다 누적합을 저장
        # sum_list.append(sum_)
        
    # 오르막길이 아니면
    else:
        # sum_list.append(sum_)
        sum_ = 0
# 남은 누적합을 저장
# sum_list.append(sum_)

# 만약 오르막길이 없으면 0을 출력
if len(sum_list) == 0:
    print(0)
# 만약 오르막길이 있다면 가장 긴 길이 출력
else:
    print(max(sum_list))

# print(max(sum_list))
```

- 파이썬 리스트는 `index[-1]`를 할 경우 맨 끝으로 가게됨.
  - 문법상 맞기 때문에 에러가 뜨지 않는다. 그래서 음수 인덱싱을 할 때엔 주의해야 한다.

- 작은 수과 큰수를 구해서 한번에 빼는건 좀 어려움
  - 앞뒤의 차이를 계속 더해나가서 최종 합친 값을 구하는게 좀더 수월함

<br>

## 2231번 분해합

```python
# 숫자 N 입력
N = int(input())

# 가장 작은 생성자 변수
answer = 0

# 1부터 N 사이의 모든 수의 분해합을 탐색
for number in range(1,N):
    # 분해합 저장 변수
    split_sum = 0
    
    # 각 자리수의 합
    for digit in str(number):
        split_sum = split + int(digit)
      
    # 각 자리수의 합 + 수의 합 => 분해합
    split_sum = split_sum + number
    
    # 구한 분해합과 입력 N이 같으면 number는 N의 생성자
    if N == split_sum:
        print(number)
        # number_list.append(number)
        break # 가장 작은 생성자 탐색
# for-else
# break를 만나지 않으면
else:
    print(0)
```

- 1~n-1까지 모든 경우의 수를 탐색해야함
  - 범위가 정해져 있기 때문에 for문 활용

<br>

## 2851번 슈퍼 마리오

```python
# 왜 안되는지?
n = []
sum_ = 0
for t in range(10):
    n.append(int(input()))

for i in n:
    sum_ += i

    if sum_ == 100:
        print(100)
        break

    if sum_ > 100:        
        if sum_ - 100 > 100 - (sum_ - i):
            print(sum_ - i)
            break
        else:
            break
print(sum_)
```

- 누적합을 이용한다.

- **누적 점수와 100의 절대값 차이가 작으면 작을수록 100에 가깝다**

  - 절대값 함수 abs()

- 가장 작은 차이를 기록해 나간다.

  ```python
  for 점수 in 점수리스트:
      누적점수 += 점수
      차이 = 
  ```

- 같은 차이일 경우 큰 수를 기록해야하는데

  - if 차이 <= 가장작은차이: 이렇게만 해주면 차이는 똑같지만 누적점수는 계속 누적되기 때문에 더 큰 점수가 기록된다.

- 가장 작은 차이를 기록하기 위해 기본 값을 가장 큰 수로 지정한다.

  - `10e9` : 10의 9승
  - `float('inf')` : 무한대

<br>

## 23825번 SASA 모형을 만들어보자

```python
print(min(map(int, input().split())) // 2)
```

<br>

## 3052번 나머지

```python
# 내 코드
number = []                 # 입력값 담을 리스트
for _ in range(10):         # 수 10개 받기
    n = int(input())
    number.append(n)        # 입력값 리스트에 추가

result = []                 # 나머지들 담을 결과값 리스트
for i in number:            # 입력값을 하나씩 꺼내서 연산할 반복문
    result.append(i % 42)   # 입력값을 42로 나눈 나머지 구하고 결과값 리스트에 추가
result = len(set(result))   # 중복 없애고 개수를 셈
print(result)

#

b = [int(input())%42 for i in range(10)]
print(len(set(b)))

#

s = set()
for i in range(10):
    s.add(int(input())%42)
print(len(s))
```

<br>

## 1292번 쉽게 푸는 문제

```python
a,b = map(int,input().split())
 
arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
print(sum(arr[a:b+1]))

#

number_list = []
for i in range(1, 46):
    number_list += [i] * i
    
A, B = map(int, input().split())
print(sum(number_list[A-1:B]))
```

```python
수열 = []
N = 1

while len(수열) < B:
    for i in range(N):
        수열.append(N)
    숫자 += 1

```

- B번째 숫자까지의 합을 구하면 되므로 수열의 길이는 B보다 크면 된다.
  - 수열의 길이 < B 때 까지 계속 더해라
    - while 문
- 수열 문제는 조건을 확실히 잡고 시작하자
- for문을 while문으로 바꾸는 연습하자

<br>

## 5622번 다이얼

```python
dict_ {
  'A':2,'B':2,'C':2,'D:3'...
}
time_ = 0

string
for key in string:
    number = dict_[key]
    time_ += number + 1
print(time_)
```

- 딕셔너리 사용하면 쉽게 풀수 있다.
- 근데 초기값은 다 써야함

<br>

## 5533번 유니크

```python
열_리스트 = []
for x in range(3):
    열 = []
    for y in range(5):
        열.append(리스트[y][x])
    열_리스트.append(열)
    
    
from pprint import pprint

list_ = [[100, 99, 98],
         [100, 97, 92],
         [63, 89, 63],
         [99, 99, 99],
         [89, 97, 98]]

# pprint(list_)
col_list = []
# 리스트를 90도 회전
for x in range(3):
    col = []
    for y in range(5):
        col.append(list_[y][x])

    col_list.append(col)

# 친구들의 점수 리스트
score_list = [0] * 5
for x in range(3):
    col = col_list[x]
    for y in range(5):
        # 친구의 점수
        score = col[y]
        # 친구의 점수가 리스트에서 1개일 때
        if col.count(score) == 1:
            # 친구의 점수가 증가합니다.
            score_list[y] += score
print(score_list)
"""
0
92
215
198
89
"""
```

<br>

## 2167번 2차원 배열의 합

```python
list_ = [[1, 2, 4],
         [8, 16, 32]]

i, j, x, y = 1, 1, 2, 2

i -= 1
j -= 1
x -= 1
y -= 1

sum_ = 0
# 이중 반복문
# i -> x
for r in range(i, x+1):
    # j -> y
    for c in range(j, y+1):
        sum_ += list_[r][c] 

print(sum_)

# 파이썬 제출
# python3 : 메모리 사용이 적고, 속도가 느려요.
# pypy3 : 메모리 사용이 많은데 속도가 빨라요. 
```

- 인덱스에 맞춰서 -1씩 해준다.

<br>
