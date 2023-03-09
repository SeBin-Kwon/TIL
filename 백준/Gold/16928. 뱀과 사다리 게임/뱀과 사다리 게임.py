import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque([1])
    visited[1] = 1
    while queue:
        current = queue.popleft()
        
        for i in range(1, 7):
            next = current + i
            if next < 101:
                if not visited[next]:
                    board[next] = board[current] + 1
                    if move[next]:
                        if not visited[move[next]]:
                            visited[move[next]] = 1
                            board[move[next]] = board[next]
                            queue.append(move[next])
                            if move[next] == 100:
                                return board[100]
                    else:
                        visited[next] = 1
                        queue.append(next)
                        if next == 100:
                            return board[100]
n, m = map(int, input().split())
board = [0] * 101
visited = [0] * 101
move = [0] * 101
for _ in range(n+m):
    u, v = map(int, input().split())
    move[u] = v

print(bfs())