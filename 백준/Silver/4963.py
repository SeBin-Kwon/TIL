import sys
sys.stdin = open('4963.txt', 'r')
from pprint import pprint

def dfs(i, j):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    stack = []
    stack.append((i,j))

    while stack:
        x, y = stack.pop()
        m[x][y] = 0

        for k in range(8):
            nx = x+dx[k]
            ny = y+dy[k]

            if 0 <= nx < h and 0 <= ny < w and m[nx][ny] == 1:
                stack.append((nx,ny))
    return 1

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    m = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                cnt += dfs(i,j)
    print(cnt)