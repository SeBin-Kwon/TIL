import sys
from collections import deque
sys.stdin = open('7576.txt','r')
input = sys.stdin.readline

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx,ny))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m, n = map(int, input().split())
box = []
for i in range(n):
    box.append(list(map(int, input().split())))
queue = deque([])

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i,j))

bfs()

result = max(map(max,box)) - 1
for row in box:
    if 0 in row:
        result = -1
print(result)