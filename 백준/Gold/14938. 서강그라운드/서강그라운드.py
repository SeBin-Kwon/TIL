import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
arr = [[int(1e9)] * n for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    arr[a-1][b-1] = l
    arr[b-1][a-1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
            if i == j:
                arr[i][j] = 0

max_value = 0
for i in range(n):
    temp_value = 0
    for j in range(n):
        if arr[i][j] <= m:
            temp_value += items[j]
    max_value = max(max_value, temp_value)
print(max_value)