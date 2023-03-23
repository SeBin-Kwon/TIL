import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    visited = [[0] * w for _ in range(l)]
    queue = deque([(x,y)])
    visited[x][y] = 1
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 'L':
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if cnt < visited[nx][ny]:
                    cnt = visited[nx][ny]
    return cnt - 1
l, w = map(int, input().split())
graph = [input().rstrip() for _ in range(l)]
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(l):
    for j in range(w):
        if graph[i][j] == 'L':
            result = max(result,bfs(i,j))
print(result)