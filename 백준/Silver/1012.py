import sys
from collections import deque
sys.stdin = open('1012.txt', 'r')
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(x, y):
    queue = deque([(x, y)])
    land[x][y] = 0 # 방문 처리
    while queue:
        x, y = queue.popleft()
        # 델타탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 지정
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            # 만약 주위에 배추가 있다면
            if land[nx][ny] == 1:
                queue.append((nx, ny))
                land[nx][ny] = 0 # 방문 처리

for t in range(T):
    m, n, k = map(int,input().split())
    land = [[0] * n for _ in range(m)]
    cnt = 0

    for _ in range(k):
        x, y = map(int,input().split())
        land[x][y] = 1
    
    # 배추 찾기
    for i in range(m):
        for j in range(n):
            if land[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)

