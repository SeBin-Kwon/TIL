import sys
input = sys.stdin.readline

n, m = map(int,input().split())
table = [list(map(int,input().split())) for i in range(n)]
sum_ = [[0]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
        for j in range(1,n+1):
            sum_[i][j] = table[i-1][j-1] + sum_[i][j-1] + sum_[i-1][j] - sum_[i-1][j-1]

for t in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(sum_[x2][y2] - sum_[x2][y1-1] - sum_[x1-1][y2] + sum_[x1-1][y1-1])
