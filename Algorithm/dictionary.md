# 딕셔너리 (Dictionary)

## 1. 해시 테이블

>파이썬 딕셔너리는 Non-sequence & Key-Value
>
>- unordered(순서가 없고) iterable(반복 가능)하다.
>
>- 키는 immutable(변경 불가능) 하며 유니크해야함

딕셔너리는 **해시 테이블(Hash Table)**을 이용하여 Key: Value를 저장

- `해시 함수` : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수
- `해시` : 해시 함수를 통해 얻어진 값

해시 함수와 해시 테이블을 이용하기 때문에 **삽입, 삭제, 수정, 조회 연산의 속도가 `리스트보다 빠르다.`**

`Hash function`을 이용한 산술 계산으로 값이 있는 위치를 바로 알 수 있기 때문에

<br>

### 파이썬의 딕셔너리와 리스트 비교

> 딕셔너리는 모두 `O(1)` 이다.

| 연산 종류   | 딕셔너리(Dictionary) | 리스트(List)                      |
| ----------- | -------------------- | --------------------------------- |
| Get Item    | O(1)                 | O(1)                              |
| Insert Item | O(1)                 | O(1) 또는 O(N) (중간에 넣을 경우) |
| Update Item | O(1)                 | O(1)                              |
| Delete Item | O(1)                 | O(1) 또는 O(N) (중간에 넣을 경우) |
| Search Item | O(1)                 | O(N)                              |

<br>

#### 딕셔너리는 언제 사용해야할까?

1. 리스트를 사용하기 힘든 경우
2. 데이터에 대한 빠른 접근 탐색이 필요한 경우
3. 현실 세계의 대부분의 데이터를 다룰 경우

<br>

## 2. 딕셔너리 기본 문법

### 선언

```pytone
변수 = {key1: value1, key2: value2}
```

<br>

### 삽입/수정

```python
딕셔너리[key] = value
```

- **내부에 해당 key가 없으면 삽입, 있으면 수정**

> 리스트, 딕셔너리 등 조회를 할 땐 대괄호로 찾아 간다.

```python
#Counting

scores = ['A', 'A', 'B', 'C', 'D', 'A', 'B']

counter = {
  'A' : 0,
  'B' : 0,
  'C' : 0,
  'D' : 0
}
for score in scores:
    counter[score] += 1
print(counter)
# {'A' : 3, 'B' : 2, 'C' : 1, 'D' : 1 }
```

```python
from collections import Counter

scores = ['A', 'A', 'B', 'C', 'D', 'A', 'B']

easy_counter = Counter(scores)
print(easy_counter)

# Counter({'A':3})
```

<br>

### 삭제

```python
딕셔너리.pop(key)
```

- 내부에 존재하는 key에 대한 value **삭제 및 반환**

- 존재하지 않는 key에 대해서는 KeyError 발생 (지운다기 보다 빼내는 것에 가깝다.)

```python
딕셔너리.pop(key, default)
```

- 두 번째 인자로 `default(기본)값`을 지정하여 KeyError 방지 가능

<br>

### 조회

key에 해당하는 value 반환

`딕셔너리[key]`

- 조회 했을 때 없으면 KeyError

`딕셔너리.get(key, default)`

- 조회 했을 때 없으면 None 반환
- 두 번째 인자로 `default(기본)값`을 지정하여 KeyError 방지 가능

<br>

## 3. 딕셔너리 메서드

- `.keys()` => ``
  - 딕셔너리의 **key 목록**이 담긴 dict_keys 객체 반환
  - 타입은 dict_key지만 리스트처럼 사용하면 된다.
  - 키가 몇개 있는지?
    - `len(dict.keys())`

  ```python
  a = {
    'name' : 'kyle'
    'gender' : 'male'
    'adress' : 'Seoul'
  }
  
  for key in a:
      print(key)
  # name 
  # gender 
  # address
  ```

- `.value()` => ``

  - 딕셔너리의 **value 목록**이 담긴 dict_values 객체 반환

- `.items()` => ``
  - 딕셔너리의 **(key, value) 쌍 목록**이 담긴 dict_items 객체 반환
    - 원래는 (key, value) 튜플이지만 ()를 생략한 것이다.

  ```python
  a = {
    'name' : 'kyle'
    'gender' : 'male'
    'adress' : 'Seoul'
  }
  
  for item in a.items():
      print(item)
  # ('name', 'kyle')
  # ('gender', 'male')
  # ('adress', 'Seoul')
  
  for key, value in a.items():
      print(key, value)
  # name kyle
  # gender male
  # address Seoul
  ```

#### 예시

```python
game = {
  'Pokemon':'Pikachu'
  'Digimon':'Agumon'
  'Yugioh':'Black Magician'
}
user_input = input()
print(game.get(user_input, "I Don't know"))
```

```python
data = {}
# 1.
number = int(input())

# 2. _는 안쓸 것이라는 뜻
for _ in range(number):
    user_input = input().split()
    # ex) korea seoul
    data[user_input[0]] = user_input[1]
# data['korea'] = 'seoul'

user_answer = input()
# korea

print(data[user_answer])
# data['korea'] => 'seoul'
```

```python
user_input = ['Jay','John','John', 'Jack', 'Jack']
from collections import Counter
print(Counter(user_input))
print(Counter(user_input).most_common())
# 튜플로 정렬 가능하게 만들기
```
