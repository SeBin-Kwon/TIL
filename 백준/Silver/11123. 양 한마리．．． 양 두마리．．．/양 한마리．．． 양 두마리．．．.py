import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == '#' and not visited[nx][ny]:
            dfs(nx, ny)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())
for t in range(T):
    cnt = 0
    grid = []
    h, w = map(int, input().split())
    for i in range(h):
        grid.append(input().rstrip())
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#' and not visited[i][j]:
                dfs(i,j)
                cnt += 1
    print(cnt)