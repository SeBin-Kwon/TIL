from collections import deque
import sys
sys.stdin = open('24444.txt', 'r')
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in graph:
    j.sort()

visited = [0] * (n+1)
cnt = 1

def bfs(r):
    global cnt
    queue = deque([r])
    while queue:
        q = queue.popleft()
        visited[q] = cnt
        cnt += 1
        for adj in graph[q]:
            if not visited[adj]:
                visited[adj] = 1
                queue.append(adj)
                
bfs(r)
print(*visited[1:],sep='\n')