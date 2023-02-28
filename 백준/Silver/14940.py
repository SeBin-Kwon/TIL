import sys
from collections import deque
sys.stdin = open('14940.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
start = ()
visited = [[-1] * m for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 2:
            start = (i,j)
        elif temp[j] == 0:
            visited[i][j] = 0
    board.append(temp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and board[nx][ny] == 1:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
bfs(start)
for i in visited:
    print(*i)