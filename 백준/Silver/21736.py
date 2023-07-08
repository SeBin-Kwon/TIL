import sys
from collections import deque
sys.stdin = open('21736.txt', 'r')
input = sys.stdin.readline

def bfs(a,b):
    cnt = 0
    queue = deque([(a,b)])
    visited[a][b] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if not visited[nx][ny] and campus[nx][ny] != 'X':
                if campus[nx][ny] == 'P':
                    cnt += 1
                queue.append((nx,ny))
                visited[nx][ny] = 1
    return cnt


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
campus = [input().rstrip() for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            result = bfs(i,j)

if result:
    print(result)
else:
    print('TT')

