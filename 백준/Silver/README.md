# 백준 Python 문제 풀이 Silver

## 7568번 덩치

```python
N= int(input())

S = [list(map(int, input().split())) for i in range(N)]

for x1, y1 in S:
    result = 1
    for x2, y2 in S:
        if x1 < x2 and y1 < y2:
            result += 1


    print(result, end =' ')
```



<br>

## 1065번 한수

```python
n = int(input())
han = 0

for num in range(1,n+1):
    if num <= 99:
        han += 1
    elif num > 99:
        nummber = list(map(int,str(num)))
        if nummber[0] - nummber[1] == nummber[1] - nummber[2]:
            han += 1
print(han)
```

- 첫번째 자리수 - 두번째 자리수 == 두번째 자리수 - 세번째 자리수 = 한수
  - 자리수가 2개인 수는 무조건 한수

<br>

## 7785번 회사에 있는 사람

```python
N = int(input())
logs = dict()
for i in range(N):
    # 공백으로 나눠진 두개의 단어
    # print(input().split())
    key, value = input().split()
    logs[key] = value 


# print(logs)

list_ = []
for key in logs:
    # print(key) 
    # value가 enter인 key를 찾아서 리스트에 저장
    if logs[key] == "enter":
        list_.append(key)

# print(list_)
list_.sort(reverse=True)
# print(list_)
for name in list_:
    print(name)
```

- 딕셔너리 사용 문제
- value가 출근인 key를 모은다.
- 딕셔너리는 리스트의 상위호환 느낌이므로 꼭 연습해서 마스터하자
- `.sort(reverse=True)`
  - 원본을 덮어 씌우는 것
- `sort()[::-1]`
  - 출력만 거꾸로 출력
  - 원본은 그대로임

<br>

## 1302번 베스트셀러

```python
n = int(input())
dict = {}
result = []

for i in range(n):
    book = input()
    if book not in dict:
        dict[book] = 1
    elif book in dict:
        dict[book] += 1
for k in dict:
    if dict[k] == max(dict.values()):
        result.append(k)
print(sorted(result)[0])
```

1. **key를 기준으로 정렬(오름차순)**

- `sorted(a.key())`

  -  key만 정렬된 값 반환

    `['a', 'c', 'e']`

- `sorted(a.items())`

  - 키를 기준으로 정렬하고 key와 value를 튜플로 묶어서 정렬된 값 반환

    `[('a',2), ('c',4), ('e'.2)]`

2. **value를 기준으로 정렬**

- `sorted(a.value())`

3. **람다식을 이용하여 정렬**

- `sorted(a.items(), key=lambda x: x[0])`
  - x[0]은 key값을 기준으로 정렬하는 것을 의미함

- `sorted(a.items(), key=lambda x: x[1]`
  - x[1]은 value값을 기준으로 정렬하는 것을 의미함

- 내림차순으로 정렬하려면 `sorted(a.key(), **reverse=True**)` 와 같이 마지막에 reverse=True 옵션만 추가해주면 됨

<br>

## 1764번 듣보잡

```python
n,m,*l=open(0).read().split()
n=int(n)
s=sorted(set(l[:n])&set(l[n:]))
print(len(s),*s,sep='\n')


import sys
n, m = map(int, input().split())
nameList = sys.stdin.read().splitlines()
hearset = set(nameList[:n])
seeset = set(nameList[n:])
ret = list(hearset & seeset)
ret.sort()
print(len(ret))
for i in ret:
    print(i)
```

<br>

## 23253번 자료구조는 정말 최고야

```python
# sys.stdin.readline() : 빠르다.
# input() : 느리다.

answer = 'Yes'
stack_list = [[12, 4, 1], [6, 2], [9, 3, 7], [11, 10 ,8, 5]]

for stack in stack_list:
    # stack = [11, 10, 8, 5]
    # stack = [5, 1, 4, 3]
    # 비교값을 pop을 통해서 스택에서 꺼내온다.
    # 5
    comparison = stack.pop()

    # 스택이 비어있지 않을 때 까지
    while len(stack) != 0
        # top comparison 비교
        if stack[-1] > comparison:
            # pop을 사용해서 comparison 값을 갱신
            comparison = stack.pop()
        else:
            answer = 'No'
            break
print(answer)
```

- 맨 위에 있는 값을 pop해서 comparison 변수에 할당, 현재 가장 위에 있는 top과 비교한다.
- 만약 top이 더 크면 pop해서 comparison 변수에 할당
- while문으로 스택이 비어있을 때 까지 비교하고 빼낸다.

<br>

## 9012번 괄호

