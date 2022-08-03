import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
k = int(input())

for b in range(k):
    i, j, x, y = map(int,input().split())
    sum_ = 0
    for c in range(i-1,x):
        for d in range(j-1,y):
            sum_ += a[c][d]
    print(sum_)