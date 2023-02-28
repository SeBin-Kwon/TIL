import sys
input = sys.stdin.readline

n = int(input())
arr = [[int(1e9)] * (n) for _ in range(n)]
while True:
    a, b = map(int,input().split())
    if a == -1:
        break
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            arr[a][b] = min(arr[a][b],arr[a][k]+arr[k][b])
            if a == b:
                arr[a][b] = 0

max_ = list(map(max, arr))
print(min(max_),max_.count(min(max_)))
for i in range(n):
    if max_[i] == min(max_):
        print(i+1, end=' ')