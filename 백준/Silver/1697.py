import sys
from collections import deque
sys.stdin = open('1697.txt', 'r')
input = sys.stdin.readline

def bfs(n):
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            return distance[x]
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= max_ and not distance[i]:
                distance[i] = distance[x] + 1
                queue.append(i)

n, k = map(int,input().split())
max_ = 10**5
distance = [0] * (max_+1)

print(bfs(n))

# x-1, x+1, x*2