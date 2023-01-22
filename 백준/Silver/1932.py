import sys
sys.stdin = open('1932.txt', 'r')
input = sys.stdin.readline

n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[n-1]))