import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    global w, s
    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 'o':
            s += 1
        elif graph[x][y] == 'v':
            w += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#' and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))

r, c = map(int, input().split())
graph = [input().rstrip() for _ in range(r)]
visited = [[0] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
wolf, sheep = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j] != '#' and not visited[i][j]:
            w, s = 0, 0
            bfs(i, j)
            if s > w:
                sheep += s
            else:
                wolf += w
print(sheep, wolf)