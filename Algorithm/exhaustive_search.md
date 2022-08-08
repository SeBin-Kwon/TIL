# 🔦 완전탐색 1 (Exhaustive Search)

## 1. 무식하게 다해보기 (Brute-force)

> Brute-force는 **모든 경우의 수** 를 탐색하여 문제를 해결하는 방식이다.

- **브루트포스(Brute-force)**라고도 하며, 무식하게 밀어붙인다는 뜻이다.
- 가장 단순한 풀이 기법이며, 단순 조건문과 반복문을 이용해서 풀 수 있다.
- 복잡한 알고리즘 보다는, 아이디어를 어떻게 코드로 구현할 것인지가 중요하다.

<br>

### 블랙잭 문제

> 5장 카드 중 3장 뽑고 그 합이 21에 가까워야함

**=> 삼중 for문**

```python
for i in range(5):
    for j in range(5):
        for k in range(5):
# => 125

for i in range(3):
    # 0, 1, 2
    for j in range(i+1,4):
        # 1, 2, 3
        for k in range(j+1,5):
            # 2, 3, 4
```

> 시간 복잡도는 같다. O(N^3)

```python
def blackjack(n, m, cards):
    max_total=0 #현재가장큰합
    # 완전탐색(Brute-force) 
    for i in range(n - 2):
        for j in range(i + 1, n - 1): 
            for k in range(j + 1, n):
                total = cards[i] + cards[j] + cards[k]
                # 현재 가장 큰 합보다는 크고, m을 넘지 않아야 갱신 
                if max_total < total <= m:
                    max_total = total

                # 합과 m이 같으면 더이상 탐색하는 의미가 없으므로 종료 
                if total == m:
                    return total 
    return max_total
```

> 21 수가 바로 주어지면 반복문을 바로 종료

- 3중 for문을 이용해 모든 경우의 수를 탐색

- i, j, k는 세 장의 카드의 인덱스를 의미

- 중복으로 뽑는 경우를 방지하기 위해 range 범위

<br>

## 2. 델타 탐색 (Delta Search)

> (0,0)에서부터 이차원 리스트의 모든 원소를 순회하며 (완전탐색) **각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동** 하는 방식이다.

- 이차원 리스트의 인덱스(좌표)의 조작을 통해서 상하좌우 탐색을 한다. 이때 행과 열의 변량인 -1, +1을 **델타(delta)값** 이라 한다.

<br>

### 델타(delta)값을 이용해 상하좌우로 이동하기

```python
# 1) 행을 x, 열을 y로 표현 dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 2) 행을 r, 열을 c로 표현 dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 상하좌우
for i in range(4):
    nx = x + dx[i] 
    ny = y + dy[i]
```

- 기준값 + 델타값
- (1,1) + (-1,0) => (0,1)
- (1,1) + (0,1) => (1,2)
- (1,1) + (1,0) => (2,1)
- (1,1) + (0,-1) => (1,0)

<br>

```python
delta = [(-1,0),(1,0),(0,-1),(0,1)]
# (1,1)
for i in range(4):
    for j in range(4):
        for d in range(delta):
            print(i+d[0],j+d[1])
```

- 델타값을 하나의 리스트 안에 튜플로 저장하기
  - 이대로 반복문 돌려서 튜플 더하기
  - 다른 언어에서는 안됨

<br>

### ⭐️ 상하좌우로 이동 후 범위를 벗어나지 않는지 확인 및 갱신하기

```python
# 1. 델타값을 이용해 상하좌우 이동 
for i in range(4):
    nx = x + dx[i] 
    ny = y + dy[i]

# **중요**
# 2. 범위를 벗어나지 않으면 갱신
    if 0 <= nx < 3 and 0 <= ny < 3:
        x = nx 
        y = ny
```

- `0 <= nx < 3` 이 수식은 파이썬만 가능
- 기준 x에서 dx만큼 탐색할 때 조건식에 맞는 경우에만 탐색할 수 있게 만드는 식

<br>

### 이차원 리스트의 상하좌우 탐색 정리

```python
# 1.델타값 정의(상하좌우) 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2.이차원 리스트 순회 
for x in range(n):
    for y in range(m):
      
        # 3.델타값을 이용해 상하좌우 이동 
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            
            # 4.범위를 벗어나지 않으면 갱신 
            if 0 <= nx < n and 0 <= ny < m:
                x = nx 
                y = ny
print(x,y)
```

1. 델타 설정
2. 델타 순회
3. 경계값

<br>

### 상하좌우 + 대각선의 8방향 델타값

```python
# 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,-1,1,1]
```