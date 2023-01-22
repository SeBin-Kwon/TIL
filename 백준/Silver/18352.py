import sys
from collections import deque
sys.stdin = open('18352.txt', 'r')
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
city = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    city[a].append(b)
visited = [0] * (n+1)
d = [0] * (n+1)
result = []

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        node = queue.popleft()
        for i in city[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                d[i] = d[node] + 1
                if d[i] == k:
                    result.append(i)
    if result:
        result.sort()
        print(*result,sep='\n')
    else:
        print(-1)

bfs(x)