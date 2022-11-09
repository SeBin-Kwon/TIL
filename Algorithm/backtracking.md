# Backtracking

> 모든 경우의 수를 탐색하는 대신 조건을 걸어서 유망(promising)하지 않은 경우에는 탐색을 중지하고 이전 노드로 돌아가서 다른 경우를 탐색한다.

- 백준 15649번 N과 M(1)

자리 수가 두 개인 경우는 이중 반복문을 통해서 간단하게 풀 수 있지만, m이 커질 수록 반복문을 계속 중첩시킬 수는 없기 때문에 백트래킹을 사용해야 한다. 조건은 간단하다. **이미 사용(방문)한 경우**라면 **제외**시키면 된다.

일반적인 DFS와의 차이점은 **가지치기**를 한다는 점

```python
def dfs():
    if len(stack) == m:
        print(*stack)
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = 1
        stack.append(i)
        dfs()
        stack.pop()
        visited[i] = 0

n, m = map(int,input().split())

stack = []
visited = [0] * (n+1)

dfs()
```

1. ```python
   n, m = map(int,input().split())
   
   stack = []
   visited = [0] * (n+1)
   ```

   - 출력되기 위해 숫자가 쌓일 stack을 생성
   - 방문처리를 위한 리스트

2. ```python
   def dfs():
       if len(stack) == m:
           print(*stack)
           return
   ```

   - DFS 함수를 만든다.
   -  DFS는 **재귀함수**로 반복될 것이기 때문에 **함수 출력 조건**을 먼저 걸어준다.
   - 리스트 s안에 m개의 요소가 쌓인다면 출력해주도록 한다.
     - *m = 2 일 경우 s = [1, 2] 가 되면 출력*
     - `print(' '.join(map(str, s)))`

3. ```python
   def dfs():
       if len(stack) == m:
           print(*stack)
           return
       for i in range(1, n+1):
           if visited[i]:
               continue
           visited[i] = 1
           stack.append(i)
           dfs()
           stack.pop()
           visited[i] = 0
   ```

   - n = 4, m = 2인 경우
     1. stack은 비어있기 때문에 첫 if문은 통과
     2. for문 진입, i = 1이 되고 방문처리 안되어있기 때문 if문 통과
     3. visited[1] = 1로 방문처리 되고, stack에 추가되어 stack = [1]이 된다.
     4. dfs함수 재실행(2), i = 2일때 stack에 추가
     5. dfs함수 재실행(3)
     6. 첫 if문 조건을 만족하기 때문에 '1 2'가 출력되고 return으로 dfs함수(3)을 빠져나온다.
     7. dfs함수(2)에서 stack.pop() 실행, 2가 빠지고 visited[2] = 0으로 초기화
     8. for문에서 i = 3부터 다시 반복, 4까지 0으로 초기화
     9. dfs함수(2)에서 빠져나와 dfs함수(1) stack.pop()실행
     10. stack = [] 비어지고 visited[1] = 0으로 초기화
     11. for문에서 i = 2 부터 다시 반복

