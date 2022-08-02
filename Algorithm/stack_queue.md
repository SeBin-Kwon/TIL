# 스택, 큐 (Stack, Queue)

## 1. 스택 (Stack)

> Stack은 쌓는다는 의미로, 마치 접시를 쌓고 빼듯이 **데이터를 한쪽에서만 넣고 빼는 자료구조**
>
> 가장 마지막에 들어온 데이터가 가장 먼저 나가므로 **LIFO(Last-in First-out, 후입선출)** 방식

<br>

### 스택 자료구조의 대표 동작

-  `push`

  스택에 새로운 데이터를 삽입하는 행위

-  `pop`

  스택의 가장 마지막 데이터를 가져오는 행위

- **`후입선출`**

  들어온 순서와 반대로 나감

<br>

###  왜 Stack을 써야할까? (why)

> 데이터 구조를 배우는 이유: 왜 만들어졌고, 언제 써야하는지 알기 위해서

1. **뒤집기, 되돌리기, 되돌아가기**

   후입선출 방식 때문에 데이터를 역순으로 빼내게 됨.

2. **마무리 되지 않은 일을 임시 저장**

   괄호 매칭, 함수 호출, 백트래킹, DFS(깊이 우선 탐색)

   `map(int, input().split())`

<br>

**파이썬은 리스트(List)로 스택을 간편하게 사용 가능**

-  `append()` => `O(1)`

  가장 최신의 데이터를 삽입

-  `pop()` => `O(1)or O(N)`

  가장 최신의 데이터를 빼기

<br>

#### 예시

```python
K = int(input())

input_list = []

for _ in range(K):
    input_list.append(int(input()))
    
stack = []

for elem in input_list
    if elem != 0:
      stack.append(elem)
    else:
      stack.pop()
print(sum(stack))
```

```python
stack = []
for _ in range(int(input())):
    number = int(input())
    
    if number == 0:
        stack.pop()
    else:
        stack.append(number)
print(sum(stack))
```

<br>

## 2. 큐 (Queue)

```python
print(sum(max(min(2, 5), 10), min(2, 5)))

print(12)
```

> Queue는 **한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조**
>
> 가장 먼저 들어온 데이터가 가장 먼저 나가므로 **FIFO(First-in First-out, 선입선출)** 방식

<br>

- **Queue**

  ⬅️ 가장 오래된 데이터 `dequeue`

  가장 최신의 데이터 ⬅️ `enqueue`							    

- **List**

  A[0]										

  ⬅️ 가장 오래된 데이터 `pop()`

  A[-1]
  
  가장 최신의 데이터 ⬅️ `append()`

<br>

### 리스트를 이용한 큐 자료구조의 단점

> **데이터를 뺄 때** 큐 안에 있는 데이터가 많은 경우 **비효율적**이다.
>  맨 앞 데이터가 빠지면서, 리스트의 인덱스가 하나씩 당겨 지기 때문이다 !
>
> -  `pop()` => `O(1)or O(N)`

<br>

### 덱 (Deque, Double-Ended Queue) 자료구조

> **양 방향**으로 삽입과 삭제가 자유로운 큐

- **덱은 양 방향 삽입, 추출이 모두 큐보다 훨씬 빠르다.**
  - 따라서 데이터의 삽입, 추출이 많은 경우, 시간을 크게 **단축** 시킬 수 있다.

**Deque**

- A[0]

  `appendleft()` ➡️

  `popleft()` ⬅️

- A[-1]

  ⬅️ `append()`

  ➡️  `pop()`

<br>

#### 예시

```python
numbers = [1, 2, 3, 4, 5]
queue = deque(numbers)
queue.append(6)
queue.popleft()

for num in queue:
  print(num, end='')
# 2 3 4 5 6

print(list(queue))
# [2, 3, 4, 5, 6]
```

- 형 변환을 안하면 deque 객체가 나온다.

- 리스트는 한번 나열해놓은 값들이 크게 바뀌지 않는다. for문으로 합을 구할 때 값이 변하면 안된다.

- 스택과 큐는 for문이 아닌 while문을 사용하고 값들이 수시로 나갔다가 들어가며 바뀐다.