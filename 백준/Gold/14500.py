import sys
sys.stdin = open('14500.txt', 'r')
input = sys.stdin.readline

def dfs(x, y, step, total):
    global answer
    if answer >= total + max_num * (4 - step):
        return
    if step == 4:
        answer = max(answer, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if step == 2:
                    visited[nx][ny] = 1
                    dfs(x, y, step + 1, total + tetromino[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(nx, ny, step + 1, total + tetromino[nx][ny])
                visited[nx][ny] = 0


n, m = map(int, input().split())
tetromino = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
max_num = max(map(max, tetromino))

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, tetromino[i][j])
        visited[i][j] = 0
print(answer)