```python
LEFT = '('
RIGHT = ')'

brackets = ["(", "(", ")", ")", "(", ")", ")"]
left_stack = []
right_stack = []

for bracket in brackets:
    # 괄호가 좌괄호이면
    if bracket == LEFT:
        # left stack push
        left_stack.append(bracket)
    # 괄호가 우괄호이면
    if bracket == RIGHT:
        # 좌괄호 스택의 길이가 0이 아닐 때
        # 좌괄호 스택이 비어있지 않을 때
        if len(left_stack) != 0:
            left_stack.pop()
        # 우괄호를 우괄호 스택에 push
        else:
            right_stack.append(bracket)
if len(left_stack) == 0 and len(right_stack) == 0:
    print('Yes')
else:
    print('No')
```

- 왼쪽 스택에 왼쪽 괄호를 넣고 오른쪽 괄호가 나오면 비어있지 않았을 때 pop해줌
- 오른쪽 괄호가 남고 왼쪽 스택이 비어있을 때, 오른쪽 스택에 넣어줌
- 왼쪽과 오른쪽 스택이 모두 길이가 0일 때 'Yes', 아니면 'No'

<br>

## 11286번 절댓값 힙

```python
from heapq import *
N = 18
heap = []
X = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0]

# heappop 값을 뺄 때
root = heappop(heap)
print(root[1])

# heappush 값을 넣을 때
heappush(heap,[abs(x),x])
```

- heappush는 인자로 여러개의 값을 가진 리스트나 튜플로 들어왔을 때 첫번째 값을 기준으로 먼저 정렬하게 된다.

- ```python
  root = heappop(heap)
  print(root[1])
  ```

<br>

## 25192번 인사성 밝은 곰곰이

```python
N = 7
gom = 0
log_list = [
    "ENTER",
    "pjshwa",
    "chansol",
    "chogahui05",
    "ENTER",
    "pjshwa",
    "chansol",
]
list_ = list()
set_ = set()
for log in log_list:
    if log == "ENTER":
        list_.clear()

    else:
        # 닉네임 = log
        # 리스트에서 중복을 탐색할 때는 N 만큼의 시간이 필요합니다.
        # 셋에서 중복을 탐색할 때는 1 만큼의 시간이 필요합니다.
        if log not in list_:
            list_.add(log)
            gom += 1

print(gom)
```

- 중복이 있는지 없는지 판별하는 문제

  - `set`으로 풀기
    - 리스트에서 중복을 탐색할 때는 N만큼의 시간이 필요
    - 셋에서는 1만큼의 시간이 필요

- `set.clear()`

  셋을 깨끗하게 지워주기

<br>

## 4396번 지뢰 찾기

### 델타 이동 / 델타 탐색

> 한 좌표를 기준으로 4방위 상하좌우 모두 탐색

- 0과 1이 안겹치게 리스트 만들기
- 4번 반복하면서 델타 값을 더해주면 됨

```python
델타_y = [0, 0, 1, -1]
델타_x = [1, -1, 0, 0]
y, x = 1, 1
for d in range(4):
    탐색_y = y + 델타_y[d]
    탐색_x = x + 델타_x[d]
    print(탐색_y, 탐색_x)
    # 1, 2
    # 1, 0
    # 2, 1
    # 0, 1
```

```python
# 8방위
델타_y = [-1, -1, -1, 0, 0, 1, 1, 1]
델타_x = [-1, 0, 1, -1, 1, -1, 0, 1]
y, x = 1, 1
for d in range(8):
    탐색_y = y + 델타_y[d]
    탐색_x = x + 델타_x[d]
```

<br>

