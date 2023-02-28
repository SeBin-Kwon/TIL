import sys
sys.stdin = open('14938.txt','r')
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
arr = [[int(1e9)] * n for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    arr[a-1][b-1] = l
    arr[b-1][a-1] = l

for k in range(n):
    for a in range(n):
        for b in range(n):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])
            if a == b:
                arr[a][b] = 0

max_ = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if arr[i][j] <= m:
            temp += items[j]
    max_ = max(max_, temp)
print(max_)