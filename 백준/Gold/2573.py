import sys
from collections import deque
sys.stdin = open('2573.txt','r')
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    seaList = []
    while queue:
        x, y = queue.popleft()
        sea = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif not board[nx][ny]:
                    sea += 1
        # 바다 하나라도 있으면 바다리스트에 추가
        if sea > 0:
            seaList.append((x, y, sea))
    # 탐색 끝나고 바다 개수만큼 녹이기
    for x, y, sea in seaList:
        board[x][y] = max(0, board[x][y] - sea)
    # 빙산 덩이리 1개 리턴하기
    return 1

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ice = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for i in range(1, n-1):
    for j in range(1, m-1):
        if board[i][j]:
            # 빙산인 부분만 얼음리스트에 추가
            ice.append((i, j))

while ice:
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    meltList = []
    for x, y in ice:
        if board[x][y] and not visited[x][y]:
            cnt += bfs(x, y)
        # 탐색 끝나고 바다가 된 빙산 녹인리스트에 추가
        if not board[x][y]:
            meltList.append((x, y))
    if cnt > 1:
        print(answer)
        break
    # 다 녹은 빙산은 탐색 안하다록 빼주기
    ice = sorted(list(set(ice) - set(meltList)))
    answer += 1
if cnt < 2:
    print(0)