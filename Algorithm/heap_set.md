# 힙 (Heap), 셋 (Set)

## 1. 힙 (Heap)

> 우선순위 큐 (Priority Queue)는 **우선순위(중요도, 크기 등 순서 이외의 기준)를 기준**으로 가장 우선순위가 높은 데이터가 가장 먼저 나가는 방식

<br>

### 순서가 아닌 우선순위를 기준으로 가져올 요소

1. 가중치가 있는 데이터
2. 작업 스케줄링
3. 네트워크

#### Priority Queue

- ⬅️ **가장 우선순위가 높은 데이터**

  큐의 맨 앞 데이터를 가져오는 행위 `dequeue`

- **가장 최신의 데이터** ⬅️

  큐의 맨 뒤에 데이터를 삽입하는 행위 `enqueue`

<br>

### 우선순위 큐를 구현하는 방법

1. 배열 (Array)
2. 연결 리스트 (Linked List)
3. 힙 (Heap)
   - 힙은 우선순위 큐로 활용할 수 있는 데이터 구조다.

<br>

### 우선순위 큐 구현 별 시간 복잡도

| 연산 종류                | Enqueue (추가) | Dequeue (삭제) |
| ------------------------ | -------------- | -------------- |
| 배열 (Array)             | O(1)           | O(N)           |
| 정렬된 배열              | O(N)           | O(1)           |
| 연결리스트 (Linked List) | O(1)           | O(N)           |
| 정렬된 연결리스트        | O(N)           | O(1)           |
| **힙 (Heap)**            | **O(logN)**    | **O(logN)**    |

<br>

### 힙 (Heap)의 특징

- **최대값 또는 최소값을 빠르게 찾아내도록** 만들어진 데이터구조

- 완전 이진 트리의 형태로 **느슨한 정렬 상태를 지속적으로 유지** 한다.

- 힙 트리에서는 중복 값을 허용한다.

<br>

### Heap은 언제 사용해야 할까?

1. 데이터가 지속적으로 정렬되야 하는 경우
2. 데이터에 삽입/삭제가 빈번할 때

<br>

### 파이썬의 heapq 모듈

> Minheap (최소 힙)으로 구현되어 있음 (가장 작은 값이 먼저 옴)

- 삽입, 삭제, 수정, 조회 **연산의 속도가 리스트보다 빠르다.**

  (배열, 연결리스트, 힙으로 구현 가능)

<br>

#### 힙과 리스트 비교

| 연산 종류   | 힙(Heap) | 리스트(List)   |
| ----------- | -------- | -------------- |
| Get Item    | O(1)     | O(1)           |
| Insert Item | O(logN)  | O(1) 또는 O(N) |
| Delete Item | O(logN)  | O(1) 또는 O(N) |
| Search Item | O(N)     | O(N)           |

<br>

#### 큐와 힙의 사용법 비교

- **Queue**

  ⬅️ 가장 오래된 데이터 `dequeue`

  가장 최신의 데이터 ⬅️ `enqueue`

- **Heap (min)**

  ⬅️ 가장 작은 데이터 `heapq.heappop()`

  가장 큰 데이터 ⬅️ `heapq.heappush()`

<br>

#### 힙 메소드

- `heapq.heapify( )`
- `heapq.heappop(heap)`
- `heapq.heappush(heap, item )`

<br>

#### 예시

```python
import heapq

numbers = [5, 3, 2, 4, 1]

result = heapq.heapify(numbers)
print(result)
# None # 원본을 바꾼다.

print(numbers)
# [1, 3, 2, 4, 5]

heapq.heappop(numbers)
print(numbers)
# [2, 3, 5, 4]

heapq.heappop(numbers)
print(numbers)
# [3, 4, 5]

heapq.heappush(numbers, 10)
heapq.heappush(numbers, 0)
print(numbers)
# [0, 3, 5, 10, 4]


```

- heqppop도 pop처럼 반환 값이 있다.
  - 꺼냈다가 다른 변수에 다시 할당 가능

```python
import heapq

# numbers = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]

heap = []
# heapq.heapify(heap)
N = int(input())
for _ in range(N):
    n = int(input())

    for number in numbers:
        if numbers != 0:
            heapq.heappush(heap, n)
        else:
            if len(heap) == 0:
                print(0)
            else:
                print(heapq.heappop(heap))
```

<br>

## 2. 셋 (Set)

> 셋(set)은 수학에서의 '집합'을 나타내는 데이터 구조로 Python에서는 기본적으로 제공해주는 데이터 구조이다.

<br>

### 셋의 연산

- `.add( )`
- `.remove( )`
- `+` (합집합)
- `-` (차집합)
- `&` (교집합)
- `^` (대칭차집합)

<br>

### Set은 언제 사용해야 할까?

1. 데이터의 중복이 없어야 할 때 (고유값들로 이루어진 데이터가 필요할 때)
2. 정수가 아닌 데이터의 삽입/삭제/탐색이 빈번히 필요할 때

<br>

### 셋(Set) 연산의 시간 복잡도

| 연산 종류   | 시간복잡도             |
| ----------- | ---------------------- |
| 탐색        | O(1) ex) in 오퍼레이터 |
| 제거        | O(1)                   |
| 합집합      | O(N)                   |
| 교집합      | O(N)                   |
| 차집합      | O(N)                   |
| 대칭 차집합 | O(N)                   |

<br>

#### 예시

``` python
s = [
  'baekjoononlinejude', 'startlink', 'codeplus'
]

words = [
  'baekjoon', 'codeplus', 'codeminus'
]

# 풀이 1
cnt = 0

word_set = set(s)

for word in words:
    if word in word_set:
        cnt += 1
print(cnt)

# 풀이 2
print(len(set(words) & set(s))
```