```python
def pprint(list_):
    for row in list_:
        print(row)

# 
# 8방위 델타리스트
델타_y = [-1, -1, -1, 0, 0, 1, 1, 1]
델타_x = [-1, 0, 1, -1, 1, -1, 0, 1]

지뢰 = "*"
빈공간 = "."

n = 8
# 게임보드 = [
#     "...**..*",
#     "......*.",
#     "....*...",
#     "........",
#     "........",
#     ".....*..",
#     "...**.*.",
#     ".....*..",
# ]
# 오픈보드 = [
#     "xxxx....",
#     "xxxx....",
#     "xxxx....",
#     "xxxxx...",
#     "xxxxx...",
#     "xxxxx...",
#     "xxx.....",
#     "xxxxx...",
# ]

n = int(input())
게임보드 = []
for _ in range(n):
    게임보드.append(list(input()))
    
오픈보드 = []
for _ in range(n):
    오픈보드.append(list(input()))

# 결과보드 생성
결과보드 = []
for i in range(n):
    temp = ["."] * n
    결과보드.append(temp)
# pprint(결과보드)


게임보드 = list(게임보드)
오픈보드 = list(오픈보드)
지뢰_발견 = False

# 이중반복문
for y in range(n):
    for x in range(n):
        # 현재 위치가 오픈한 위치
        # 오픈보드 -> x
        if 오픈보드[y][x] == "x":
            지뢰수 = 0
            for d in range(8):
                탐색_y = y + 델타_y[d]
                탐색_x = x + 델타_x[d]
                # 탐색_y 탐색_x의 범위는 리스트를 벗어나면 안된다.
                # 리스트의 범위는 0 ~ 7(리스트의 길이 8)

                if 0 <= 탐색_y <= n-1 and 0<= 탐색_x <= n-1:
                    if 게임보드[탐색_y][탐색_x] == 지뢰:
                        지뢰수 += 1

            결과보드[y][x] = str(지뢰수)
            
            # 현재 오픈한 위치에 지뢰가 있는지 확인 
            if 게임보드[y][x] == 지뢰:
                지뢰_발견 = True

# 지뢰를 발견했으면 모든 지뢰의 위치를 결과보드에 표시
if 지뢰_발견 == True:
    for y in range(n):
        for x in range(n):
            if 게임보드[y][x] == 지뢰:
                결과보드[y][x] = 지뢰

# pprint(결과보드)
for row in 결과보드:
    print("".join(row))
```

<br>

## 2615번 오목

```python
# 상 -> y -= 1
# 하 -> y += 1

# 우 하 우상 우하
dy = [0, 1, -1, 1] 
dx = [1, 0, 1, 1]
BLACK = 1
WHITE = 2
N = 19

board = []

# 오목판 상황 입력
for _ in range(N):
    # 하나의 행을 입력 
    temp_list = list(map(int,input().split()))
    board.append(temp_list)

# 무승부가 발생했을 때 출력하기 위한 값
answer = 0

# 이중 반복문 
for y in range(N):
    for x in range(N):
      
        # 검은색돌이나 흰색돌일때만 델타 탐색을 수행
        if board[y][x] == 1 or board[y][x] == 2:
      
            # 델타 탐색
            for d in range(4):
                # 방향이 바뀔 때마다 동일한 색의 돌의 개수 초기화(1)
                stone_count = 1
                
                # 다음 좌표 탐색
                ny = y + dy[d]
                nx = x + dx[d]

                while True:
                    # 인덱스 조건, 범위를 벗어나면 탈출
                    if not(-1 < ny < N and -1 < nx < N):
                        break

                    # 같은 색(값) 돌인지 확인하는 조건, 다른 색 돌이면 탈출
                    if (board[y][x] != board[ny][nx]):
                        break
                    
                    # 같은 값이고 범위를 벗어나지 않으면 같은 색 돌의 수 + 1
                    stone_count += 1

                    # 같은 방향 다음 좌표를 탐색
                    ny = ny + dy[d]
                    nx = nx + dx[d]
                
                # 돌의 개수가 5개라면 
                if stone_count == 5:
                  
                    # 이전 좌표
                    # 기준 좌표(y, x) 에서 델타 값을 마이너스
                    prev_y = y - dy[d]
                    prev_x = x - dx[d]

                    # 육목인지 판단
                    # 조건 1. 이전좌표가 범위를 벗어나면 오목
                    # if not(-1 < prev_y < N and -1 < prev_x < N):
                    
                    # 조건 2. 기준 좌표의 값과 이전 좌표의 값이 다르면 오목
                    # if board[y][x] != board[prev_y][prev_x]:
                    
                    # 조건 1과 조건2를 만족하면 오목이 완성
                    if not(-1 < prev_y < N and -1 < prev_x < N) or board[y][x] != board[prev_y][prev_x]:
                        # 현재 돌의 색 출력
                        print(board[y][x])
                        
                        # 현재 돌의 좌표를 출력
                        print(y + 1, x + 1)
                        
                        # answer 값 갱신
                        # 승패가 결정났기 때문에 answer 값 출력 X
                        answer = board[y][x]
                        

                        # 실제 코딩테스트에서 사용이 불가능한 방법
                        # exit(0)


# 전체를 반복했는데 무승부일 때 0 출력
if answer == 0:
    print(answer)
```

- 우, 하, 우상, 우하 방향으로 탐색
  - 가장 좌상단에 있는 바둑알을 출력해야하므로
