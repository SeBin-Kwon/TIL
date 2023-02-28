import sys
from collections import deque
sys.stdin = open('1389.txt', 'r')
input = sys.stdin.readline

def bfs(start):
    visited = [-1] * (n+1)
    queue = deque([start])
    visited[start] = 0
    while queue:
        node = queue.popleft()
        for i in friend[node]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[node] + 1
    return sum(visited) + 1

n, m = map(int, input().split())
friend = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

# answer = []
# for i in range(1,n+1):
#     answer.append(bfs(i))

# print(answer.index(min(answer)) + 1)

min_ = 1e9
for i in range(1,n+1):
    temp = bfs(i)
    if min_ > temp:
        min_ = temp
        min_num = i
print(min_num)
