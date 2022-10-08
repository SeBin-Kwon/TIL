import sys
input = sys.stdin.readline

n = int(input())
level = []
for i in range(n):
    level.append(int(input()))

cnt = 0
for i in range(n-2,-1,-1):
    if level[i+1] <= level[i]:
        cnt += level[i] - (level[i+1] - 1)
        level[i] = level[i+1] - 1
print(cnt)
