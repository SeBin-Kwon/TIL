from  collections import deque
import sys
# sys.stdin = open('1260.txt', 'r')
input = sys.stdin.readline

n, m, v = map(int,input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

# 방문할 수 있는 정점이 여러 개인 경우 번호 작은 것부터 방문 (1번 ~ N번)

for i in range(1,n+1):
    g[i].sort()

# v부터 방문 시작

# 1부터 시작하기 때문에 n+1을 한다.


visited = [0] * (n+1)

def dfs(v):
    print(v,end=' ')
    visited[v] = 1
    for i in g[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

def bfs(v):
    
    queue = deque([v])
    visited[v] = 1

    while queue:
        now = queue.popleft()
        print(now,end=' ')
        for i in g[now]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)

dfs(v)
print()
visited = [0] * (n+1)
bfs(v)