import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for l in range(6):
            nz = z + dh[l]
            nx = x + dx[l]
            ny = y + dy[l]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y] + 1
                    queue.append((nz,nx,ny))

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

dh = [0, 0, 0, 0, 1, -1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                queue.append((k, i, j))
bfs()
flag = 0
max_num = -2
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 0:
                flag = 1
            max_num = max(max_num, box[k][i][j])

if flag:
    print(-1)
elif max_num == -1:
    print(0)
else:
    print(max_num - 1)