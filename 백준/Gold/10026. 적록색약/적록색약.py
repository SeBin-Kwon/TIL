import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,v):
    queue = deque([(x,y)])
    v[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not v[nx][ny]:
                if redgreen:
                    if (graph[x][y] == 'B' and graph[nx][ny] != 'B') or (graph[x][y] != 'B' and graph[nx][ny] == 'B'):
                        continue
                    else:
                        v[nx][ny] = 1
                        queue.append((nx,ny))
                else:
                    if graph[nx][ny] == graph[x][y]:
                        v[nx][ny] = 1
                        queue.append((nx,ny))
    return 1
    
n = int(input())
graph = [input().rstrip() for _ in range(n)]
normalvisited = [[0] * n for _ in range(n)]
redgreenvisited = [[0] * n for _ in range(n)]
normalcnt, redgreencnt = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if not normalvisited[i][j]:
            redgreen = False
            normalcnt += bfs(i,j,normalvisited)
        if not redgreenvisited[i][j]:
            redgreen = True
            redgreencnt += bfs(i,j,redgreenvisited)
print(normalcnt, redgreencnt)

