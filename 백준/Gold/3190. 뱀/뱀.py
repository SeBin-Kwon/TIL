import sys
from collections import deque
input = sys.stdin.readline

def turn(d, c):
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

def start():
    direction = 1
    time = 1
    x, y = 0, 0
    visited = deque([[y, x]])
    board[y][x] = 2
    while True:
        x, y = x + dx[direction], y + dy[direction]
        if 0 <= y < n and 0 <= x < n and board[y][x] != 2:
            if not board[y][x] == 1:
                ty, tx = visited.popleft()
                board[ty][tx] = 0
            board[y][x] = 2
            visited.append([y, x])
            if time in times.keys():
                direction = turn(direction, times[time])
            time += 1
        else:
            return time

dx = [0,1,0,-1]
dy = [-1,0,1,0]

n = int(input())
board = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    a, b = map(int,input().split())
    board[a-1][b-1] = 1
l = int(input())
times = {}
for i in range(l):
    x, c = input().split()
    times[int(x)] = c
print(start())