- while문으로 nx, ny의 값을 지속적으로 변화시켜줌
- 육목 판별
  - 기준 좌표 뒤쪽에 같은 색 돌이 있는지 확인해야함
    - 애초에 카운트 시작을 2번째 돌부터 시작하게되면 카운트는 5지만 육목이 될 수 있음

<br>

## 2644번 촌수계산

```python
import sys


def pprint(arr):
    for i in range(len(arr)):
        print(i, arr[i])


sys.stdin = open("_촌수계산.txt")

n = int(input())
start, end = list(map(int, input().split()))

m = int(input())

# 빈 리스트를 (n+1)개를 가진 이차원 리스트
# _ : 값을 사용하지않겠다는 의미
graph = [[] for _ in range(0, n + 1)]

for _ in range(m):
    # 공백을 기준으로 2개의 숫자가 입력되기 떄문에
    x, y = list(map(int, input().split()))

    # 무방향 인접 그래프라서
    graph[x].append(y)
    graph[y].append(x)

# 방문 표시를 할 리스트
visited = [False] * (n + 1)

# dfs를 시작하기위해서 기본값 설정
# 스택에 값을 추가할 때 촌수도 같이 추가한다.
# stack = [start]
stack = []
stack.append((start, 0))
visited[start] = True

# 장답을 출력할 변수
answer = -1

# 스택이 비어있지 않으면 반복
while len(stack) != 0:
    # LIFO, 스택의 가장 위에 있는 값을 저장
    # 번호와 촌수를 같이 pop
    number, count = stack.pop()

    # pop을 한 값이 우리가 원하는 값(end)
    # 촌수가 연결이 안되어있으면 line50~line52 실행 X
    if number == end:
        answer = count
        break

    # 해당하는 값의 인접 그래프를 저장
    adj_graph = graph[number]

    # print(number, adj_graph)

    # 인접하는 값들을 탐색
    for adj_number in adj_graph:
        # 방문한적이 없을 때만 스택에 값을 append
        if not visited[adj_number]:
            # 인접 번호와 촌수 + 1를 같이 append
            stack.append((adj_number, count + 1))
            # 인접 값을 방문 표시
            visited[adj_number] = True

# 그래서 촌수는 어떻게 계산을 해야될까?
# 촌수 출력
print(answer)
```

- (사람번호, 촌수)를 튜플 형태로 dfs에 넣어준다.
  - (7,0) => (2,0+1) => (8,0+1+1)

<br>

## 1063번 킹

```python
input = sys.stdin.readline

# 포지션의 인덱스를 이용해 ord, chr를 위한 리스트
position = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 각 커맨드 당 8방향
commands = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T' : [-1, 0], 'RT' : [-1, 1], 'LT' : [-1, -1], 'RB' : [1, 1], 'LB': [1, -1]}

# 킹의 위치, 스톤의 위치, 명령의 개수
king, stone, n = input().rstrip().split()

# 위치 조작
kx, ky = 8 - int(king[1]), position[ord(king[0]) - 65]
sx, sy = 8 - int(stone[1]), position[ord(stone[0]) - 65]

for _ in range(int(n)):
    command = input().rstrip()
    dx, dy = commands[command]

    nx = kx + dx
    ny = ky + dy
    # 킹 와 스톤의 위치가 범위 내에 있는지 파악
    if 0 <= nx < 8 and 0 <= ny < 8 and 0 <= sx < 8 and 0 <= sy < 8:
        # 만약 킹이 움직일려고 하는 위치가 스톤의 위치라면
        if nx == sx and ny == sy:
            # 만약 스톤의 위치에서 델타 값 을 더한 위치가 범위내 있는지 파악
            if 0 <= sx + dx < 8 and 0 <= sy + dy < 8:
                sx, sy = sx + dx, sy + dy
                kx, ky = nx, ny
            # 범위가 벗어나면 다음 명령어
            else:
                continue
        else:
            kx, ky = nx, ny

result1, result2 = "", ""

result1 += chr(position[ky] + 65) + str(8 - kx)
result2 += chr(position[sy] + 65) + str(8 - sx)

print(result1)
print(result2)
```

<br>

## 1926번 그림

```python
import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visit[a][b] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if maps[nx][ny] == 1:
                    cnt += 1
                    visit[nx][ny] = True
                    queue.append((nx, ny))
    return cnt
n ,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
land = 0

answer = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and not visit[i][j]:
            answer.append(bfs(i, j))
            land += 1
print(land)
print(max(answer))
```

<br>

## 1926번 그림

```python

```

- 이차원 리스트 DFS 문제
- 델타 탐색을 위한 델타 리스트 만들기
- 
