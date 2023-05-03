import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, ex, ey):
    queue = deque([(x,y)])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            print(board[ex][ey])
            return
        for i in range(8):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < l and 0 <= my < l and not visited[mx][my]:
                board[mx][my] = board[x][y] + 1
                visited[mx][my] = 1
                queue.append((mx,my))
                
dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

T = int(input())
for t in range(T):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    x, y = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    bfs(x, y, ex, ey)

