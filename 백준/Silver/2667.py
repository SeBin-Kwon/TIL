import sys
from collections import deque
sys.stdin = open('2667.txt', 'r')
input = sys.stdin.readline

# 1 집있음, 0 집없음
# 연결된 집의 모임인 단지를 정의함, 번호도 붙임
# 단지 수 출력, 각 단지에 속하는 집의 수 오름차순 정렬 후 출력

def bfs(x,y):
    global num
    queue = deque([(x,y)])
    visited[x][y] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == '1':
                    visited[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny))
    num += 1
    house.append(cnt)
        
n = int(input())
graph = [input().rstrip() for _ in range(n)]
visited = [[0] * n for _ in range(n)]
house = []
num = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and visited[i][j] == 0:
            bfs(i,j)

house.sort()
print(num)
print(*house, sep='\n')